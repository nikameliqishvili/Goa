def even_count():
    n = int(input("შეიყვანე მთელი რიცხვი n: "))
    count = 0

    for i in range(1, n + 1):
        if i % 2 == 0:
            count += 1

    print("ლუწი რიცხვების რაოდენობაა:", count)

even_count()
