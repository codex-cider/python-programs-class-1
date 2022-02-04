mobile1 = {'mi', 'realme', 'oppo', 'nokia', 'samsung'}

# m = mobile1  # it will assign reference
# m.remove('oppo')
#
# print(mobile1)
# print(m)

m = mobile1.copy()
m.remove('oppo')

print(mobile1)
print(m)

mobile1.add('infnix')
print(mobile1)

