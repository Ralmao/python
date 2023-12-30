#Acces program
while True:
  print("who are you")
  name =input()
  if name != "joe":
    continue
  print("Hello joe, gimme a password (its a fish)")
  password=input()
  if password == "swordfish":
    break
print("Bienvenido")