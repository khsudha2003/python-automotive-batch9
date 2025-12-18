students = [
    ("Ritik", "kumar"), ("Ravi", "Kumar"), ("Shiva", "Gupta"), ("Shivam", "Kumar"),
    ("Mohan", "Singh"), ("Geeta", "Yadav"), ("Amit", "Patel"), ("Priya", "Singh"),
    ("Rahul", "Sharma"), ("Pooja", "Verma"), ("Anil", "Kumar"), ("Sunita", "Gupta"),
    ("Vikash", "Yadav"), ("Neha", "Patel"), ("Deepak", "Singh"), ("Ritu", "Sharma"),
    ("Karan", "Gupta"), ("Meera", "Verma"), ("Ritik", "Verma"), ("Lata", "Yadav")
]

# Dictionary to store seen first names and their associated surnames
# Format: {first_name: [list_of_surnames_seen]}
name_map = {}

found_pair = False

for first_name, surname in students:
    if first_name in name_map:
        # Check if the current surname is different from any previously recorded surname
        for seen_surname in name_map[first_name]:
            if surname != seen_surname:
                print(f"Found: {first_name} {seen_surname} and {first_name} {surname}")
                found_pair = True
                # Optional: Uncomment 'break' and 'exit()' to stop after the very first pair found
                # break 
        
        # Add the current surname to the list for future comparisons
        name_map[first_name].append(surname)
        
    else:
        # If this is the first time seeing this name, initialize the list with the surname
        name_map[first_name] = [surname]

    # Optional: Exit completely after finding the first pair
    if found_pair:
        break

if not found_pair:
    print("No students found with the same first name and different surnames.")

Output of the code above:
Based on the provided list, the first pair found is:
Found: Ritik kumar and Ritik Verma