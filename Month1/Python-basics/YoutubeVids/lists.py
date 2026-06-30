# Python Tutorial for Beginners4: Lists, Tuple, and Sets
courses = ["History","Math","Physics"]
courses2 = ["PE", "Chemistry"]
print(courses)
print(len(courses))
print(courses[1])
print(courses[-1])
print(courses[1:])

courses.append("Art")
print(courses)

courses.insert(1,"Science")
print(courses)

courses.extend(courses2)
print(courses)

popped = courses.pop()
print(courses)
print(popped)

courses.reverse()
print(courses)

courses.sort()
print(courses)

courses.sort(reverse=True)
print(courses)

sorted_course = sorted(courses)
print((sorted_course))

# Min, Max, Sum(list of numbers)

print(courses.index("Art"))
print('Art' in courses)

for index, course in enumerate(courses, start = 1):
    print(index, course)

course_str = ', '.join(courses)
new_list = course_str.split(" - ")
print(course_str)
print(new_list)