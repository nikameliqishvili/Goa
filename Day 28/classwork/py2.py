
age_input = input("შეიყვანეთ თქვენი ასაკი: ")
age = int(age_input)


if age < 18:
    print("შენ ხარ არასრულწლოვანი")
elif 18 <= age <= 64:
    print("შენ ხარ სრულწლოვანი")
else:
    print("შენ ხარ პენსიონერი")