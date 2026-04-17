estado = "S"
while estado.upper() == "S":

    opcion = input("""
    =============Menu =============
    Que deseas hacer?
    a) incrementar
    b) decrementar
    
    Elige una opcion: """).lower()

    if opcion == "a":
        inicio = int(input("Ingresa el primer numero: "))
        fin = int(input("Ingresa el ultimo numero: "))

        if inicio < fin:
            for i in range(inicio, fin + 1):
                print(f"{i} ", end="")
            print()

    elif opcion == "b":
        inicio = int(input("Ingresa el primer numero: "))
        fin = int(input("Ingresa el ultimo numero: "))

        if inicio > fin:
            for i in range(inicio, fin - 1, -1):
                print(f"{i} ", end="")
            print()

    else:
        print("Ingresa una respuesta valida")
        continue

    estado = input("deseas continuar (S/N): ")
