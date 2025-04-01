edad = int(input("Introduce tu edad: "))
if edad >=18: 
    print("Eres mayor de edad")
    if edad <=20:
        print("Esta pollo")
        print("en la flor dela juventud")
    elif edad > 21:
        if edad > 21 and edad <= 25:
            print("NO esta tan pollo")
        elif edad > 25 and edad < 40:
            print("ta joven, pero Ya no tanto")
        elif edad > 40:
            print("se lo llevo el puntas")


else:
    if (edad > 0):
        print("Eres menos de edad")
    else:    
        print("edad herrada")

print("Terminado")