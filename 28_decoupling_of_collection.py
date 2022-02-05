print('---------------  LIST  -------------------')
mobiles = ['mi', 'nokia', 'samsung']  # coupling
mobile1, mobile2, mobile3 = mobiles  # de-coupling

print(mobile1)
print(mobile2)
print(mobile3)

print('---------------  TUPLE  -------------------')
fruits = ('mango', 'banana', 'apple')
f1, f2, f3 = fruits

print(f1)
print(f2)
print(f3)

print('---------------  SET  -------------------')
fruits = {'mango', 'banana', 'apple'}
f1, f2, f3 = fruits

print(f1)
print(f2)
print(f3)

print('---------------  DICTIONARY  -------------------')
student = {
    'name': 'Ravi verma',
    'mobile': 8819076632,
}

st1, st2 = student
print(st1)
print(st2)

print('---------------  LIST WITH *  -------------------')
newMobiles = ['s20', 'j7', 'm31', 'realme 2 pro', 'nord 2']
*m1, m2, m3 = newMobiles
print(m1)
print(m2)
print(m3)


