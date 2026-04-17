
nombre=""
edad=""
password=""

while True:
    try:
    #Nombre (solo letras, no vacio)
    # ""   o "     Hola mundo    "          "Hola mundo"
        nombre = input("Ingresa tu nombre: ").strip()
        if nombre == "":
            raise ValueError("No puedes colocar un nombre vacio")
        if not nombre.isalpha():
            raise ValueError("Nombre no puede contener numeros")
        break
    except ValueError as error:
        print(error)


#Edad( entre 0 y 120)
while True:
    try:
        edad = int(input("Ingresa tu edad: "))
        if edad <0 :
            raise IndexError("La edad no puede ser menor a 0")
        elif edad > 120:
            raise IndexError("La edad no puede ser mayor a 120")
        else: 
            break
    except IndexError as error:
        print(error)
    except ValueError:
        print("Ingresa la edad en numeros")


#contraseña (minimo 8 caracteres)
while True:
    try:
        password = input("Ingresa la contraseña: ").strip()
        if len(password)>= 8:
            break
        raise ValueError("La contraseña debe de ser de 8 caracteres o mas")

    except ValueError as error:
        print(error)




print(f"nombre: {nombre}")
print(f"edad: {edad}")
print(f"contraseña: {password}")