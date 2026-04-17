

#funciones
def imprimirMenu():
    print("""
    1) suma
    2) resta
    3) divison
    4) multiplicacion
    """)

def sumar(n1,n2):
    resultado = n1 + n2
    print(f"El resultado de la suma es: {resultado}")

def restar(n1,n2):
    resultado = n1-n2
    print(f"El resultado de la resta es: {resultado}")

def dividir(n1,n2):
    try:
        resultado = n1/n2
        print(f"resultado de la division es: {resultado}")
    except ZeroDivisionError:
        print("No se puede dividir entre 0")

def multiplicar(n1,n2):
    resultado = n1*n2
    print(f"resultado de la multiplicacion es: {resultado}")



#ejecucion
numero1 = 1
numero2 = 1
while True:
    try:
        numero1 = int(input("Ingresa el primer numero:"))
        numero2 = int(input("Ingresa el segundo numero:"))
        break
    except ValueError:
        print("Ingrese un numero valido")
    
imprimirMenu()
opcion = input("Ingresa una opcion: ").strip()

match opcion:
    case "1":
        sumar(numero1,numero2)
    case "2":
        restar(numero1,numero2)
    case "3":
        dividir(numero1,numero2)
    case "4":
        multiplicar(numero1,numero2)
    case _:
        print("Ingresa una opcion valida")

