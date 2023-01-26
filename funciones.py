def calcularImc(peso,estatura):
    imc = peso/(estatura*estatura)
    return(imc)

def diagnosticoImc(imc):
    if(imc < 18.5) :
        print("Bajo peso")
    if(imc >18.5 and imc <24.9):
        print("peso normal")
    if(imc >24.9 and imc <29.9):
        print("sobre peso")
    if (imc >29.9 and imc < 34.9):
        print ("obesidad I")
    if (imc >35.9 and imc < 39.9):
        print ("obesidad II")
    if (imc >40):
        print("obesidad III")

def calculaDescuento(descuento,precio):
    total_pagar = precio*(1-(descuento/100))
    return(total_pagar)    

def calcularIva (precio_final):
    precio_iva_incluido = precio_final*0.19
    return(precio_iva_incluido)