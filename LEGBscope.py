'''
LEGB rule in python
# local,enclosing,global,built-in
Local (L): The current scope, which could be a function, class, or block of code.
Enclosing (E): The scope of any enclosing functions or classes. This applies to nested functions or classes.
Global (G): The top-level scope of the module or script.
Built-in (B): The scope of built-in functions and constants in Python (e.g., len, print, True).
'''

# x = 'global x'

# def test():
#     y = 'local y'
#     print(y)
# test()


import builtins
print(dir(builtins))

m = min([5,1,3,4,8,9])
print(m)





















