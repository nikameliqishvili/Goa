# ვარიანტი 1: split() ფუნქციით
def count_long_words_split():
    sentence = input("შემოიტანეთ წინადადება: ")
    words = sentence.split()
    count = 0
    for word in words:
        if len(word) > 4:
            count += 1
    print(f"4-ზე მეტი სიგრძის სიტყვების რაოდენობა: {count}")

# ვარიანტი 2: split() ფუნქციის გარეშე
def count_long_words_no_split():
    sentence = input("შემოიტანეთ წინადადება: ")
    count = 0
    current_length = 0
    

    for char in sentence + " ":
        if char != " ":
            current_length += 1
        else:
            if current_length > 4:
                count += 1
            current_length = 0
    print(f"4-ზე მეტი სიგრძის სიტყვების რაოდენობა (ხელით): {count}")

count_long_words_split()
count_long_words_no_split()