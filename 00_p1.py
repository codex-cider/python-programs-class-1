student = {
    "name": "priyanshu shukla",
    "mobile": 6265915578,
    "email": "priyanshushukla@gmail.com",
    "dateOfBirth": "17/12/2001",
    "SGPA": [9.2, 8.9, 9.0, 0, 0, 0, 0, 0],
    "CGPA": [9.2, 9.0, 8.9, 0, 0, 0, 0, 0]
}

for key, value in student.items():
    # print(key, "--", value)
    # print("{} --&&-- {}".format(key, value))
    print(f"{key}:   {value}")
    # print(f"Type of {key} -- {type(value)}")
    if(key == "SGPA"):
        sem = 1
        for sgpa in value:
            print(f"{sem} sem -- {sgpa}")
            sem = sem + 1
    if (key == "CGPA"):
        sem = 1
        for cgps in value:
            print(f"{sem} sem -- {cgps}")
            sem = sem + 1
