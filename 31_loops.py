
# for element in ( any array/collection )  # syntax of for


myList = ["20", "5632", "986544"]

for item in myList:
    print(item)


for i in range(10):   # [0,1,2,3,4,5,6,7,8,9] --> rang(10) --> 10 is last index
    print(i, end=", ")

print("\n")
for i in range(1, 10):   # [0,1,2,3,4,5,6,7,8,9] --> rang(1, 11) --> 1 is starting index and 11 is last index
    print(i, end=", ")

print("\n")
# 2 * 1 = 2
# 2 * 2 = 4

table = 2
for i in range(1, 11):
    print(f"{table} * {i} = {table*i}")

for i in range(10):
    for j in range(10):
        print(i, j)


MPCollages = {
    'indore': ["indore Collage 1", "indore Collage 2", "indore Collage 3"],
    'ujjain': ["ujjain Collage 1", "ujjain Collage 2", "ujjain Collage 3"]
}

for city in MPCollages:
    print("---  Collages in ", city)
    for collage in MPCollages[city]:
        print("Collage name is ", collage)
