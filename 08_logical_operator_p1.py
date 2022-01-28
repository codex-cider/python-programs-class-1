
p10th = 80
p12th = 60

pyWorkShop = True
cgpa = 8


if p10th > 80 and p12th > 60:
    if cgpa > 8:
        print("Can join placement cell")
    elif cgpa <= 6:
        print("Try off campos")
    if (6 < cgpa <= 8) or pyWorkShop:
        print("Can join placement cell")


