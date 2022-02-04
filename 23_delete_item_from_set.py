mobile1 = {'mi', 'realme', 'oppo', 'nokia', 'samsung'}

mobile1.remove('oppo')  # will through error if element not found
print(mobile1)

mobile1.discard('realme')
print(mobile1)

mobile1.pop()
print(mobile1)

mobile1.clear()  # for empty set
print(mobile1)

del mobile1  # to delete object
# print(mobile1) # will through error -- mobile1 is undefined

