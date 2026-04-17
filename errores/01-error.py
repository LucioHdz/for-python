
#print(10/0)
try:
    print(1 + "")

except TypeError as _:
    print("ocurrio un error")