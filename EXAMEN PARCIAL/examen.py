#Objetivo: Evaluacioón Parcial
#Nombre: QUISPE CRISOSTOMO, Edison
#Fecha: 13/04/2025



#Menu Principal

while (True):
    Menu0 = int(input("""
    ====== MENÚ DE OPCIONES ======
    1. AUTENTICARSE
    2. REGISTRAR DONACIONES
    3. CALCULADORA
    4. REPORTE TOTAL
    5. SALIR DEL PROGRAMA
    """))

    if (Menu0 == 1):
        print("====== Bienvenido a la Autentificacion ======")
        print("Ingrese su usuario: ")
        Usuario = input()
        print("Ingrese su contraseña")
        Contraseña = input()
        if (Usuario == "Quispe" and Contraseña == "76165900"):
            print("=== Bienvenido ===")
        else:
            print("Usuario o contraseña incorrecta")
            break
        
    if (Menu0 == 1):
        Menu = int(input("""===== MENÚ DE OPCIONES =====
        2. REGISTRAR DONACIONES
        3. CALCULADORA
        4. REPORTE TOTAL
        5. SALIR DEL PROGRAMA
        """))

    

#=======================================

        if (Menu == 2):
            print("====== REGISTRAR DONACIONES ======")
            
            # Validar la sección
            Opcion = ""
            while not (Opcion == "A" or Opcion == "B" or Opcion == "C" or Opcion == "D"):
                print("Ingrese una de las siguientes opciones (A/B/C/D): ")
                Opcion = input().upper()
                if not (Opcion == "A" or Opcion == "B" or Opcion == "C" or Opcion == "D"):
                    print("Error: Ingrese una opción válida (A/B/C/D).")
            
            # Validar la cantidad de alumnos
            Cantidad = 0
            while Cantidad <= 0:
                print("Ingrese la cantidad de Alumnos: ")
                Cantidad_str = input()
                if all(c >= "0" and c <= "9" for c in Cantidad_str):  # Validar si es un número
                    Cantidad = int(Cantidad_str)
                    if Cantidad <= 0:
                        print("Error: Ingrese un número mayor a cero.")
                else:
                    print("Error: Ingrese un número válido.")
            
            # Registrar datos de cada alumno
            i = 0
            while i < Cantidad:
                print("\n=== Registro del Alumno", i + 1, "===")
                
                # Ingresar apellido paterno
                print("Ingrese el Apellido Paterno del Alumno: ")
                Apellido = input()
                
                # Validar DNI
                Dni = ""
                while len(Dni) != 8 or not all(c >= "0" and c <= "9" for c in Dni):  # Validar si es un número de 8 dígitos
                    print("Ingrese el DNI del Alumno (8 dígitos): ")
                    Dni = input()
                    if len(Dni) != 8 or not all(c >= "0" and c <= "9" for c in Dni):
                        print("Error: El DNI debe contener exactamente 8 dígitos.")
                
                print("\nRegistro completado para el alumno.\n")
                i += 1
            
                # Validar Género
                Genero = ""
                while Genero != "M" and Genero != "F":
                    print("Ingrese el Género del Alumno (M/F): ")
                    Genero = input().upper()
                    if Genero != "M" and Genero != "F":
                        print("Error: Ingrese 'M' para masculino o 'F' para femenino.")
                
                # Validar si usa lentes
                Lentes = ""
                while Lentes != "1" and Lentes != "0":
                    print("¿Usa lentes? (1=SI / 0=NO): ")
                    Lentes = input()
                    if Lentes != "1" and Lentes != "0":
                        print("Error: Ingrese '1' para Sí o '0' para No.")
                
                # Validar Edad
                Edad = 0
                while Edad < 13 or Edad > 18:
                    print("Ingrese la Edad del Alumno (13-18 años): ")
                    Edad_str = input()
                    if all(c >= "0" and c <= "9" for c in Edad_str):  # Vcon esto validar si es un número
                        Edad = int(Edad_str)
                        if Edad < 13 or Edad > 18:
                            print("Error: La edad debe estar entre 13 y 18 años.")
                    else:
                        print("Error: Ingrese un número válido.")
                
                # Validar Monto Recaudado
                Monto = 0
                while Monto <= 0:
                    print("Ingrese el Monto Recaudado del Alumno (mayor a 0): ")
                    Monto_str = input()
                    if all((c >= "0" and c <= "9") or c == "." for c in Monto_str) and Monto_str.count(".") <= 1:
                        Monto = float(Monto_str)
                        if Monto <= 0:
                            print("Error: El monto debe ser mayor a 0.")
                    else:
                        print("Error: Ingrese un número decimal válido.")
        
####################################################
    if (Menu0 == 3):
        Opcion = ""
        while Opcion not in ["A", "B", "C", "D", "E"]:
            print("""========CALCULADORA=========
                A. SUMA DE DOS NUMEROS
                B. RESTA DE DOS NUMEROS
                C. MULTIPLICACION DE DOS NUMEROS
                D. DIVISION DE DOS NUMEROS
                E. MODULO DE DOS NUMEROS
                """)
            Opcion = input().upper()
            if Opcion not in ["A", "B", "C", "D", "E"]:
                print("Error: Seleccione una opción válida.")

        num1 = 0
        while num1 <= 0:
            print("Ingrese el primer número (mayor a 0): ")
            num1_str = input()
            if all(c >= "0" and c <= "9" or c == "." for c in num1_str) and num1_str.count(".") <= 1:
                num1 = float(num1_str)
                if num1 <= 0:
                    print("Error: El número debe ser mayor a 0.")
            else:
                print("Error: Ingrese un número válido.")

        num2 = -1
        while num2 <= 0:
            print("Ingrese el segundo número (mayor a 0): ")
            num2_str = input()
            if all(c >= "0" and c <= "9" or c == "." for c in num2_str) and num2_str.count(".") <= 1:
                num2 = float(num2_str)
                if num2 <= 0:
                    print("Error: El número debe ser mayor a 0.")
            else:
                print("Error: Ingrese un número válido.")

        if Opcion == "A":  
            print("Resultado de la suma:", num1 + num2)

        elif Opcion == "B": 
            print("Resultado de la resta:", num1 - num2)

        elif Opcion == "C": 
            print("Resultado de la multiplicación:", num1 * num2)

        elif Opcion == "D": 
            while num2 == 0:  
                print("ERROR: NO SE PUEDE DIVIDIR ENTRE CERO.")
                print("Ingrese el divisor nuevamente (mayor a 0): ")
                num2_str = input()
                if all(c >= "0" and c <= "9" or c == "." for c in num2_str) and num2_str.count(".") <= 1:
                    num2 = float(num2_str)
                    if num2 <= 0:
                        print("Error: El divisor debe ser mayor a 0.")
            print("Resultado de la división:", num1 / num2)

        elif Opcion == "E":  
            print("Resultado del módulo:", num1 % num2)

######################################################

    if (Menu0 == 4):
        print("====== REPORTE TOTAL ======")

        # Inicializar contadores
        masculinos = 0
        femeninas = 0
        femeninas_lentes = 0
        masculinos_lentes = 0
        sin_lentes = 0
        menores_edad = 0
        mayores_edad = 0
        monto_total = 0
        Cantidad = 0


    if (Menu0 == 5):
        print("ESTÁ SALIENDO DE TECNICAS DE PROGRAMACION :P")
        break
    
