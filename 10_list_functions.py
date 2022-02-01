mobile1 = ['MI', 'Realme', 'Oppo', 'Nokia']

mobile1.insert(1, 'vivo')

print("After insert at index first")
print(mobile1)

mobile1.pop()
print("After pop")
print(mobile1)

print("Append 'One plus'")
mobile1.append("One plus")
print(mobile1)

print("Remove element by value")
mobile1.remove('Realme')
print(mobile1)

print("pop element by index -- 2")
mobile1.pop(2)
print(mobile1)

listSize = len(mobile1)
print("List Size -- " + str(listSize))

mobile1.insert(listSize, 'new')
print(mobile1)

center = int(len(mobile1) / 2)
mobile1.insert(center,  'at center')
print(mobile1)
