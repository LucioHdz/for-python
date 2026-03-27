productoSolicitado = ""
print("""  
Menu:

No.Prod     Producto               Precio
1           Hamburguesa             $120
2           Pizza                   $150
3           Ensalada                $90
4           Refresco                $35
5           Cafe                    $25
""")


producto = int(input("Ingresa el numero de producto: "))
cantidad = int(input("Ingresa la cantidad de productos: "))

subtotal = 0
if producto == 1:
    productoSolicitado = "Hamburguesa"
    subtotal = cantidad * 120
elif producto == 2:
    productoSolicitado = "Pizza"
    subtotal = cantidad * 150
elif producto == 3:
    productoSolicitado = "Ensalada"
    subtotal = cantidad * 90
elif producto == 4:
    productoSolicitado = "Refresco"
    subtotal = cantidad * 35
elif producto == 5:
    productoSolicitado = "Cafe"
    subtotal = cantidad * 25
else:
    print("Producto no valido")

descuento = 0

if subtotal >= 500:
    descuento = subtotal * 0.10  #equivale al 10%

if producto >= 1 and producto <= 5:
    print(f"""
        Producto:      {productoSolicitado}
        Cantidad:      {cantidad}
        Subtotal:      {subtotal}
        Descuento:     {descuento}
        Total A Pagar: {subtotal-descuento}
    """)


