mobiles = ('mi', 'realme', 'nokia', 'oppo', 'samsung')  # packing

(mobile1, mobile2, mobile3, mobile4, mobile5) = mobiles  # unpacking
print(mobile1)


# if element less than tuple length ( note: can not user more than one star )
(m1, *m2, m3) = mobiles  # m2 print list
print(m2)
