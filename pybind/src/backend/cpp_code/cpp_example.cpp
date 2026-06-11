#include "cpp_example.hpp"

#include "spdlog/spdlog.h"

int Adder::add(int a, int b) {
    spdlog::info("Adding {} and {}", a, b);
    return a + b;
}