students = []

def add(students, id, name):
    students.append({ "id": id, "name": name })
    return students

def addStudent():
    id = input("Whats the id\n")
    name = input("Whats the name\n")
    add(students, id, name)

def display(students, id):
    for s in students:
        if s["id"] == id:
            return s

def displayStudent():
    id = input("Whats the id\n")
    student = display(students, id)
    print(student)

def main():
    while True:
        choice = int(input("""
            1. Add student
            2. Display student
            3. Save and Quit\n               
        """))
        if (choice == 1):
            addStudent()
        elif (choice == 2):
            displayStudent()
        else:
            break

# main()


