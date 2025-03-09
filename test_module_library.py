# import module_library   ... 1

# import module_library as mm   ...2

from module_library import find_index,test

import sys
courses = ["history","math","physics","compsci"]

# index = module_library.find_index(courses, "physics")       ... 1

# index = mm.find_index(courses, "physics")   .. . 2

index = find_index(courses, "math")
# print(index)
# print(test)

print(sys.path)