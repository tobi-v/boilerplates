cmake_minimum_required(VERSION 3.26)

PROJECT(bindings LANGUAGES CXX)
set(CMAKE_CXX_STANDARD 20)


if (CMAKE_COMPILER_IS_GNUCXX)
    add_definitions("-fPIC")
endif()

file(GLOB python_srcs CONFIGURE_DEPENDS *.cpp)

find_package(Python3 REQUIRED COMPONENTS Development Interpreter)

add_subdirectory(../../../external/pybind11 pybind11_build)
add_subdirectory(../../.. cpp_backend_lib_build)

add_library(_cpp_backend_pybind MODULE ${python_srcs})
set_target_properties(_cpp_backend_pybind PROPERTIES PREFIX "")
target_link_libraries(_cpp_backend_pybind PRIVATE
        cpp_backend_lib
        pybind11::module)

if (CMAKE_LIBRARY_OUTPUT_DIRECTORY) 
  configure_file(${PROJECT_SOURCE_DIR}/__init__.py ${CMAKE_LIBRARY_OUTPUT_DIRECTORY}/cpp_backend_lib/__init__.py COPYONLY)
endif()
