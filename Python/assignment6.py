# List of 20 students (first_name, surname)
students =[("Amit", "Sharma"),("Rahul", "Verma"),("Amit", "Patel"),
           ("Neha", "Singh"),("Rohit", "Mehta"),("Rahul", "Gupta"),
           ("Priya", "Kapoor"),("Anjali", "Iyer"),("Neha", "Chopra"),
           ("Vikas", "Yadav"),("Suresh", "Kumar"),("Pooja", "Malhotra"),
           ("Ravi", "Joshi"),("Anjali", "Nair"),("Karan", "Bansal"), 
           ("Rohit", "Agarwal"),("Manoj", "Tiwari"),("Pooja", "Arora"),
           ("Sunil", "Khanna"),("Vikas", "Mishra")]

# Dictionary to keep only one student per first name
unique_students = {}

for first_name, surname in students:
    # If first name not already stored, add it
    if first_name not in unique_students:
        unique_students[first_name] = surname

# Display result
print("All students with out removing dulpicates (same name, different surname):")
for first_name, surname in unique_students.items():
    print(f"{first_name} {surname}")