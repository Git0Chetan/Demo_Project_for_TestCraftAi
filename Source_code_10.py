class Student:
    def __init__(self, student_id, name, age):
        if not isinstance(student_id, str) or len(student_id) < 3:
            raise ValueError("Student ID must be a string with at least 3 characters")
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("Name must be a non-empty string")
        if not isinstance(age, int) or age < 5 or age > 100:
            raise ValueError("Age must be an integer between 5 and 100")
       
        self.student_id = student_id
        self.name = name.strip()
        self.age = age
        self.grades = {}
   
    def add_grade(self, subject, grade):
        """Add a grade for a subject."""
        if not isinstance(subject, str) or len(subject.strip()) == 0:
            raise ValueError("Subject must be a non-empty string")
        if not isinstance(grade, (int, float)) or grade < 0 or grade > 100:
            raise ValueError("Grade must be a number between 0 and 100")
       
        self.grades[subject.strip().title()] = grade
   
    def get_average_grade(self):
        """Calculate average grade."""
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)
   
    def get_grade(self, subject):
        """Get grade for a specific subject."""
        return self.grades.get(subject.strip().title())
   
    def is_passing(self, passing_grade=60):
        """Check if student is passing (average grade >= passing_grade)."""
        return self.get_average_grade() >= passing_grade
 
class StudentManager:
    def __init__(self):
        self.students = {}
   
    def add_student(self, student):
        """Add a student to the system."""
        if not isinstance(student, Student):
            raise TypeError("Must provide a Student object")
        if student.student_id in self.students:
            raise ValueError(f"Student with ID {student.student_id} already exists")
       
        self.students[student.student_id] = student
   
    def remove_student(self, student_id):
        """Remove a student from the system."""
        if student_id not in self.students:
            raise ValueError(f"Student with ID {student_id} not found")
       
        del self.students[student_id]
   
    def get_student(self, student_id):
        """Get a student by ID."""
        return self.students.get(student_id)
   
    def get_all_students(self):
        """Get all students."""
        return list(self.students.values())
   
    def get_top_students(self, n=5):
        """Get top n students by average grade."""
        all_students = self.get_all_students()
        sorted_students = sorted(all_students, key=lambda s: s.get_average_grade(), reverse=True)
        return sorted_students[:n]
