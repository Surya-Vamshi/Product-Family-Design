import importlib
# from newclass import *
module = importlib.import_module("newclass")
newclass = getattr(module, "newclass")
s = [newclass()]
s.append(newclass())
print("Before Change")
print("S1 x =", s[0].x)
print("S2 x =", s[1].x)
s[0].x = 50
print("After Change")
print("S1 x =", s[0].x)
print("S2 x =", s[1].x)

