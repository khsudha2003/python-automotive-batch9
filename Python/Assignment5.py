def find_name_duplicates(students_list):
    """
    Finds students whose first name matches another student in the list,
    but have a different surname.

    Args:
        students_list: A list of dictionaries, each with 'name' and 'surname' keys.

    Returns:
        A list of dictionaries for students who meet the duplicate name criteria,
        maintaining only one entry per duplicate name found.
    """
    # Dictionary to store all names encountered: {first_name: [list of surnames]}
    name_map = {}
    # Set to keep track of names we have already added to the results
    # to maintain only one duplicate entry per unique name.
    found_duplicates_names = set()
    result_duplicates = []

    # First pass: Build the name_map
    for student in students_list:
        name = student['name'].lower()
        surname = student['surname'].lower()
        if name not in name_map:
            name_map[name] = set()
        name_map[name].add(surname)

    # Second pass: Identify duplicates based on the criteria
    for student in students_list:
        name = student['name'].lower()
        surname = student['surname'].lower()

        # Check if the name appears more than once (indicated by multiple surnames associated with it)
        if len(name_map[name]) > 1:
            # Check if we've already recorded this specific name in our results
            if name not in found_duplicates_names:
                # Add the original case student details to the result list
                result_duplicates.append(student)
                # Mark this name as found so we don't add subsequent matches of the same name
                found_duplicates_names.add(name)

    return result_duplicates

# --- Example Usage ---

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
