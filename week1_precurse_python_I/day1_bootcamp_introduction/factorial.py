def factorial(numero):
    if numero == 1:
        return 1
    return numero*factorial(numero - 1)

x = int(input())
print("El factoriál de {numero} es {factorial_numero}".format(factorial_numero = factorial(x), numero = x))
print(f"El factorial de {x} es {factorial(x)}") 
