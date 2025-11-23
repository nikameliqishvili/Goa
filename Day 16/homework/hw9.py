num1 = float(input("შეიყვანე პირველი რიცხვი: "))
num2 = float(input("შეიყვანე მეორე რიცხვი: "))
op = input("შეიყვანე ოპერატორი (+, -, *, /, **, %, //, >, <, >=, <=, ==, !=): ")

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
elif op == "**":
    print(num1 ** num2)
elif op == "%":
    print(num1 % num2)
elif op == "//":
    print(num1 // num2)
elif op == ">":
    print(num1 > num2)
elif op == "<":
    print(num1 < num2)
elif op == ">=":
    print(num1 >= num2)
elif op == "<=":
    print(num1 <= num2)
elif op == "==":
    print(num1 == num2)
elif op == "!=":
    print(num1 != num2)
else:
    print("არასწორი ოპერატორი")
