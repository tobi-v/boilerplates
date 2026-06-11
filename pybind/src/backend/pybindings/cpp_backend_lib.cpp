#include "../cpp_code/cpp_example.hpp"
#include "spdlog/spdlog.h"

#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <pybind11/stl.h>
namespace py = pybind11;

void bind_adder(py::module& m) {
  py::class_<Adder>(m, "Adder")
      .def(py::init<>())
      .def("add", &Adder::add);
}

PYBIND11_MODULE(_cpp_backend_pybind, m) {
  py::options ops;
  ops.enable_enum_members_docstring();
  ops.disable_function_signatures();

  spdlog::info("Initializing C++ backend pybind module");
  bind_adder(m);
}