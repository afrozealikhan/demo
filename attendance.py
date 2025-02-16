# Simple attendance check portal

# List of students
students = ['John', 'Alice', 'Bob', 'Emma', 'David']

# Dictionary to store attendance
attendance = {student: False for student in students}

# Function to mark attendance
def mark_attendance(student_name):
    if student_name in attendance:
        attendance[student_name] = True
        print(f"Attendance marked for {student_name}.")
    else:
        print(f"Student {student_name} not found.")

# Function to display attendance
def display_attendance():
    print("\nAttendance Report:")
    for student, present in attendance.items():
        status = "Present" if present else "Absent"
        print(f"{student}: {status}")

# Main program
def main():
    print("Welcome  the Attendance Portal")

    while True:
        print("\nOptions:")
        print("1. Mark Attendance")
        print("2. Display Attendance")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            student_name = input("Enter student's name to mark attendance: ")
            mark_attendance(student_name)
        elif choice == '2':
            display_attendance()
        elif choice == '3':
            print("Exiting the portal.")
            break
        else:
            print("Invalid choice, please try again.")

# Run the portal
if __name__ == "__main__":
    main()

