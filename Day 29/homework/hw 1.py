
data = ["გამარჯობა", 25, 3.14, "Python", True, "კოდი", 100]


string_count = 0

for i in data:
    if isinstance(i, str):
        string_count += 1

print("სტრინგების რაოდენობა სიაში არის:", string_count)
