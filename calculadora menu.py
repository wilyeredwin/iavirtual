
def calculadora (a,b,calculo):
    resultado=0
    if calculo=="1":
        resultado=a+b
    elif calculo=="2":
        resultado=a-b
    elif calculo=="3":
        resultado=a*3
    elif calculo=="4":
        if b!=0:
            resultado=a/b
        else:
            print("División inválida")
    print(resultado)
a=int(input("Digite el primer número: "))
b=int(input("Digite el segundo número: "))
bandera = True
while bandera:
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    calculo=(input("Seleccione la operación a realizar: "))
    if calculo=="5":
        break
    else:
        calculadora(a,b,calculo)