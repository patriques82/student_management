students = []

def add(students, id, name):
    students.append({ "id": id, "name": name })
    return students

def addStudent():
    id = input("Whats the id")
    name = input("Whats the name")
    add(students, id, name)

def main():
    choice = int(input("""
        1. Add student
        2. Remove student
    """))
    if (choice == 1):
        addStudent()
    else:
        pass


