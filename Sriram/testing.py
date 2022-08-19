ask = input("How'd you like to mesaure yourself? CM or M :")
if ask == "CM":
    height = int(input("Enter your height in CM: "))
    height = height/100
elif ask == "M":
    height = float(input("Enter your height in M: "))

weight = int(input("Enter your weight in KG: "))
Body_mass_index = weight/(height*height)
print(Body_mass_index)
if Body_mass_index < 20:
    print("Under-weight")
elif Body_mass_index > 30:
    print("Over-weight")