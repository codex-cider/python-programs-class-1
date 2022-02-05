student = {
    'name': 'Ravi verma',
    'mobile': 8819076632,
    'email': 'kkmadhpuriya@gmail.com',
    'pass': True
}

print(student)
student['pass'] = False
print(student)

student.update({'email': 'test@gmail.com', 'name': "Laxmi Verma"})
print(student)

student['batch'] = "CS"
print(student)

student.update({'result': 'pass', 'CGPA': "8.2"})
print(student)

fees = {
    'first sem': '60,000',
    'second sem': '60,000',
    'third sem': '61,000',
}

student['fees'] = fees
print(student)

student.pop('mobile')
print(student)

student.popitem()  # it will remove last element
print(student)

modifiedStudent = student.copy()
print(modifiedStudent)

modifiedStudent.clear()
print(modifiedStudent)

del modifiedStudent  # it will delete the object from the memory

result = ("1st", '2nd', '3rd', '4th', '5th', '6th')
marks = 0

st = student.fromkeys(result, marks)
print(st)
