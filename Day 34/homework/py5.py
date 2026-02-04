def remove_duplicates():
    original_list = [1, 2, 2, 3, 3, 4, 5, 6, 5]
    unique_list = []
    
    for item in original_list:
        if item not in unique_list:
            unique_list.append(item)
            
    print(f"სია დუბლიკატების გარეშე: {unique_list}")

remove_duplicates()