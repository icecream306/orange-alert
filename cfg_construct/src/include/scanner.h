#pragma once
#include <string>
#include <vector>
#include "control_flow_graph.h"

enum ScannerState {FUNC_STATE = 0 , BLOCK_ID , BLOCK_RELATIVE , DIV_LINE , CODE_TEXT};
class Scanner {
public:
    Scanner() = default;

    void ParseFile(const char* file_name_,ControlFlowGraph &graph);
private:
    ScannerState state_ = FUNC_STATE;
    std::string func_name_;
    long block_id_;
};