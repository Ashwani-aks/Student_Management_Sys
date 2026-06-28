# make new student
class Student:
    def __init__(self, name, age, grade, course):
        self.name = name
        self.age = age
        self.grade = grade
        self.course = course

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Grade:", self.grade)
        print("Course:", self.course)

# Student Management System
class STM:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def update_student(self, old_student, new_student):
        if old_student in self.students:
            index = self.students.index(old_student)
            self.students[index] = new_student
        else:
            print("Student not found in the list.")

    def delete_student(self, student):
        if student in self.students:
            self.students.remove(student)
        else:
            print("Student not found in the list.")

    def search_student(self, name):
        for student in self.students:
            if student.name == name:
                return student
        return None

    def display_students(self):
        for student in self.students:
            student.display()
            print()


# Example usage
stm = STM()

student1 = Student("Alice", 20, "A", "Computer Science")
student2 = Student("Bob", 22, "B", "Mathematics")

# Add students
stm.add_student(student1)
stm.add_student(student2)

# Display all students
stm.display_students()