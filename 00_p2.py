students = ["Ravi", "Rudransh", "Riya", "Laxmi", "Priyanshu", "Riya", "Riya"]

def searchName(name, students):
    count = 0
    for student in students:
        if student.lower() == name.lower():
            count = count + 1

    return count


name = input("Enter any name ")

findCount = searchName(name, students)

print(f"Total Student found {findCount} with name {name}")
