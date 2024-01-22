print(not True )
print(not False)

print(" NOT AND")

print("True and True =>", not (True and True))
print("True and True =>", not (True and False))
print("True and True =>", not (False and True))
print("True and True =>", not (False and False))

stock =input("Ingrese el numero des tock => ")
stock = int(stock)

print(not (stock >= 100 and stock <= 1000))
