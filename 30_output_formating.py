print("Hi this is print")

# print("Hi i obtain marks " + 20 + "in math")  # print error because 20 is integer and can't be add with string
print("Hi i obtain marks", 20, "in math")

fruits = {"apple", "banana", "mango"}
# if we don't provide sep then it will use space
print("Fruits are", fruits, "total number is", len(fruits), sep=" -- ")

print("a = %d & b is %.2f" % (20, 20.5562))  # %d is for integer & %f for float
print("a = %d & b is %.3f" % (20, 20.5562))  # print floating number up-tp 3 decimal (%.3f)
print("a = %d & b is %f" % (20, 20.55627878456466))  # default up-to decimal is 6
print("a = %.5d & b is %.3f" % (250, 20.5562))  # print integer with 5 digits (%.5d)

# print number without adding any zeroes before if number after . is less than total digits of printing integer
# value of after . is 1 & printing dgit is 290
print("a = %.1d & b is %.3f" % (290, 20.5562))

# print space before inputs
print("a=%20d & b=%30.2f" % (30, 120.5))
# here %20d will print 20 spaces and then d -- (30)
# & %30.2f will print 30 space and .2f -- (120.50)

# Print octane number
print("Octane value of 20 is %o" % 20)

# print hex value
print("Hex value of 13 is %X" % 13)  # can use X or x

# print exponential value
print("%.3E" % 15845.301254)
print("%.2E" % 15845.301254)
print("%.7E" % 15845.301254)
print("%20.5E" % 15845.301254)

# Print with formate function
print("a = {} & b = {}".format(20, 30.5))
print("marks is {1} & name is {0}".format("Ravi Verma", 50))

# print("marks is {2} & name is {0}".format("Ravi Verma", 50))  # have an error because formate have only 2 element

print("Hindi marks is {hindi} & English marks is {english} total is {total}".format(english=30, total=75, hindi=45))
print("Hindi marks is {hindi} & English marks is {english} total is {0}".format(75, english=30, hindi=45))

