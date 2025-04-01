import os
os.system('cls' if os.name == 'nt' else 'clear')
Estudiantes=[]
banderaPrincipal  =True
while banderaPrincipal:
   print("__________________________________________________________")
   print("                 MENU PRINCIPAL")
   print("__________________________________________________________")
   print("1. Agregar nuevos estudiantes")
   print("2. Mostrar estudiantes con promedio mayor a un valor dado")
   print("3. Buscar estudiantes por nombre")
   print("4. Salir del programa")
   opcion=input("Digite Opción")
   if (opcion=="4"):  #Salir
       banderaPrincipal=False
       break
   Notas={"N1": 0,"N2":0,"N3":0,"N4":0}
   if (opcion=="1"): # Entrada de estudiantes
      bandera =True
      while bandera:
         nombre= input("Entra Nombre Estudiante: ")
         edad= int(input("Entra Edad Estudiante: "))
         Notas["N1"]= float(input("Entra calificacion N1 Estudiante: "))
         Notas["N2"]= float(input("Entra calificacion N2 Estudiante: "))
         Notas["N3"]= float(input("Entra calificacion N3 Estudiante: "))
         Notas["N4"]= float(input("Entra calificacion N4 Estudiante: "))
         Promedio = sum(Notas.values())/4
        
         Estudiantes.append({"Nombre":nombre,"Edad":edad,"Calificaciones":Notas, "Promedio":Promedio })
         print(nombre, ' promedio notas ',Promedio)
         input("-----<digite una tecla para continuar>------------")
         opcion =input("Deseas Continuar ingresando alumnos S/N?")
         if opcion.upper()=="N":
            bandera=False
   elif (opcion == "2"): # informe estudiantes mayor el promedio
      print('Informe estudiantes con promedio mayor a un valor dado')
      print('------------------------------------------------------')
      promediobase = float(input("Digite el promedio base del informe: "))
      print("---------Buscando e informando estudiantes mayores al promedio'")
      for estudiante in Estudiantes:
         if estudiante["Promedio"]  >  promediobase:
               print(estudiante["Nombre"]," - Calificación Promedio ",estudiante["Promedio"])
      print('-----------------------fin informe---------------------')
   elif (opcion == "3"):
      print('Busqueda de estudiantes por Nombre--------------------')
      print('------------------------------------------------------')
      NomEstudiante = input("Digite el nombre del estudiante: ").upper()
      for estudiante in Estudiantes:
         if NomEstudiante in estudiante["Nombre"].upper() :
               print(estudiante["Nombre"]," Encontrado")
      print('-----------------------fin informe---------------------')
              





