#1
numbers = []

while True:
    value = input("შეიყვანე რიცხვი (stop): ")

    if value == "stop":
        break

    num = int(value)
    if num > 0:
        numbers.append(num)

print(numbers)
#2
numbers = []

while True:
    value = input("შეიყვანე რიცხვი (stop): ")

    if value == "stop":
        break

    num = int(value)

    if num < 50:
        numbers.insert(0, num)
    else:
        numbers.append(num)

print(numbers)
#3
numbers = []
total = 0

while total <= 100:
    num = int(input("შეიყვანე რიცხვი: "))
    numbers.append(num)
    total += num

print("სია:", numbers)
print("ჯამი:", total)
#4
numbers = []

while True:
    num = int(input("შეიყვანე რიცხვი: "))

    if num in numbers:
        break
    else:
        numbers.append(num)

print(numbers)
#5
numbers = []

count = int(input("რამდენი რიცხვი შეგყავს?: "))

for i in range(count):
    num = int(input("შეიყვანე რიცხვი: "))
    numbers.append(num)

average = sum(numbers) / len(numbers)
print("საშუალო:", average)
#6
positive = []
negative = []

count = int(input("რამდენი რიცხვი შეგყავს?: "))

for i in range(count):
    num = int(input("შეიყვანე რიცხვი: "))

    if num >= 0:
        positive.append(num)
    else:
        negative.append(num)

print("დადებითი:", positive)
print("უარყოფითი:", negative)
#7
numbers = []

count = int(input("რამდენი რიცხვი შეგყავს?: "))

for i in range(count):
    num = int(input("შეიყვანე რიცხვი: "))
    numbers.append(num)

i = 0
while i < len(numbers) - 1:
    if numbers[i] + numbers[i + 1] < 50:
        numbers.pop(i + 1)
    else:
        i += 1

print(numbers)
