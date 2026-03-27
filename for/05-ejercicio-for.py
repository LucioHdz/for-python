


# contar las vocales
contador = 0
for letra in "computadora":
    if (
        letra == "a" or 
        letra == "e" or 
        letra == "i" or 
        letra == "o" or
        letra == "u"
        ):
        contador+=1
print(contador) 







contador = 0

for letra in "computadora":
    if letra in "aeiou":
        contador += 1
print(contador)