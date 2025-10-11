students = {
    "Alice": 85,
    "Bob": 70,
    "Charlie": 95
}
a=input("Enter the student's name: ")
if a in students:
    print(f"{a}'s mark: {students[a]}")
else:
    print(f"Student not found.")