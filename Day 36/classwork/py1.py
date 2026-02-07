def sum_numbers(numbers):
    total = 0
    for n in numbers:
        total += n
    return total


nums = [10, 20, 30, 100, 200, 500]
result = sum_numbers(nums)
print(result)
