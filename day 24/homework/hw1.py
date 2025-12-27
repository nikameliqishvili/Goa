nums = [1, 6, 7, 8, 3, 12, 56, 76, 90, 345, 12, 33, 55]
print(nums[:5])
#
fruits = ["apple", "banana", "cherry", "date", "fig"]
print(fruits[-3:])
#
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(letters[3:8])
#
colors = ["red", "green", "blue", "yellow"]
print(colors[:])
#
text = "Programming"
print(text[:5])
#
word = "HelloWorld"
print(word[-5:])
#
message = "PythonRocks"
print(message[3:9])
#
phrase = "ArtificialIntelligence"
print(phrase[-12:-4])
#
fruits = ["apple", "banana", "cherry", "date"]
print(fruits[-2])
#
fruits = ["apple", "banana", "cherry", "date"]
print(fruits[-2])
#
letters = ["a", "b", "c", "d", "e", "f", "g", "o"]
word = letters[-2] + letters[-1] + letters[-2] + letters[-8]
print(word)
#
letters = ["a", "b", "c", "d", "e", "f", "g", "o"]
word = letters[-2] + letters[-1] + letters[-2] + letters[-8]
print(word)
#
names = ["Nika", "Giorgi", "Ana", "Luka", "Mari"]

print("--- For ციკლი ---")
for name in names:
    print(name)

print("\n--- While ციკლი ---")
i = 0
while i < len(names):
    print(names[i])
    i += 1