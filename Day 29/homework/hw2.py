# სახელების სია პატარა ასოებით
names_lower = ["giorgi", "nino", "luka", "ana"]

# ცარიელი სია
names_upper = []

# პატარა ასოებიდან დიდ ასოებზე გადაყვანა
for i in names_lower:
    names_upper.append(i.upper())

print("პატარა ასოებით:", names_lower)
print("დიდი ასოებით:", names_upper)
