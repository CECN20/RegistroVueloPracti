import funciones as fn

imc = fn.calcularImc(60,1.70)
print (imc)
fn.diagnosticoImc(imc)


opcion = 0
while (opcion != 4):
    print("\tMenu")
    print("IMC")
    print("Calcular Decuento")
    print("Calcular IVa")
    print("Salir")
    opcion = int(input("ingrese la opcion →"))
    if opcion == 1:
        peso = int(input("Ingrese su peso (masa )→"))
        estatura = int(input("ingrese su estatura (en metros)→"))
        imc = fn.calcularImc(peso,estatura)
        print (imc)
        fn.diagnosticoImc(imc)
    if opcion == 2:
        precio = int(input("Ingrese precio del producto"))
        descuento = int(input("ingrese descuento del producto→"))
        print(f"el precio final es →{fn.calculaDescuento(precio,descuento)}")
    if opcion == 3:
        precio = int(input("Ingrese precio del producto"))
        print (f"El iva es → {fn.calcularIva(precio)}")
        