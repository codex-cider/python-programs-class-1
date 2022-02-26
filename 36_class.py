class Student:
    name = "Test Name"

    def getName(self):
        print(f"Name is -- {self.name}")


st1 = Student()
st2 = Student()

st1.name = "Ravi Verma"
st1.getName()

st2.name = "Devendra Yadav"
st2.getName()

st2 = st1
st2.getName()
st1.name = "New Name"

st1.getName()

