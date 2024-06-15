#include "control_flow_graph.h"
#include "scanner.h"
#include <iostream>


int main(int argc,char *argv[]) {
    if(argc != 2) {
        std::cout << "expect 2 arguments" << std::endl;
        return -1;
    }

    auto file_name = argv[1];
    Scanner scanner;
    ControlFlowGraph g(file_name);
    scanner.ParseFile(file_name, g);
    g.Print();
    return 0;
    
}