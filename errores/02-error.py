# edad = 0
try:
    edad = int(input("Ingresa tu edad: "))
    print(f"Tu edad es: {edad}")
except ValueError as _ :
    print("edad incorrecta, escribe tu edad en numeros")
    
try:
    if edad <=18: 
        raise TypeError("Eres menor de edad")
except TypeError as error:
    print(error)

# palabra = "palabra"

# for i in range(len(palabra)):
#     palabra[i+1]
    
if not "texto123".isalpha():
    print("True")
else:
    print("False")





