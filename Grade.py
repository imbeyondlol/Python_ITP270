#!/bin/python3

subjects = ["physics", "calculus", "poetry", "history"]

grades = [98, 97, 85, 88]



gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

print(gradebook)

gradebook.append(["computer science", 100])

gradebook.append(["visual arts", 93])

gradebook[-1][1] += 5

poetry_grade = grades[subjects.index("poetry")]

grades.remove(poetry_grade)

gradebook.remove(["poetry", poetry_grade])


gradebook.insert(subjects.index("poetry"), ["poetry", "Pass"])

last_semester_gradebook = [["Spanish", 90], ["Statistics", 85], ["Art", 95]]



full_gradebook = last_semester_gradebook + gradebook



print(full_gradebook)
