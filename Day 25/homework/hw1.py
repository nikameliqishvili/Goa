#1
names = ["nika", "luka", "giorgi"]

index = int(input("შეიყვანე ინდექსი: "))
name = input("შეიყვანე სახელი: ")

names.insert(index, name)
print(names)
#2
fruits = ["apple", "banana", "apple", "orange"]

fruit = input("შეიყვანე ხილი: ")

if fruit in fruits:
    fruits.remove(fruit)
    print(fruits)
else:
    print("ეს ხილი ლისტში არ არის")
#3
nums = [1, 2, 3, 2, 4, 2, 5]

num = int(input("შეიყვანე რიცხვი: "))
count = nums.count(num)

print(count)
#4
colors = ["red", "blue", "green", "yellow"]

color = input("შეიყვანე ფერი: ")

if color in colors:
    print(colors.index(color))
else:
    print("Not found")
#5
my_list = [1, 2, 3, 4, 5]

answer = input("გინდა list-ის გასუფთავება? (yes/no): ")

if answer == "yes":
    my_list.clear()

print(my_list)
#6
numbers = []

for i in range(5):
    num = int(input("შეიყვანე რიცხვი: "))
    numbers.append(num)

total = 0
for n in numbers:
    total += n

print("ჯამი:", total)
#7
letters = ["a", "b", "c", "d", "e"]

index = int(input("შეიყვანე ინდექსი: "))

removed = letters.pop(index)

print("წაშლილი ელემენტი:", removed)
print("ლისტი:", letters)
#8
animals = ["dog", "cat", "horse", "cow"]

animal = input("შეიყვანე ცხოველი: ")

if animal in animals:
    print(animals.index(animal))
else:
    print("Animal not found")
#9
nums = [1, 2, 3, 4]

index = int(input("შეიყვანე ინდექსი: "))
num = int(input("შეიყვანე რიცხვი: "))

if index < len(nums):
    nums.insert(index, num)
else:
    nums.append(num)

print(nums)
#10
tasks = ["homework", "clean room", "exercise"]

answer = input("Are you sure you want to delete all tasks? (yes/no): ")

if answer == "yes":
    tasks.clear()

print(tasks)
#11
numbers = []

while True:
    value = input("შეიყვანე რიცხვი (ან stop): ")

    if value == "stop":
        break

    numbers.append(int(value))

print(numbers)
