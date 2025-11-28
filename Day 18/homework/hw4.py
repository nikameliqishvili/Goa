#
age = int(input("შეიყვანეთ თქვენი ასაკი: "))

if age >= 18:
    if age >= 60:
        print("პენსიონერი")
    else:
        print("ზრდასრული")
else:
    print("ბავშვი ხარ")

