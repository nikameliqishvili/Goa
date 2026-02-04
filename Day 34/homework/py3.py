def sum_even_elements():

    numbers = [10, 15, 22, 33, 40, 55, 60]
    even_sum = 0
    
    for num in numbers:
      
        if num % 2 == 0:
            even_sum += num  
            
    print(f"სიაში არსებული ლუწი რიცხვების ჯამია: {even_sum}")


sum_even_elements()