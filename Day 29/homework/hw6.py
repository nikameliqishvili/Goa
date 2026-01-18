
text = input("შეიყვანე სტრინგი: ")

vowels = "აეიოუ"
vowel_count = 0
consonant_count = 0

for char in text.lower():
    if char in vowels:
        vowel_count += 1
    elif char.isalpha():  
        consonant_count += 1

print("ხმოვნების რაოდენობა:", vowel_count)
print("თანხმოვნების რაოდენობა:", consonant_count)
