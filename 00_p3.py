class Collage:
    students = []
    faculties = []

    def addStudent(self):
        name = input("Enter name ")
        mobile = input("Enter mobile ")
        email = input("Enter email ")
        rollNo = input("Enter Roll number ")
        student = {
            'name': name,
            'mobile': mobile,
            'email': email,
            'rollN0': rollNo,
        }
        self.students.append(student)

    def addFaculty(self):
        name = input("Enter Faculty Name ")
        dep = input("Enter Department ")
        subject = input("Enter Subject ")
        faculty = {
            'name': name,
            'dep': dep,
            'subject': subject,
        }
        self.faculties.append(faculty)

    def printStudent(self):
        print(f"{self.students}")

    def printFaculty(self):
        print(f"{self.faculties}")

    def options(self):
        print("Choose any one option")
        option = int(input("1. for add student\n2. for add faculty\n3. print student\n4. print faculty\n"))
        if option == 1:
            self.addStudent()
        elif option == 2:
            self.addFaculty()
        elif option == 3:
            self.printStudent()
        elif option == 4:
            self.printFaculty()
        else:
            print("Wrong Option Selected")

    def loopOptions(self):
        continueLoop = True
        while (continueLoop):
            self.options()
            con = input("For continute press 1 else any key ")
            if con == '1':
                continueLoop = True
            else:
                continueLoop = False


collage = Collage()  # Object of Collage Class
collage.loopOptions()
