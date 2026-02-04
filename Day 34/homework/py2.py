def find_max_element():
    numbers = [12, 45, 7, 89, 23, 56, 10]
    if not numbers:
        return

    max_val = numbers[0] 
    for num in numbers:
        if num > max_val:
            max_val = num
    
    print(f"სიის უდიდესი ელემენტია: {max_val}")


find_max_element()