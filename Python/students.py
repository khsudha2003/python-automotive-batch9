# A list of 20 students
school_students = [
    {'name': 'Alice', 'surname': 'Smith'},
    {'name': 'Bob', 'surname': 'Johnson'},
    {'name': 'Charlie', 'surname': 'Williams'},
    {'name': 'David', 'surname': 'Brown'},
    {'name': 'Eve', 'surname': 'Jones'},
    {'name': 'Frank', 'surname': 'Garcia'},
    {'name': 'Grace', 'surname': 'Miller'},
    {'name': 'Henry', 'surname': 'Davis'},
    {'name': 'Ivy', 'surname': 'Rodriguez'},
    {'name': 'Jack', 'surname': 'Martinez'},
    # Duplicates start here:
    {'name': 'Alice', 'surname': 'Williams'}, # Match for first Alice, different surname
    {'name': 'Bob', 'surname': 'Smith'},      # Match for first Bob, different surname
    {'name': 'Eve', 'surname': 'Davis'},      # Match for first Eve, different surname
    {'name': 'Jack', 'surname': 'Johnson'},  # Match for first Jack, different surname
    {'name': 'Frank', 'surname': 'Brown'},    # Match for first Frank, different surname
    # Another entry for Alice to test the "maintain only one duplicate" rule
    {'name': 'Alice', 'surname': 'Davis'},
    # Unique students to reach 20 total
    {'name': 'Liam', 'surname': 'Wilson'},
    {'name': 'Mia', 'surname': 'Moore'},
    {'name': 'Noah', 'surname': 'Taylor'},
    {'name': 'Olivia', 'surname': 'Anderson'},
]

# Find the students matching the criteria
students_with_name_duplicates = find_name_duplicates(school_students)

print("Total students in list:", len(school_students))
print("\nStudents who have the same first name as another student (different surname):")
for student in students_with_name_duplicates:
    print(f"- Name: {student['name']}, Surname: {student['surname']}")
