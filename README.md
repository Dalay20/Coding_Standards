# 🎓 Student Grade Management System

A simple **Python** project that manages student records, grades, averages, letter grades, pass/fail status, and honor roll eligibility.

---

## 📋 Core Features

1. **Add Students**
   - Each student record includes a **Student ID** and a **Name**.
   - Both fields are required and validated to be non-empty.

2. **Add Grades**
   - Each student can have multiple numeric grades (0–100).
   - Invalid or out-of-range values are rejected.

3. **Calculate Average Grade**
   - Automatically computes the average of all grades.

4. **Determine Letter Grade**
   - Converts the average score into a letter grade:

     | Range | Letter |
     |--------|--------|
     | 90–100 | A |
     | 80–89  | B |
     | 70–79  | C |
     | 60–69  | D |
     | < 60   | F |

5. **Determine Pass/Fail**
   - Students with an average of **60 or higher** are marked as **Passed**, otherwise **Failed**.

6. **Honor Roll Detection**
   - Students with an average of **90 or higher** are automatically placed on the **Honor Roll**.

7. **Remove Grades**
   - Grades can be removed:
     - By **index** (e.g., the 2nd grade), or
     - By **value** (e.g., 95.0).
   - Handles missing or invalid values gracefully.

8. **Generate Summary Report**
   - Displays a full student report with:
     - Student ID  
     - Student Name  
     - List of Grades  
     - Number of Grades  
     - Average Grade  
     - Letter Grade  
     - Pass/Fail Status  
     - Honor Roll Status  

---

## 🚀 Example Usage

```python
from student import Student

# Create a student
student_a = Student("S001", "Alice Smith")

# Add grades
student_a.add_grade(95)
student_a.add_grade(88.5)
student_a.add_grade(76)

# Remove a grade
student_a.remove_grade_by_index(1)

# Generate a report
print(student_a.generate_report())
