# დადებითი და უარყოფითი რიცხვების სია
numbers = [10, -5, 20, -3, -15, 7, 0, -1]

positive_sum = 0
negative_count = 0

for num in numbers:
    if num > 0:
        positive_sum += num
    elif num < 0:
        negative_count += 1

print("დადებითი რიცხვების ჯამი:", positive_sum)
print("უარყოფითი რიცხვების რაოდენობა:", negative_count)
