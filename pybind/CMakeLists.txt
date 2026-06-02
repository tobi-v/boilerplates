cmake_minimum_required(VERSION 3.26)
project(cpp_backend_lib LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)

set(source_files src/backend/cpp_code/cpp_example.cpp)

add_library(${PROJECT_NAME} ${source_files})
target_compile_options(${PROJECT_NAME} PRIVATE -Wall -Wextra -Wpedantic -Werror)
