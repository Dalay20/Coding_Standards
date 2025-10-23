"""Student grade management system."""


class Student:
    """Represents a student and their grades."""

    def __init__(self, student_id, name):
        """Initialize a student with ID, name, and empty grades list."""
        self.id = student_id
        self.name = name
        self.grades = []
        self.is_passed = False
        self.honor = None

    def add_grades(self, grade):
        """Add a numeric grade to the student record."""
        if isinstance(grade, (int, float)):
            self.grades.append(grade)
        else:
            print(f"Invalid grade '{grade}', must be a number.")

    def calc_average(self):
        """Return the average of all grades."""
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def check_honor(self):
        """Determine if the student qualifies for honors."""
        if self.calc_average() > 90:
            self.honor = True
        else:
            self.honor = False

    def delete_grade(self, index):
        """Delete a grade safely by index."""
        if 0 <= index < len(self.grades):
            del self.grades[index]
        else:
            print("Index out of range.")

    def report(self):
        """Print the student's report."""
        avg = self.calc_average()
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Grades Count: {len(self.grades)}")
        print(f"Average: {avg:.2f}")
        print(f"Honor: {'Yes' if self.honor else 'No'}")


def start_run():
    """Test the Student class."""
    a = Student("x", "Alice")
    a.add_grades(100)
    a.add_grades(50)
    a.calc_average()
    a.check_honor()
    a.delete_grade(1)
    a.report()


if __name__ == "__main__":
    start_run()
