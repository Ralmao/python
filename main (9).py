import random

options =("piedra", "papel", "tijera")

user_option =(input("piedra, papel o tijera => ")).lower()
computer_option = random.choice(options)

if not user_option in options:
  print("esa opcion no es valida")

print("User option =>", user_option)
print("Computer option =>", computer_option)

if user_option == computer_option:
  print("Empate!")
elif user_option == "piedra":
  if computer_option == "tijera":
    print("piedra gana a tijera")
    print("user gano!")
  else:
    print("papel gana a piedra")
    print("computer gano!")
elif user_option =="papel":
  if computer_option == "piedra":
    print("papel gana a piedra")
    print("user gano")
  else:
    print("tijera gana a papel")
    print("computer gano!")
elif user_option == "tijera":
   if computer_option == "papel":
     print("tijera gana a papel")
     print("user gano!")
   else:
    print("piedra gana a tijera")
    print("computer gano!")
     