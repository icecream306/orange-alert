CMAKE_MINIMUM_REQUIRED(VERSION 3.0)
project(CFG_CONSTRUCT)

set(CMAKE_CXX_STANDARD 17)

include_directories(${CMAKE_CURRENT_SOURCE_DIR}/src/include)
file(GLOB SRC_LIST ${CMAKE_CURRENT_SOURCE_DIR}/src/*.cpp)

# add_compile_options(-fstandalone-debug)
message(STATUS "optional: -fstandalone-debug")


add_executable(constructor ${SRC_LIST})
