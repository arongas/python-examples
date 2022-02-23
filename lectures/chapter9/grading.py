student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for key in student_scores:
    score = student_scores[key]
    if score >= 91:
        value = "Outstanding"
    elif score >= 81:
        value = "Exceeds Expectations"
    elif score >= 71:
        value = "Acceptable"
    else:
        value = "Fail"
    student_grades[key] = value

print(student_grades)
