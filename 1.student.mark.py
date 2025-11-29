#TODO: Learn how to handle exceptions e.g attempting to list student/course data that doesn't exist

students = [] 
courses = [] 
marks = {} 

def input_student_info():
    n = int(input("\nEnter number of students: "))
    for i in range(n):
        print(f"\nStudent #{i + 1}")
        student_id = input("Student ID: ")
        student_name = input("Student's name: ")
        
        dob = input("Date of birth (dd/mm/yyyy): ")
        d,m,y = dob.split("/")
        dob = (d, m, y)
        
        students.append({"student_id": student_id,
                        "student_name": student_name,
                        "dob": dob})

def input_course_info():
    n = int(input("\nEnter number of courses: "))
    for i in range(n):
        course_id = input("Course ID: ")
        course_name = input("Course's name: ")
        courses.append({"course_id": course_id,
                       "course_name": course_name})

def input_marks():
    if not courses:
        print("No available courses.")
        return
    
    if not students:
        print("No available students.")
        return
    
    list_courses()
    choice = input("Enter course ID: ")
    if choice not in marks:
        marks[choice] = {}
    for s in students:
        marks[choice][s["student_id"]] = float(input(f"Enter Student #{s["student_id"]}'s mark: "))

def list_courses():
    if not courses:
        print("No available courses.")
        return
    
    for c in courses:
        print(f"\n{c["course_id"]} | {c["course_name"]}\n")

def list_students():
    if not students:
        print("\nNo available students.")
        return
    
    for s in students:
        d,m,y = s["dob"]
        print(f"\n{s["student_id"]} | {s["student_name"]} | {d}/{m}/{y}\n")

def show_marks():
    if not marks:
        print("\nNo available marks.")
        return
    
    list_courses()
    choice = input("Enter course ID: ")
    for (student_id, m) in marks[choice].items():
        for s in students:
            print(f"{student_id} | {s["student_name"]}: {m}\n")

def menu():
    print("\n<STUDENT MARK MANAGEMENT>\n"
          "1. Input student information\n"
          "2. Input course information\n"
          "3. Input marks for a given course\n"
          "4. List courses\n"
          "5. List students\n"
          "6. Show marks for a given course\n"
          "0. Exit")

def main():
    while True:
        menu()
        choice = int(input("Enter choice (0-6): "))

        match choice:
            case 1:
                input_student_info()
            case 2:
                input_course_info()
            case 3:
                input_marks()
            case 4:
                list_courses()
            case 5:
                list_students()
            case 6:
                show_marks()
            case _:
                break


if __name__ == "__main__":
    main()