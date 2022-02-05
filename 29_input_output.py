number = int(input("Enter Any Number "))
print(number)


firstNumber, secondNumber = input("Enter two number ").split()  # split with space
print(firstNumber)
print(secondNumber)


print('--------   SPLIT WITH SEPERATOR  -------------')
date, month, year = input("Enter date of birth in formate DD/MM/YYYY ").split("/")  # split with /
print(date)
print(month)
print(year)

print('--------   SPLIT WITH LIST COMPREHENSION  -------------')
n1, n2, n3, n4, n5 = [int(x) for x in input("Enter five numbers ").split()]
print(n1)
print(n2)
print(n3)
print(n4)
print(n5)

print(n1, n2, n3, n4, n5)
print(n1, ',', n2, ',', n3, ',', n4, ',', n5)

print(n1, n2, n3, n4, n5, sep=",")
print(n1, n2, n3, n4, n5, sep="-")


name = "test"
rank = "50"
# test@50
print(name, rank, sep="@")
print(name, end="@")
print(rank, end="------")

