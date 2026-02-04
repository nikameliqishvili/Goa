def find_longest_word():
    sentence = input("შემოიტანეთ წინადადება: ")
    words = sentence.split()
    
    longest_word = ""
    index = 0
    
    while index < len(words):
        if len(words[index]) > len(longest_word):
            longest_word = words[index]
        index += 1
        
    print(f"ყველაზე გრძელი სიტყვაა: {longest_word}")

find_longest_word()