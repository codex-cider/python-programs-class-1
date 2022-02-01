mobile1 = ['motorola', 'samsung', 'infinix']

mobile1.sort()
print(mobile1)

mobile1.sort(reverse=True)
print(mobile1)


mobile2 = ['Motorola', 'samsung', 'Infinix']
mobile2.sort()  # Sorting will not work -- it will sort capital letter words first then small
print(mobile2)

mobile2.sort(key=str.lower)  # for sorting capital and small words
print(mobile2)


