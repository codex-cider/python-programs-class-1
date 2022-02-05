# ordered, changeable

student = {
    'name': 'Ravi verma',  # name value pair Or key value pair -- name/key = name, value = Ravi Verma
    'mobile': 8819076632,  # name value pair Or key value pair -- name/key = mobile, value = 8819076632
    'email': 'kkmadhpuriya@gmail.com',  # name value pair Or key value pair -- name/key = email, value = kkmadhpuriya@gmail.com
    'pass': True
}

print(student['name'])  # access value by name/key
print(student['mobile'])  # access value by name/key

isHaveBranch = 'branch' in student
print(isHaveBranch)

isHaveMobile = 'mobile' in student
print(isHaveMobile)
