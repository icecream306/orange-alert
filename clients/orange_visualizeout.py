#!/usr/bin/env python3
from typing import Mapping, Set, TextIO
from collections import namedtuple
from enum import Enum
from copy import deepcopy
import os
import sys
import pickle
import logging

import networkx as nx
from networkx.drawing.nx_pydot import write_dot

# IT: Ugly hack; this can be avoided if we pull the script at the top level
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from clientlib.facts_to_cfg import Statement, Block, Function, construct_cfg,load_csv ,load_csv_map # type: ignore


class EdgeType(Enum):
    SEQ = "seq"
    JUMP = "jump"
    CALL = "call"


class NodeType(Enum):
    ARITH = "arith"
    JUMP = "jump"
    SLOAD = "sload"
    SSTORE = "sstore"
    CALLPRI = "callpri"
    CALLPUB = "callpub"
    REVERT = "revert"
    THROW = "throw"
    STOP = "stop"
    CALLDATA = "calldata"
    BLOCKINFO = "blockinfo"
    UNKNOWN = "unknown"

block_begin_stmt = {}
block_end_stmt = {}
call_map = {}

logging.basicConfig(
    filename='visualize.log',       # 指定日志文件名
    format='%(asctime)s - %(name)s - %(levelname)s : %(message)s'  # 日志格式
)

logger = logging.getLogger(__name__)

def emit(s: str, out: TextIO, indent: int=0):
    # 4 spaces
    INDENT_BASE = '    '

    print(f'{indent*INDENT_BASE}{s}', file=out)

def get_node_type(stmt:Statement) -> NodeType:
    # tofix: CALLPUB的tac操作码是什么？
    if stmt.op == "JUMPI":
        return NodeType.JUMP
    if stmt.op == "SLOAD":
        return NodeType.SLOAD
    if stmt.op == "SSTORE":
        return NodeType.SSTORE
    if stmt.op == "CALLPRIVATE":
        return NodeType.CALLPRI
    if stmt.op == "CALL":
        return NodeType.CALLPUB
    if stmt.op == "REVERT":
        return NodeType.REVERT
    if stmt.op == "THROW":
        return NodeType.THROW
    if stmt.op == "STOP":
        return NodeType.STOP
    if stmt.op == "CALLDATALOAD" or stmt.op == "CALLDATACOPY":
        return NodeType.CALLDATA
    if stmt.op == "BLOCKHASH" or stmt.op == "TIMESTAMP":
        return NodeType.BLOCKINFO
    if stmt.op == "UNKNOWN":
        return NodeType.UNKNOWN
    return NodeType.ARITH

def draw_graph(functions: Mapping[str, Function]):
    contract_graph = None
    for function in sorted(functions.values(),key=lambda x: x.ident):
        # todo:打印函数入口节点
        visibility = "public" if function.is_public else "private"
        func_graph = nx.MultiDiGraph()
        draw_block(function.head_block, set(), func_graph)
        if contract_graph is None:
            contract_graph = deepcopy(func_graph)
        else:
            contract_graph = nx.compose(contract_graph,func_graph)
    
    # 根据call_graph构建contract_graph
    for start_stmt,to_block in call_map.items():
        to_stmt = block_begin_stmt[to_block]
        contract_graph.add_edge(start_stmt,to_stmt,edge_type=EdgeType.CALL.value)
    
    # nx.write_gpickle(contract_graph,"contract.gpickle")
    with open("contract.gpickle","wb") as f:
        pickle.dump(contract_graph,f,pickle.HIGHEST_PROTOCOL)
        
    write_dot(contract_graph,"contract.dot")

def draw_block(block: Block,visited: Set[str],func_graph : nx.MultiDiGraph,prev_block : Block = None):
    if block.ident in visited:
        # 添加和前一个块最后语句之间的跳转边
        if prev_block is not None:
            func_graph.add_edge(prev_block.statements[-1].ident,block.statements[0].ident,edge_type=EdgeType.JUMP.value)
        return
    
    visited.add(block.ident)

    prev = [p.ident for p in block.predecessors]
    succ = [s.ident for s in block.successors]

    # 过滤掉要删除的语句
    block.statements = [stmt for stmt in block.statements if stmt.ident not in orange_del_stmt]

    # tofix: find all empty block statement op are
    # assert len(block.statements) != 0, f"block {block.ident} is empty block after deletion !" 
    if len(block.statements) == 0:
        temp_statement = Statement(block.ident+'added',"UNKNOWN",None,None)
        block.statements.append(temp_statement)

    block_begin_stmt[block.ident] = block.statements[0].ident
    block_end_stmt[block.ident] = block.statements[-1].ident
    # 添加block的第一个节点
    func_graph.add_node(block.statements[0].ident,node_type=get_node_type(block.statements[0]).value,source_file=contract_name)

    # 添加和前一个块最后语句之间的跳转边
    if prev_block is not None:
        func_graph.add_edge(prev_block.statements[-1].ident,block.statements[0].ident,edge_type=EdgeType.JUMP.value)

    # 将块内语句顺序添加进图
    for i in range(1,len(block.statements)):
        func_graph.add_node(block.statements[i].ident,node_type=get_node_type(block.statements[i]).value,source_file=contract_name)
        func_graph.add_edge(block.statements[i-1].ident,block.statements[i].ident,edge_type=EdgeType.SEQ.value)
    
    # 记录call关系
    if block.statements[-1].op == "CALLPRIVATE":
        target_block = tac_variable_value[block.statements[-1].operands[0]]
        call_map[block.statements[-1].ident] = target_block

    for succ_block in block.successors:
        draw_block(succ_block,visited,func_graph,block)



def main():
    # sys.path.append("/home/dumbcoo/giga/gigahorse-toolchain/.temp/contract/out/")
    gigahorse_output_dir = "/home/dumbcoo/giga/gigahorse-toolchain/.temp/"
    os.chdir(gigahorse_output_dir)
    contract_names = os.listdir()
    for cname in contract_names:
        os.chdir(os.path.join(gigahorse_output_dir,cname,'out'))
        if len(os.listdir()) == 0:
            logger.warning(f'{cname} error ')
            continue
        global contract_name
        contract_name = cname+'.sol'

        print(f'drawing graph of {contract_name}')

        global tac_variable_value
        # tac_variable_value = load_csv_map('TAC_Variable_Value.csv')
        tac_variable_value = load_csv_map('TAC_Variable_Value.csv')
        
        global orange_del_stmt
        orange_del_stmt = set(x[0] for x in load_csv('Orange_Del_Statement.csv'))

        _, functions,  = construct_cfg()
        
        draw_graph(functions)

        block_begin_stmt.clear()
        block_end_stmt.clear()
        call_map.clear()


if __name__ == "__main__":
    main()
