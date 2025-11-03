#Mini project 22 - Attendence & Leave Manger
#Name - Nibha Singh
#Enrollment No. - 2502140128

#Empty list
students = []

#   Calculations of attendence for eligblity
def calculate_attendance(total, present):
    pct = (present / total) * 100
    leaves = total - present
    cna = int(0.75 * total - present) if pct < 75 else 0
    eligible = pct >= 75
    return pct, leaves, cna, eligible

# Function to add student by taking input & to re-take the input if they put information of classes wrong
def add_record():
    print("\n--- ADD NEW STUDENT RECORD ---")
    name = input("Enter student name: ").strip()

    while True:
        total = int(input("Enter total classes: "))
        present = int(input("Enter classes attended: "))

        if total <= 0 or present < 0:
            print("Invalid input! Total must be positive, present cannot be negative.")
            continue
        elif present > total:
            print(" Input incorrect! 'Present classes' cannot be greater than 'Total classes'.")
            print("Please enter the values again.")
            continue
        else:
            break
    pct, leaves, cna, eligible = calculate_attendance(total, present)

    # To store the record temporarily
    students.append({
        "name": name,
        "total": total,
        "present": present,
        "pct": pct,
        "leaves": leaves,
        "eligible": eligible
    })
    print("\n--------------REPORT----------------------")
    print(f"Name: {name}")
    print(f"Attendance: {pct:.1f}%")
    print(f"Leaves taken: {leaves}")

    if eligible:
        print(f"✅ {name} is eligible.")
    else:
        print(f"{name} is NOT eligible (below 75%).")
        print(f"Attend {cna} more classes to reach 75%.")
    print("--------------END OF REPORT----------------------\n")

# To view all the students using list comprhension
def view_all():
    print("\n--- VIEW ALL STUDENTS ---")
    if not students:
        print("No records found yet.\n")
        return

    for i, s in enumerate(students, 1):
        status = "Eligible ✅" if s["eligible"] else "Not Eligible"
        print(f"{i}. {s['name']} → {s['pct']:.1f}% ({status})")
    print()

# To check if the student is eligible by the name
def check_student():
    print("\n--- SEARCHING STUDENT ---")
    if not students:
        print("No records available. Add students first.\n")
        return
    name = input("Enter student name to check: ").strip().lower()
    found = False
    for student in students:
        if s["name"].lower() == name:
            found = True
            status = "Eligible" if s["eligible"] else "Not Eligible"
            print(f"\nName: {s['name']}")
            print(f"Attendance: {s['pct']:.1f}%")
            print(f"Leaves taken: {s['leaves']}")
            print(f"Status: {status}\n")
            break

    if not found:
        print("No student found with that name.")

# To delete all the clear by using clear function
def clear_records():
    print("\n--- CLEAR ALL RECORDS ---")
    confirm = input("Are you sure you want to delete all data? (Yes/No): ").strip().lower()
    if confirm == "Yes":
        students.clear()
        print("All records cleared!")
    else:
        print("Cancelled.")

def main():
    print("--------------WELCOME TO ATTENDANCE & LEAVE MANAGER----------------------")

    while True:
        print("\nSelect any among these Menu Options:")
        print("1. Add Student Record")
        print("2. View All Students")
        print("3. Search Student by Name")
        print("4. Clear All Records")
        print("5. Exit")

        choice = input("\nPlease enter your choice (1-5): ").strip()

        if choice == "1":
            add_record()
        elif choice == "2":
            view_all()
        elif choice == "3":
            check_student()
        elif choice == "4":
            clear_records()
        elif choice == "5":
            print("\nThank you for using Attendance & Leave Manager!")
            break
        else:
            print("Invalid choice! Please enter a number between 1–5.")

#Running the program
if __name__ == "__main__":
    main()
