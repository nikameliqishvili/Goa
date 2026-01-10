#1
sentence = input("შეიყვანე წინადადება: ")

words = sentence.split()
for word in words:
    print(word.capitalize())
#2
word = input("შეიყვანე სიტყვა: ")

print(word.upper())
print(word.lower())
print(word.capitalize())
#3
password = input("შეიყვანე პაროლი: ")

while len(password) < 8:
    print("პაროლი სუსტია")
    password = input("შეიყვანე უფრო ძლიერი პაროლი: ")

print("პაროლი საკმარისად ძლიერია")
#4
total = 0
for i in range(5):
    num = int(input("შეიყვანე რიცხვი: "))
    total += num

print("ჯამი:", total)
#
total = 0
count = 0

while count < 5:
    num = int(input("შეიყვანე რიცხვი: "))
    total += num
    count += 1

print("ჯამი:", total)
#5
total = 0

while True:
    num = int(input("შეიყვანე რიცხვი (0 დასასრული): "))
    
    if num == 0:
        break

    if num > 0:
        print("დადებითია")
    else:
        print("უარყოფითია")

    total += num

print("რიცხვების ჯამი:", total)
#6
minor = 0
adult = 0
pensioner = 0

while True:
    age = int(input("შეიყვანე ასაკი (-1 დასასრული): "))
    
    if age == -1:
        break
    elif age < 18:
        minor += 1
    elif age < 65:
        adult += 1
    else:
        pensioner += 1

print("არასრულწლოვანი:", minor)
print("სრულწლოვანი:", adult)
print("პენსიონერი:", pensioner)
#7
num = int(input("შეიყვანე რიცხვი (1-5): "))

if num == 1:
    print("One")
elif num == 2:
    print("Two")
elif num == 3:
    print("Three")
elif num == 4:
    print("Four")
elif num == 5:
    print("Five")
else:
    print("არასწორი რიცხვი")
#8
total = 0
count = 0

while count < 5:
    num = int(input("შეიყვანე რიცხვი: "))
    total += num
    count += 1

average = total / 5
print("საშუალო:", average)

if average > 50:
    print("დიდი საშუალო")
else:
    print("პატარა საშუალო")
