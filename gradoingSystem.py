"""
Write a program to accept the class score and the exam score from the user and
display the grade to the user.
"""

print("GRADING SYSTEM")
print("""
A = >80
B = 70 - 79.9
C = 60 - 69.9
D = 50 - 59.9
F = <50
""")

classScore = float(input("Please Enter The Class Score: "))
examScore = float(input("Please Enter The Exam Score: "))

totalScore = classScore + examScore

if totalScore >= 80:
    print("A")
elif totalScore >= 70 and totalScore <= 79.99:
    print("B")
elif totalScore >= 60 and totalScore <= 69.99:
    print("C")
elif totalScore >= 50 and totalScore <= 59.99:
    print("D")
elif totalScore < 50:
    print("F")
