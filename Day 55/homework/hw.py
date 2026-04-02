def solution(number):
    if number < 0:
        return 0
    
    total = 0
    
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    
    return total
##################################################################
def check_exam(arr1, arr2):
    score = 0
    
    for correct, answer in zip(arr1, arr2):
        if answer == "":
            score += 0
        elif answer == correct:
            score += 4
        else:
            score -= 1
    
    return max(score, 0)
#####################################################################
def high_and_low(numbers):
    # 1. Split the string into a list of strings and convert them to integers
    nums = [int(n) for n in numbers.split()]
    
    # 2. Find the max and min, then format them into a string
    return f"{max(nums)} {min(nums)}"
#######################################################################
def find_short(s):
    return len(min(s.split(), key=len))
#######################################################################
def remove(st):

    stripped_st = st.rstrip('!')

    trailing_marks = '!' * (len(st) - len(stripped_st))
    
    return stripped_st.replace('!', '') + trailing_marks
#########################################################################
def remove(st):

    words = st.split(" ")

    cleaned_words = [word.rstrip("!") for word in words]
    

    return " ".join(cleaned_words)
###########################################################################
def points(games):
    total_points = 0
    
    for game in games:
        # Split the string "x:y" into two variables
        # strings like "3:1" become x="3" and y="1"
        x, y = game.split(":")
        
        # Compare scores (convert to int first)
        if x > y:
            total_points += 3
        elif x == y:
            total_points += 1
            
    return total_points