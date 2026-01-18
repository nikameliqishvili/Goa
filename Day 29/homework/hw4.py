
words = ["python", "code", "programming", "ai", "developer", "web"]


new_words = []

for i in words:
    if len(i) > 5:
      
        new_words.append(i.capitalize())
    else:
        
        new_words.append(i.upper())

print("ძველი სია:", words)
print("ახალი სია:", new_words)
