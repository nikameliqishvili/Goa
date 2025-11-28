#
number = int(input("შეიყვანეთ რაიმე რიცხვი: "))

if number > 0:
    if number % 2 == 0:
        print("დადებითი ლუწი")
    else:
        print("დადებითი კენტი")
else:
    print("რიცხვი უარყოფითია")
