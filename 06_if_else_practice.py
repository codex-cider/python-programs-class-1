
a = int(input("Enter Any Number"))

if a > 50:
    if a % 2 == 0:
        print("Hi")
    else:
        if a % 13 == 0:
            print("Loop End")
        else:
            print("Hi")
else:
    print("Test")
    if a % 7 == 0:
        print("You Have 50% chances to win")
    else:
        print("LOOP END")

