#include "scanner.h"
#include <algorithm>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <ios>
#include <iostream>
#include <string>
#include <vector>

void Scanner::ParseFile(const char *file_name, ControlFlowGraph &graph) {
  std::ifstream fin;
  fin.open(file_name, std::ios::in);
  std::vector<long> prev_ids;
  std::vector<long> next_ids;
  std::vector<std::string> code;
  std::string line;
  while (std::getline(fin, line)) {
    if (state_ == ScannerState::FUNC_STATE) {
      // if (line.empty() || line[0] == '\n') {
      //   continue;
      // }

      // auto b = line.find("function");
      // func_name_ = line.substr(b + 8);
      // func_name_.pop_back();

      auto str = line.c_str();
      auto off = strspn(str, " \t");
      str += off;
      if ((*str) != '\0') {
        func_name_ = std::string(str);
        state_ = ScannerState::BLOCK_ID;
      }

    } else if (state_ == ScannerState::BLOCK_ID) {
      auto str = line.c_str();
      auto off = strspn(str, " \t");
      str += off;
      if(strlen(str)==0) {
        continue;
      }
      if(*str=='}') {
        state_ = ScannerState::FUNC_STATE;
        continue;
      }
      char *dummy_endpointer;
      auto id_str = strstr(str, "0x");
      block_id_ = strtol(id_str, &dummy_endpointer, 0);
      state_ = ScannerState::BLOCK_RELATIVE;

    } else if (state_ == ScannerState::BLOCK_RELATIVE) {
      prev_ids.clear();
      next_ids.clear();
      auto str = line.c_str();
      char *dummy_endpointer;
      str = strpbrk(str, "=");
      str += 2;
      std::string addr;
      while ((*str) != ']') {
        if ((*str) == ',') {
          prev_ids.push_back(strtol(addr.c_str(), &dummy_endpointer, 16));
          addr.clear();
        } else if ((*str) != ' ') {
          addr.push_back((*str));
        }
        ++str;
      }

      str = strpbrk(str, "=");
      str = strstr(str, "0x");

      while (str != nullptr) {
        next_ids.push_back(strtol(str, &dummy_endpointer, 0));
        str = dummy_endpointer;
        str = strstr(str, "0x");
      }
      state_ = ScannerState::DIV_LINE;
    } else if (state_ == ScannerState::DIV_LINE) {
      state_ = ScannerState::CODE_TEXT;
      continue;
    } else if (state_ == ScannerState::CODE_TEXT) {
      auto str = line.c_str();
      auto off = strspn(str, " \t");
      str += off;
      if (strlen(str) == 0 || (*str) == '\n') {
        graph.AddNode(block_id_, std::move(prev_ids), std::move(next_ids),
                      std::move(code));
        state_ = ScannerState::BLOCK_ID;
      } else if ((*str) == '}') {
        graph.AddNode(block_id_, std::move(prev_ids), std::move(next_ids),
                      std::move(code));
        func_name_.clear();
        state_ = ScannerState::FUNC_STATE;
      } else {
        code.push_back(str);
      }
    }
  }
}