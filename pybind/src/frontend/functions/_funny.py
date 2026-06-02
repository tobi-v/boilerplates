from cpp_backend_lib import Adder
from numpy import sqrt  # We don't want this to appear externally

class classy:
    def __init__(self):
        self.adder = Adder()

    def sqrt_of_sum(self, a, b):
        return sqrt(self.adder.add(a, b))
