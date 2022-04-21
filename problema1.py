# Problema 1.2

En una reuniion asistieron **n** personas, ¿Cuantos saludos de mano (puños) hubieron?

a = n * (n-1)/2

Solucion

definicion de variables: n: numero de personas s: numero de saludos

se sabe que cada persona debe saludar a las (n-1) restantes, por lo que habra n * (n-1) saludos, como cada saludo intervienen 2 personas, la cantidad de saludos de mano sera:

s = n * (n-1)/2

Diagrama N/S

    Declarar variables
    leer n
    s = n * (n-1)/2
    imprimir s


n: int
s: int

n = int(input("ingrese la cantidad de personas: "))


s = n * (n-1)/2

print(s)


