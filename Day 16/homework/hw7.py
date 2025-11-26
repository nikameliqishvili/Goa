my_password = "mypassword123"

user_input = input("შეიყვანე პაროლი: ")

while user_input != my_password:
    user_input = input("პაროლი არასწორია. შეიყვანე ისევ: ")

print("სწორია გაარტყი")
