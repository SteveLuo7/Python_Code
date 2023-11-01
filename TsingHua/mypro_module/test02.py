import math

print(id(math))
print(type(math))

import importlib

a = importlib.import_module("math")
print(a.pi)