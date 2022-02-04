
mobile1 = {'mi', 'realme', 'oppo', 'nokia', 'samsung'}
mobile2 = {'one plus', 'motorola', 'jio'}
mobile3 = {'sony', 'vivo', 'infinix', 'mi'}

# allMobile = mobile1 + mobile2  # invalid can't user + operator

allMobiles = mobile1.union(mobile2).union(mobile3)  # mi will use one time only from mobile1 & mobile3

print(mobile1)
print(allMobiles)

print("/-------------------------------------------------------------/")
print("/-------------------  UPDATE FUNCTION  -----------------------/")
print("/-------------------------------------------------------------/")
mobile3.update(mobile1)  # mobile1 ke elements mobile3 me save honge
print(mobile3)

print("/-------------------------------------------------------------/")
print("/-------------  INTERSECTION FUNCTION  -----------------------/")
print("/-------------------------------------------------------------/")
mobile4 = {'mi', 'realme', 'oppo', 'nokia', 'samsung'}
mobile5 = {'one plus', 'motorola', 'jio', 'nokia'}
x = mobile5.intersection(mobile4)
print(x)
mobile5.intersection_update(mobile4)
print(mobile5)

print("/-------------------------------------------------------------/")
print("/---------  SYMMETRIC DIFFERENCE FUNCTION  -------------------/")
print("/-------------------------------------------------------------/")
mobile6 = {'mi', 'realme', 'oppo', 'nokia', 'samsung'}
mobile7 = {'one plus', 'motorola', 'jio', 'nokia'}
x = mobile6.symmetric_difference(mobile7)
print(x)
mobile6.symmetric_difference_update(mobile7)
print(mobile6)

print("/-------------------------------------------------------------/")
print("/-------------------  DIFFERENCE FUNCTION  -------------------/")
print("/-------------------------------------------------------------/")
mobile8 = {'mi', 'realme', 'oppo', 'nokia', 'samsung'}
mobile9 = {'one plus', 'motorola', 'jio', 'nokia'}
x = mobile9.difference(mobile8)
print(x)
mobile8.difference_update(mobile9)
print(mobile8)
