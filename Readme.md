# Activity: Simple Student Records

Objective:

Learn how to store, access, and modify data using nested lists with dictionaries.

---

## Instructions:

1. Create a list containing student records (each student as a dictionary).
2. Display all students in the list.
3. Modify a student’s grade.
4. Calculate and print a student’s average grade.

## Copy this Sample List

```bash
students = [
    {"name": "Alice", "age": 22, "course": "CS", "grades": [85, 90, 88]},
    {"name": "Bob", "age": 24, "course": "IT", "grades": [78, 82, 80]}
]
```

### Expected Output:

```bash
Name: Alice, Age: 22, Course: CS, Grades: [85, 90, 88]
Name: Bob, Age: 24, Course: IT, Grades: [78, 82, 80]

Alice's updated grades: [85, 95, 88]
Alice's Average Grade: 89.33
```

---

Hint:
use sum to calculate all

```python
sum(students[0]["grades"])
```

and divide it by `3`
