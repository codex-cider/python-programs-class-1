mobiles = ('mi', 'realme', 'nokia', 'oppo', 'samsung', 'mi')

if 'nokia' in mobiles:
    print("Nokia mobile found")


foundIndex = mobiles.index('nokia')
print(foundIndex)

# 2 is starting search index & 5 is ending search index. so nokia will be search from index 2 to 5
# foundIndex = mobiles.index('nokia', '2', '5')

counts = mobiles.count('mi')
print("Counts -- " + str(counts))
