# 1) 
def count_characters(text):
    return len(text)


# 2) 
def count_vowels(text):
    vowels = "აეიოუAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count


# 3)
def max_number(numbers):
    return max(numbers)


# 4) 
def words_starting_with_upper(words):
    result = []
    for word in words:
        if word[0].isupper():
            result.append(word)
    return result


# 5)
def average(numbers):
    return sum(numbers) / len(numbers)


# 6) 
def square(number):
    return number * number


# 7)
def check_number():
    num = int(input("შეიყვანე რიცხვი: "))
    if num > 0:
        return "დადებითია"
    elif num < 0:
        return "უარყოფითია"
    else:
        return "ნულია"


# 8) 
def text_and_number(text, number):
    return text.upper(), str(number)


# 9)
def even_numbers(numbers):
    evens = []
    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
    return evens


# 10)
def print_hello(count):
    for i in range(count):
        print("Hello, World")


# 11) 
def celsiusToFahrenheit(celsius):
    return (celsius * 9 / 5) + 32


# 12) 
def sumDigits(number):
    total = 0
    for i in str(abs(number)):
        total += int(i)
    return total


# 13) 
def calculateArea(length, width):
    area = length * width
    print(area)
    return area


# 14) 
def sum_in_range(start, end):
    total = 0
    for i in range(start, end + 1):
        total += i
    return total
