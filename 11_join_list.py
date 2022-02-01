mobile1 = ['MI', 'Realme', 'Oppo', 'Nokia']
mobile2 = ['motorola', 'samsung', 'infinix']

mm = mobile1
mm[1] = 'new value'

print(mobile1)  # ['MI', 'Realme', 'Oppo', 'Nokia']
print(mm)  # ['MI', 'new value', 'Oppo', 'Nokia']

mCopy = mobile2.copy()
mCopy[1] = 'new value'
print(mobile2)  # ['motorola', 'samsung', 'infinix']
print(mCopy)  # ['motorola', 'new value', 'infinix']

# Add Two list using +
allMobiles = mobile1 + mobile2
print(allMobiles)
print(mobile1)

# Add Two list using extend
mobile1.extend(mobile2)
print(mobile1)





