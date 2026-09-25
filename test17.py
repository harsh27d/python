class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_average(self):
        total = 0

        for mark in self.marks:
            total = total + mark

        return total / len(self.marks)

    def check_result(self):
        average = self.calculate_average()

        if average >= 40:
            return "Pass"
        else:
            return "Fail"


student = Student("Harsh", [75, 68, 82, 70, 65])

print("Name:", student.name)
print("Marks:", student.marks)
print("Average:", student.calculate_average())
print("Result:", student.check_result())