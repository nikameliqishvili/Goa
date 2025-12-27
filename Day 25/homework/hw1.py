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
