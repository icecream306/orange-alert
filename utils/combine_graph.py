import os
import pickle
import networkx as nx
import sys
from copy import deepcopy

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from clients.orange_visualizeout import EdgeType, NodeType

combined_graph = None
graphs = []
os.chdir('../.temp/')
names = os.listdir()
i=0
for name in names:
    try:
        with open(os.path.join('.',name,'out','contract.gpickle'),'rb') as f:
            graph = pickle.load(f)
            graphs.append(graph)
    except FileNotFoundError:
        print(f"The file {name} does not exist.")
        i = i+1
    except IOError:
        print(f"An error occurred while trying to read the file {name}.")
        i = i+1

print(f'read gpickles completed with {i} file(s) error,combining...')

combined_graph = nx.disjoint_union_all(graphs)

assert combined_graph is not None , 'empty graph'

with open (os.path.join(os.path.dirname(__file__),'combined_graph.gpickle'),'wb') as f:
    pickle.dump(combined_graph,f,pickle.HIGHEST_PROTOCOL)

