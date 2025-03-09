
courses = ['history','math','physics','compscience']
# print(courses[2:])
# print(courses[-3])
# courses.append('art')
# courses_2 = ['sanskrit','politics']
# courses.insert(0, courses_2)
# courses.remove('math')
# courses.pop()
# courses.insert(0,'art')
# popped = courses.pop()
#
# print(popped)
# courses.reverse()

# num = [1,5,9,31,6,2,78,0]
#
# num.sort()
# courses.sort()
# print(min(num))

# print(courses.index('art'))

#########################

# [looping]

# for item in courses:
#     print(item)

# for index, course in enumerate(courses):
#     print(index,course)
#
# course_str = ' - '.join(courses)
#
# print(course_str)
#

# --------------------[tuples]------------------------


# tuples are immutable,no such append,join,remove and oothers  operation does not wprk as list ...

# tuple_1 = ('history','math','physics','compsci')
# tuple_2 = tuple_1
#
# print(tuple_1)
# print(tuple_2)
#
# tuple_1[0] = 'art'
# print(tuple_1)
# print(tuple_2)

# -----------------[sets]-----------------------------

cs_courses = {'history','geography','physics','math','compscience'}
art_courses = {'history','design','politics','math'}
print(cs_courses.intersection(art_courses))
print(cs_courses.union(art_courses))
# print('math' in cs_courses)















