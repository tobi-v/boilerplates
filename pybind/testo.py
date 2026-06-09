from tobi.functions import classy
from numpy._globals import _NoValueType

nov = _NoValueType()
print(f"nov: {nov}")
sd = classy()
a = 11
b = 5
res = sd.sqrt_of_sum(a, b)

print(f"sqrt({a} + {b}) = {res}")
