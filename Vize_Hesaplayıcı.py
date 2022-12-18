a = float(input("1.Vize Notu:"))
b = float(input("2.Vize Notu:"))
c = float(input("Final Notu:"))

genelno = a * 3/10 + b * 30/100 + c * 40/100



if genelno >= 90:
    print("AA")
elif genelno  >= 85:
    print("BA")
elif genelno >= 80:
    print("BB")
elif genelno >= 75:
    print("CB")
elif genelno >= 70:
    print("CC")
elif genelno >= 65:
    print("DC")
elif genelno >= 60:
    print("DD")
elif genelno >= 55:
    print("FD")
elif genelno < 50:
    print("FF")

print("Not Ortalamanız : {}".format(genelno))



