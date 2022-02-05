student = {
    'name': 'Ravi verma',
    'mobile': 8819076632,
    'email': 'kkmadhpuriya@gmail.com',
    'pass': True
}

name = student['name']  # through error if key not found
print(name)

mobile = student.get('mobile')  # return None if key not found
print(mobile)

branch = student.setdefault('branch', 'You Do not have branch')
print(branch)

allKeys = student.keys()
print(allKeys)

allValues = student.values()
print(allValues)

getAllItems = student.items()
print(getAllItems)

for key in allKeys:
    print("key is -- " + key)

for value in allValues:
    print("value is -- " + str(value))

for key, value in getAllItems:
    print(key + " -- " + str(value))
# name -- Ravi Verma
# mobile -- 8819076632

for stElement in student:  # it will return key
    print(stElement)
    print(student[stElement])
    print("----------------------")

