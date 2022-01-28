# Create a list
listData = ["item 1", "item 2", "item 3", 'item 4', 50, 30.5, True]

# print list item at index 3
print(listData[3])

# Another way of creating of list ( by using constructor )
listData2 = list(["item 1", "item 2", "item 3", 'item 4', 50, 30.5, True])

# print list item at index 4
print(listData2[4])

# print list item from 1 to 5
print(listData2[1:5])

# print list item from start to 5
print(listData2[:5])

# print list item from 2 to end
print(listData2[2:])

# start counting of item from end
print(listData2[-4:-2])

# invalid
print(listData2[-4:1])


fruits = ['apple', 'banana', 'mango', 'grapes', 'coconut']

# update item at index 2
print(fruits)
fruits[2] = 'watermelon'  # update using index
print(fruits)

fruits.insert(2, 'strawberry')  # update using function
print(fruits)

# find item in list
if 'grapes' in fruits:
    print("Grapes is present in list")

print('mango' in fruits)

