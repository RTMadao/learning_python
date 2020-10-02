def generadorPares(limite):
    n=1

    while n<limite:
        yield n*3
        n=n+1

numeroPares = generadorPares(10) 

print(next(numeroPares))
print(next(numeroPares))
print(next(numeroPares))
print(next(numeroPares))

#al encontrar el signo * antes de un parametro se entiende que no se conoce numero de elementos a ingresar, y estos se agregaran en forma de tupla
#def generar(*ciudades): 