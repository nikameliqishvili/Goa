#1)შექმენით სახელებით სავსე სია, თუ სიტყვის ყველა ასო არის პატარა და პირველი ასო არის d, მაშინ ახალ სიაში ჩაამატეთ სახელი "NIKA", თუ სიტყვის ყველა ასო არის დიდი ან იწყება ასო K-თი, მაშინ სიაში ჩაამატეთ სახელი "GOGA", სხვა შემთხვევაში სიაში ჩაამატეთ სიტყვა.
# საწყისი სია სახელებით
names = ["davit", "DATO", "kaxa", "Keti", "dato", "Luka"]

new_list = []

for name in names:

    if name.islower() and word.startswith("d"):
        new_list.append("NIKA")

    elif name.isupper() or word.startswith("K"):
        new_list.append("GOGA")

    else:
        new_list.append("ლიდერი")

print(new_list)
#2)შექმენით სიტყვებით სავსე სია, თუ სიტყვის ყველა ასო არის პატარა, ანუ წერია lowercase-ში, ამ სიტყვის ყველა ასო გახადეთ დიდი.
#თუ სიტყვა შეიცავს თუნდაც ერთ uppercase ასოს, ეს სიტყვა ამოშალეთ სიიდან. ბოლოს დაპრინტეთ მიღებული სია. (არ შექმნათ ახალი სია, იმუშავეთ იგივე სიტყვების სიაში) გამოიყენეთ while ციკლი.
# საწყისი სია
words = ["hello", "World", "python", "Code", "java", "c++"]

i = 0
while i < len(words):

    if not words[i].islower():
        words.pop(i)   
    else:
   
        words[i] = words[i].upper()
        i += 1 

print(words)
#3) შექმენით ქვეყნების სია, წაშალეთ pop() ან remove() ფუნქციით ყველა ის სიტყვა რომლის ყველა ასო არის დიდი, ხოლო ყველა სხვა სიტყვას ყველა ასო გაუხადეთ დიდი. დაპრინტეთ საბოლოო შედეგი. გამოიყენეთ while ციკლი
# ქვეყნების სია
countries = ["GEORGIA", "france", "Italy", "SPAIN", "germany", "Usa"]

i = 0
while i < len(countries):

    if countries[i].isupper():
        countries.pop(i)
    else:
      
        countries[i] = countries[i].upper()
        i += 1

print(countries)
#4) შექმენით სტრინგის ცვლადი და ცარიელი სია. სტრინგში მყოფი დიდი ასოები გახადეთ პატარა და ამ სიაში ჩაამატეთ, ხოლო სტრინგში მყოფი პატარა ასოები გახადეთ დიდი და ასევე ჩააგდეთ ამ სიაში. დაპრინტეთ საბოლოო სია, გამოიყენეთ while ციკლი.
# სტრინგის ცვლადი
text = "PyThOnIsFuN"


result = []

i = 0
while i < len(text):

    if text[i].isupper():
        result.append(text[i].lower())

    else:
        result.append(text[i].upper())
    i += 1


print(result)
#5) შექმენით სტრინგის ცვლადი და ცარიელი სია, თუ სტრინგის ასო არის პატარა, მაშინ ცარიელ სიაში ჩაამატეთ "%" ნიშანი, ხოლო თუ სტრინგის ასო არის დიდი, მაშინ ცარიელ სიაში ჩაამატეთ "@" ნიშანი. თუ მინუსების რაოდენობა სიაში არის ლუწი, მაშინ წაშალე ყველა "%" ნიშანი, ხოლო თუ მინუსების რაოდენობა სიაში არის კენტი, წაშალე ყველა "@" ნიშანი. "%" და "@" -ების თავიდან სიაში ჩასაგდებად გამოიყენეთ for ციკლი, ხოლო "%" ან "@" -ების წასაშლელად გამოიყენეთ while ციკლი.
# სტრინგის ცვლადი
text = "PyThOn"


symbols = []


for char in text:
    if char.islower():
        symbols.append("%")
    elif char.isupper():
        symbols.append("@")


if len(symbols) % 2 == 0:
    i = 0
    while i < len(symbols):
        if symbols[i] == "%":
            symbols.pop(i)
        else:
            i += 1

else:
    i = 0
    while i < len(symbols):
        if symbols[i] == "@":
            symbols.pop(i)
        else:
            i += 1


print(symbols)
#6) შექმენით სტრინგებით სავსე სია, წაშალეთ ის სტრინგ მონაცემთა ტიპის ელემენტები რომლებიც არიან 5-ზე მეტი სიგრძეში ან დგანან კენტ ინდექსზე. გამოიყენეთ remove() ფუნქცია.
# სტრინგების სია
words = ["cat", "elephant", "dog", "python", "sun", "notebook", "sky"]

i = 0
while i < len(words):
    
    if len(words[i]) > 5 or i % 2 == 1:
        words.remove(words[i])  
        i += 1  

print(words)
