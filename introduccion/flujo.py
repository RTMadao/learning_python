def saludar(nombre):
    print(f'Hello {nombre}')
sumar = lambda numero1, numero2: numero1 + numero2

x = 60

if x < 30 or x > 50:
    print("menor")
elif x > 30 and x < 50:
    print("mayor")
else:
    print("igual")

if not(x == 30):
    print("no es igual")

foods = ['manzana','pera','banana']
for food in foods:
    print(food)

for n in range(1,11):
    print(n)

    count = 5
    validacion = True
while validacion:
    print(count)
    if count > 8:
        validacion = False
    count+=1

saludar('Carlos')
print(sumar(2,3))