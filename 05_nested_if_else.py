# result of student

percentage = float(input("Enter percentage: "))

if percentage > 100:
    print("Invalid")
elif percentage >= 60:
    print("First Division")
elif percentage >= 50:
    print("Second Division")
elif percentage >= 33:
    print("Third Division")
elif percentage >= 0:
    print("Fail")
else:
    print("Invalid")
