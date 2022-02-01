myNumbers = []
for i in range(10):
    number = int(input("Enter number "))
    myNumbers.append(number)

filteredList = [item for item in myNumbers if item < 50]
