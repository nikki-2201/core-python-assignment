class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_average(self):
        return round(sum(self.marks) / len(self.marks), 2) if self.marks else 0


def main():
    students = {}
    try:
        n = int(input("Enter the number of students: "))
        if n <= 0:
            print("Please enter a valid number of students.")
            return

        for _ in range(n):
            name = input("Enter student name: ").strip()
            while not name:
                name = input("Name cannot be empty. Enter student name: ").strip()

            marks_input = input(f"Enter marks for {name}, separated by commas: ").strip()
            while not marks_input or not all(mark.isdigit() for mark in marks_input.split(',')):
                marks_input = input(f"Invalid marks entered. Please enter valid marks for {name}, separated by commas: ").strip()

            marks = list(map(int, marks_input.split(",")))
            students[name] = Student(name, marks)

        averages = {name: student.calculate_average() for name, student in students.items()}

        top_student = max(averages, key=averages.get)
        top_student_avg = averages[top_student]

        print("\nAverage Marks:", averages)
        print(f"Top Performer: {top_student} with an average of {top_student_avg}")
    
    except ValueError:
        print("Invalid input! Please enter valid numbers.")
    

if __name__ == "__main__":
    main()
