course_name = "python"
credits = 3
is_active = True
grades = [85, 92, 78, 90, 88]
student_map = {"alice": 92, "bob": 78, "charlie": 85}

if credits >= 3 and is_active:
    status = "Enrolled"
elif credits == 0:
    status = "Dropped"
else:
    status = "Pending"

for i, grade in enumerate(grades):
    if grade >= 90:
        grades[i] = grade + 2

filtered = [g for g in grades if g >= 85]

def compute_gpa(grades):
    return round(sum(grades) / len(grades), 2)

def letter_grade(score):
    return "A" if score >= 90 else "B" if score >= 80 else "C"

gpa = compute_gpa(grades)
grade = letter_grade(gpa)

class Course:
    def __init__(self, name, credits):
        self.name = name
        self.credits = credits

    def is_advanced(self):
        return self.credits >= 4

cs_course = Course(course_name, credits)
advanced = cs_course.is_advanced()

bonus = lambda x: x + 5
max_grade = max(grades)
min_grade = min(grades)

print(f"Course: {cs_course.name} | GPA: {gpa} | Grade: {grade}")
print(f"Advanced: {advanced} | Filtered: {filtered}")
print(f"Max: {max_grade} | Min: {min_grade}")
