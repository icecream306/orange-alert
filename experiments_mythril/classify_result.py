import json
import os
import shutil

def load_json_data(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def process_files(json_data, input_dir, output_dirs):
    contract_dict = {item['contract_name']: item['targets'] for item in json_data}
    
    for filename in os.listdir(input_dir):
        if filename.startswith('out_') and filename.endswith('.hex'):
            contract_name = filename[4:-4]  # Remove 'out_' prefix and '.hex' suffix
            file_path = os.path.join(input_dir, filename)
            
            with open(file_path, 'r') as f:
                content = f.read()
            
            has_swc_104 = "SWC ID: 104" in content
            target = contract_dict.get(contract_name+'.sol')
            
            if target is not None:
                if has_swc_104 and target == 0:
                    dest_folder = output_dirs['fp']
                elif not has_swc_104 and target == 0:
                    dest_folder = output_dirs['tn']
                elif has_swc_104 and target == 1:
                    dest_folder = output_dirs['tp']
                elif not has_swc_104 and target == 1:
                    dest_folder = output_dirs['fn']
                else:
                    continue  # Skip if doesn't match any condition
                
                shutil.copy(file_path, os.path.join(dest_folder, filename))

def main():
    json_file = '/home/dumbcoo/orange-alert/dataset/ucllc_labels.json'  # 请替换为实际的JSON文件路径
    input_directory = '/home/dumbcoo/orange-alert/experiments_mythril/output'  # 请替换为实际的输入目录路径
    output_directories = {
        'fp': '/home/dumbcoo/orange-alert/experiments_mythril/res_classified_test/fp',
        'tn': '/home/dumbcoo/orange-alert/experiments_mythril/res_classified_test/tn',
        'tp': '/home/dumbcoo/orange-alert/experiments_mythril/res_classified_test/tp',
        'fn': '/home/dumbcoo/orange-alert/experiments_mythril/res_classified_test/fn'
    }
    
    # 确保输出目录存在
    for dir_path in output_directories.values():
        os.makedirs(dir_path, exist_ok=True)
    
    json_data = load_json_data(json_file)
    process_files(json_data, input_directory, output_directories)

if __name__ == "__main__":
    main()