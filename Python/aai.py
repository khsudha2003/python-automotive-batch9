# List of 20 students (represented as dictionaries)
# Goal: Find the student with the same first name but different surname
students = [
    {"first": "Alice", "last": "Smith"}, {"first": "Bob", "last": "Jones"},
    {"first": "Charlie", "last": "Brown"}, {"first": "David", "last": "Wilson"},
    {"first": "Emma", "last": "Taylor"}, {"first": "Frank", "last": "Miller"},
    {"first": "Grace", "last": "Davis"}, {"first": "Henry", "last": "Garcia"},
    {"first": "Alice", "last": "White"},  # DUPLICATE: Same first name as index 0, different last name
    {"first": "Jack", "last": "Harris"}, {"first": "Kelly", "last": "Clark"},
    {"first": "Liam", "last": "Lewis"}, {"first": "Mia", "last": "Walker"},
    {"first": "Noah", "last": "Hall"}, {"first": "Olivia", "last": "Allen"},
    {"first": "Paul", "last": "Young"}, {"first": "Quinn", "last": "King"},
    {"first": "Ryan", "last": "Wright"}, {"first": "Sophia", "last": "Scott"},
    {"first": "Thomas", "last": "Green"}
]

def find_duplicate_first_names(student_list):
    # Dictionary to track which first names we have seen and their surnames
    seen_first_names = {}
    found_duplicates = []

    for student in student_list:
        first = student["first"]
        last = student["last"]

        if first in seen_first_names:
            # Check if the surname is different
            if seen_first_names[first] != last:
                # Store both the original and the new one
                found_duplicates.append({"first": first, "last": seen_first_names[first]})
                found_duplicates.append(student)
        else:
            seen_first_names[first] = last
            
    return found_duplicates

# Run the search
results = find_duplicate_first_names(students)

# Print results
if results:
    print(f"Found {len(results)} students sharing the same first name but different surnames:")
    for s in results:
        print(f"- {s['first']} {s['last']}")
else:
    print("No such duplicates found.")