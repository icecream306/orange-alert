#pragma once

#include <cstdio>
#include <fstream>
#include <ios>
#include <memory>
#include <ratio>
#include <string>
#include <unordered_map>
#include <utility>
#include <vector>
class BlockNode {
public:
  BlockNode(long id, std::vector<long> &&prev_ids, std::vector<long> &&next_ids,
            std::vector<std::string> &&code_text)
      : id_(id), prev_ids_(std::move(prev_ids)), next_ids_(std::move(next_ids)),
        code_text_(std::move(code_text)) {}

private:
  long id_;
  std::vector<long> prev_ids_;
  std::vector<long> next_ids_;

  std::vector<std::string> code_text_{};

  friend class ControlFlowGraph;
};

class ControlFlowGraph {
public:
  ControlFlowGraph(std::string input_file_name) {
    out_file_name_ = input_file_name + "_cfg.dot";
  } 

  void AddNode(long id, std::vector<long> &&prev_ids,
               std::vector<long> &&next_ids, std::vector<std::string> &&code_text) {
    auto node = std::make_shared<BlockNode>(
        id, std::forward<std::vector<long>>(prev_ids),
        std::forward<std::vector<long>>(next_ids),
        std::forward<std::vector<std::string>>(code_text));
    node_map_.insert(std::make_pair(id, node));
  }

  void Print() {
    std::ofstream fout;
    fout.open(out_file_name_,std::ios::out);
    fout << "digraph G {\n";
    for(auto &p : node_map_) {
      auto node = p.second;
      fout << node->id_ << "[" << "shape=\"plain\" color=\"green\" label=<<TABLE BORDER=\"0\" CELLBORDER=\"1\" CELLSPACING=\"0\" CELLPADDING=\"4\">\n";
      fout << "<TR><TD>" << "0x" << std::hex << node->id_ << std::dec << "</TD></TR>\n";
      
      fout << "<TR><TD>";
      for(auto &statement : node->code_text_) {
        fout << statement << "<BR/>\n";
      }
      fout << "</TD></TR>\n";
      fout << "</TABLE>>];\n";
      // 打印连接所有后继节点的边
      for(auto &next_id : node->next_ids_) {
        fout << node->id_ << "->" << next_id << "\n";
      }
    }
    fout << "}\n";
  }

private:
  std::unordered_map<long, std::shared_ptr<BlockNode>> node_map_;
  std::string out_file_name_;
};