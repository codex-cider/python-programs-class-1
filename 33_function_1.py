
# Name: Ravi Verma
# Email: ravi@gmail.com

def getStudentInfo():
    name = input("Enter name ")
    mobile = input("Enter Mobile ")
    email = input("Enter email ")
    dob = input("Enter DOB ")
    rollNumber = input("Enter Roll Number ")

    student = {
        "name": name,
        "mobile": mobile,
        "email": email,
        "DOB": dob,
        "rollNumber": rollNumber
    }

    print(student)

    # print(f"Name: {name}")
    # print(f"Mobile: {mobile}")
    # print(f"Email: {email}")
    # print(f"DOB: {dob}")
    # print(f"rollNumber: {rollNumber}")

getStudentInfo()
