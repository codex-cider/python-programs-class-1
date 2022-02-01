mobile1 = ['MI', 'Realme', 'Oppo', 'Nokia']
mobile2 = ['motorola', 'samsung', 'infinix']

for item in mobile2:
    mobile1.append(item)

print(mobile1)

myNumbers = []

for i in range(10):
    number = int(input("Enter number "))
    myNumbers.append(number)

print(myNumbers)

filteredList = []

for item in myNumbers:
    if item < 50:
        filteredList.append(item)

print(filteredList)



