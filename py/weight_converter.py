weight = int(input("weight : "))
unit = input("(l)bs or (k)gs : ")
if unit.lower() == "l":
    converted = weight * 0.45
    print(f"you are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"you are {converted} pounds")