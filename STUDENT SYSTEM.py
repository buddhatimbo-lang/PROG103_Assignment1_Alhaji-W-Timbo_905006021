import time


students = []
# --- 1. Storage (The Data) ---
# This list holds all the student records you enter


# --- 2. Functional Requirements (The Logic) ---
def add_student():
     global students
     """Function to input and process a student record"""
     print("\n--- Add a New Student ---")
     name = input("Enter student name: ")
     student_id = input("Enter student id: ")
     grade = input("Enter Student grade (0-100): ")
     # Create a record (Dictionary)
     record = {"name": name,
              "student_id": student_id,
              "grade": grade}
      # Process: Add the record to our list
     students.append(record)
print("Record saved successfully!")


def view_records():
 global students
 """Function to display the processed results"""
 print("\n--- Current Student Records ---")
 if not students:
  print("No records found. please add a student first.")
 else:
 # Loop through each record to display them
  for s in students:
   print(f" ID: {s['student_id']} | Name: {s['name']} | Grade: {s['grade']}")
  print("\nReturning to menu in 5 seconds...")
  time.sleep(5)


 # --- 3. The Main Terminal Interface (The Loop) ---
def main():
    while True:
        print("\n================================")
        print("STUDENT MANAGEMENT SYSTEM")
        print("================================")
        print("1. Add Student Record")
        print("2. View All Records")
        print("3. Exit Program")
        choice = input("\nSelected an option (1-3): ")
        # Decision structures (if, elif, else)
        if choice == '1':
              add_student()
        elif choice == '2':
                 view_records()
        elif choice == '3':
            print("Closing system. Goodbye!")
            break  # This stops the  loop and exits
        else:
         print("Invalid input! please type 1' 2, or 3.")
        # This starts the application
main()
