#1) ერთიდან იდან ოცდაათამდე გამოიტანეთ მხოლოდ ლუწი რიცვხვები
for i in range(0,20,2):
    print(i)
for i in range(0,20):
    if i %2 == 0:
        print(i)


min = 0
while min < 20:
    if min %2 == 0:
        print(min)
    min += 1
# ხუთიდან  ოცამდე გამოიტანეთ მხოლოდ ლუწი რიცვხვები
for i in range(5,20,2):
    if i %2 == 0:
        print(i)

min = 5
while min <= 20:
    if min %2 == 0:
        print(min)
    min += 1
#1) while loop ის გამოყენებით დაბეჭდეთ თქვენი სახელი და გვარი 15ჯერ
min = 0
while min  <= 15:
    print("nika meliqishvili")
    min += 1
#4) while loop ის გამოყენებით დაბეჭდეთ რიცხვები ერთიდან 20მდე და გვერდით მიუწერეთ ამ რიცხვებს ლუწია თუ კენტი
min = 1
while min <= 20:
    min +=1
    if min %2 == 0:
       print(min,"luwia") 
    else:
        print(min,"kentia")
#5) 10 დან 20 მდე დაბეჭდეთ რიცხვები
for i in range(10,20):
    print(i)
     
min = 10
while min <= 20:
    min+=1
    print(min)
#6) 15 დან 40მდე დაბეჭდეთ რიცხვები ორის გამოკლებით, მაგალითად 15, 17, 19 ...
for i in range(15,41,2):
    print(i)
min = 15
while min <= 40:
    min += 2
    print(min)
    #3)10 დან 20 მდე გამოიტანეთ მხოლოდ ლუწი რიცხვები  forloop/while loop ორივეთი
for i in range(10,20):
        if i % 2==0:
            print(i)
min = 10
while min <= 20:
    if min %2==0:
        print(min)
    min +=1
