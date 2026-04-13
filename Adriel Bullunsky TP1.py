""""
Ejercicio 1 --- "Caja de Kiosco"
"""
"""

nombre = input("Por favor, ingrese el nombre del cliente: ")

while not nombre.isalpha() or nombre == "":
    print(" Error: El nombre solo debe contener letras y no estar vacio")
    nombre = input("Por favor, ingrese el nombre del cliente: ").strip()    



productos_str = input("Por favor, ingrese la cantidad de productos: ").strip()

while not productos_str.isdigit() or int(productos_str) == 0:
    print("Error: Ingrese un numero entero positivo mayor a 0.")
    productos_str = input("Por favor, ingrese la cantidad de productos: ").strip()

cantidad_productos_int = int(productos_str)

total_con_descuento = 0
total_sin_descuento = 0

for i in range (1, cantidad_productos_int + 1):
    precio_str = input(f"producto {i} - precio: ").strip()

    while not precio_str.isdigit() or int(precio_str) == 0:
        print("Error,por favor ingrese un numero entero.")
        precio_str = input(f"producto {i} - precio: ")

    valor_int = int(precio_str)

    descuento = input("¿El producto tiene descuento? (S/N): ").strip().lower()

    while descuento != 's' and descuento != 'n':
        print("Error, por favor ingrese 's' para si o 'n' para no.")
        descuento = input("¿El producto tiene descuento? (S/N): ").strip().lower()

    total_sin_descuento += valor_int

    if descuento == 's':
        precio_final = valor_int * 0.90

    else:
        precio_final = valor_int

    total_con_descuento += precio_final

ahorro = total_sin_descuento - total_con_descuento
promedio_por_producto = total_con_descuento / cantidad_productos_int

print(f"El total sin descuento es: ${total_sin_descuento}")
print(f"El total con descuento es: ${total_con_descuento:.2f}")
print(f"El ahorro es de: ${ahorro:.2f}")
print(f"El promedio por producto es: ${promedio_por_producto:.2f}")

"""

"""
Ejercicio 2 --- "Acceso al Campus y menú seguro"

"""

"""
INGRESO_DE_NOMBRE = "alumno"
INGRESO_DE_CONTRASEÑA = "python123"
INTENTOS_MAX = 3
acceso_concedido = False
acceso_concedido = True

nombre = input("Por favor, ingrese el nombre: ")
contraseña = input("Por favor, ingrese la contraseña: ")
intento = 1

while not (nombre == INGRESO_DE_NOMBRE and contraseña == INGRESO_DE_CONTRASEÑA) and intento < INTENTOS_MAX:
    print("ERROR, CREDENCIALES INVALIDAS")
    nombre = input("Por favor, ingrese el nombre: ")
    contraseña = input("Por favor, ingrese la contraseña: ")
    intento += 1 

if nombre == INGRESO_DE_NOMBRE and contraseña == INGRESO_DE_CONTRASEÑA:
    print("Acceso concedido")

else:
    print("Cuenta bloqueda")


if not acceso_concedido:
    print("Cuenta bloqueada")
else:
    
    while True:
        print("\n1) Estado 2) Cambiar clave 3) Mensaje 4) Salir")
        opcion = input("Opción: ")


        if not opcion.isdigit(): 
            print("Error: ingrese un número válido.")
            continue 
            
        opcion = int(opcion) 
        
        if opcion < 1 or opcion > 4:
            print("Error: opción fuera de rango")
        elif opcion == 1:
            print("Inscripto")
        elif opcion == 2:
        
            nueva_clave = input("Nueva clave: ")
            if len(nueva_clave) < 6: 
                print("Error: mínimo 6 caracteres")
            else:
                confirmacion = input("Confirme su nueva clave: ")
                if nueva_clave == confirmacion:
                    clave_correcta = nueva_clave
                    print("Clave cambiada con éxito.")
                else:
                    print("Error: las claves no coinciden.")
        elif opcion == 3:
            print("Un gran poder conlleva una gran responsabilidad.")
        elif opcion == 4:
            print("Saliendo del sistema...")
            break 

"""

"""
Ejercicio 3 ---- "Agenda de turnos con nombres".


l1 = ""
l2 = ""
l3 = ""
l4 = ""
m1 = ""
m2 = ""
m3 = ""

operador = input("Por favor, ingrese el nombre del operador: ")
while not operador.isalpha():
    print("Error: Por favor, el nombre debe contener solo letras.")
    operador = input("Por favor, ingrese el nombre del operador: ")

while True:
    print("\n AGENDA DE TURNOS")
    print("1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del dia")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")
    
    opcion = input("Por favor, elija una opcion: ")

    if not opcion.isdigit():
        print("Error: Por favor, la opcion debe contener solo numeros.")
        continue
     
    if opcion == "1":
    
        dia = input("Elegir dia (1=Lunes, 2=Martes): ")
        if dia == "1" or dia == "2":
            paciente = input("Por favor, ingrese el nombre del paciente: ")
            if paciente.isalpha():

                repetido = False
                if dia == "1":
                    if paciente == l1 or paciente == l2 or paciente == l3 or paciente == l4:
                       repetido = True
                else:
                    if paciente == m1 or paciente == m2 or paciente == m3:
                       repetido = True
                
                if repetido:
                     print("Error: Por favor, ya ha sido otorgado el turno para este dia.")
                else:
                    if dia == "1":
                        if l1 == "": l1 = paciente
                        elif l2 == "": l2 = paciente
                        elif l3 == "": l3 = paciente
                        elif l4 == "": l4 = paciente
                        else: print("Todos los turnos para el Lunes han sido reservados.")
                    else:
                        if m1 == "": m1 = paciente
                        elif m2 == "": m2 = paciente
                        elif m3 == "": m3 = paciente
                        else: print("Todos los turnos para el Martes han sido reservados.")
            else:
               print("Error: El nombre ya fue cargado.")       
        else:
          print("Error, el dia seleccionado no corresponde.")

    elif opcion == "2":
        dia = input("por favor, ingrese el dia que quisiera cancelar(1=Lunes, 2=Martes): ")
        nombre_paciente = input("Por favor, ingrese el nombre del paciente para sacarlo de la lista: ")

        if dia =="1":
            if l1 == nombre_paciente: l1 = ""
            elif l2 == nombre_paciente: l2 = ""
            elif l3 == nombre_paciente: l3 = ""
            elif l4 == nombre_paciente: l4 = ""
            else: print("Disculpe, el paciente no se encuentra.")
        elif dia == "2":
            if m1 == nombre_paciente: m1 = ""
            elif m2 == nombre_paciente: m2 = ""
            elif m3 == nombre_paciente: m3 = ""
            else: print("Disculpe, el paciente no se encuentra.")

    elif opcion == "3":
        dia = input("Ver agenda de (1=Lunes, 2=Martes): ") 
        if dia == "1":
            print("Turno 1:", l1 if l1 != "" else "(libre)")
            print("Turno 2:", l2 if l2 != "" else "(libre)")
            print("Turno 3:", l3 if l3 != "" else "(libre)")
            print("Turno 4:", l4 if l4 != "" else "(libre)")
        elif dia == "2":
            print("Turno 1:", m1 if m1 != "" else "(libre)")
            print("Turno 2:", m2 if m2 != "" else "(libre)")
            print("Turno 3:", m3 if m3 != "" else "(libre)")

    elif opcion == "4":
    
        ocupados_lunes = 0
        if l1 != "": ocupados_lunes += 1
        if l2 != "": ocupados_lunes += 1
        if l3 != "": ocupados_lunes += 1
        if l4 != "": ocupados_lunes += 1
        
        ocupados_martes = 0
        if m1 != "": ocupados_martes += 1
        if m2 != "": ocupados_martes += 1
        if m3 != "": ocupados_martes += 1
        
        print(f"Lunes: Ocupados {ocupados_lunes}, Libres {4 - ocupados_lunes}")
        print(f"Martes: Ocupados {ocupados_martes}, Libres {3 - ocupados_martes}")
        
        if ocupados_lunes > ocupados_martes:
            print("Día con más turnos: Lunes")
        elif ocupados_martes > ocupados_lunes:
            print("Día con más turnos: Martes")
        else:
            print("Disculpe hay una igualdad en la cantidad de turnos solicitados.")

    elif opcion == "5":
        print(f"Cerrando sistema. Operador: {operador}")
        break 
    
    else:
        print("Opción fuera de rango.")        

"""      


"""
ejercicio 4 ---- "Escape room: La Boveda"

"""
"""

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzar_seguidos = 0 


nombre = input("Por favor, ingrese nombre del agente: ")
while not nombre.isalpha(): 
    print("Error: El nombre debe contener solo letras.")
    nombre = input("Por favor, ingrese nombre del agente: ")

print(f"\nAgente {nombre}, buena suerte!!.")


while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
    
    
    if alarma == True and tiempo <= 3:
        print("\n¡SISTEMA BLOQUEADO POR ALARMA! Fuiste capturado!!.")
        break 

    print(f"\n--- ESTADO: Energía {energia} | Tiempo {tiempo} | Cerraduras {cerraduras_abiertas}/3 ---")
    if alarma: print("¡ALERTA: Alarma activa!")
    
    print("1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")
    
    opcion = input("Por favor, elija una acción: ")
    
    while not opcion.isdigit(): 
        print("Error:Por favor, ingrese un número válido.")
        opcion = input("Poe favor, elija una acción: ")

    if opcion == "1":
        energia = energia - 20 
        tiempo = tiempo - 2
        forzar_seguidos = forzar_seguidos + 1 

    
        if forzar_seguidos == 3:
            print("¡La cerradura se trabó! Se activó la alarma.")
            alarma = True
        else:
            if energia < 40:
                print("RIESGO DE ALARMA. Por favor, ingrese un número del 1 al 3:")
                riesgo = input("> ")
                while not riesgo.isdigit():
                    riesgo = input("Por favor, ingrese un número válido (1-3): ")
                if riesgo == "3":
                    alarma = True
                    print("¡Movimiento incorrecto! Alarma activada.")
            
            if not alarma:
                cerraduras_abiertas = cerraduras_abiertas + 1
                print("¡Cerradura abierta con éxito!")

    elif opcion == "2":
        
        forzar_seguidos = 0
        energia = energia - 10
        tiempo = tiempo - 3
    
        print("Hackeando...")
        for i in range(4): 
            codigo_parcial = codigo_parcial + "A" 
            print(f"Progreso: {codigo_parcial}")
            
    
        if len(codigo_parcial) >= 8:
            if cerraduras_abiertas < 3:
                cerraduras_abiertas = cerraduras_abiertas + 1
                print("¡Panel hackeado! Una cerradura se liberó.")
                codigo_parcial = "" 

    elif opcion == "3":
        forzar_seguidos = 0
        tiempo = tiempo - 1
        descanso = 15
        if alarma: 
            descanso = descanso - 10 
            print("No pudiste descansar por el ruido de la alarma.")
        
        energia = energia + descanso
        if energia > 100: energia = 100
        print(f"Te tomaste un desecanso. Recuperaste energia.")

    else:
        print("Opción fuera de rango.")

if cerraduras_abiertas >= 3:
    print(f"\n¡VICTORIA! El agente {nombre} abrió la bóveda.")
elif energia <= 0:
    print("\nDERROTA: Te quedaste sin energia.")
elif tiempo <= 0:
    print("\nDERROTA: Tiempo limite superado.")

"""


"""
Ejercicio 5:-----"Escape room: La Arena del Gladiador"

"""
"""
nombre = input("Por favor, ingrese el nombre del Gladiador: ")
while not nombre.isalpha():
    print("Error: Por favor, ingrese solo letras")
    nombre = input("Por favor, ingrese el nombre del Gladiador: ")

vida_gladiador = 100  
vida_enemigo = 100    
pociones = 3          
ataque_pesado_base = 15 
daño_enemigo = 12     
juego_activo = True    

while vida_gladiador > 0 and vida_enemigo > 0:
    print(f"\n--- {nombre}: {vida_gladiador} HP | Enemigo: {vida_enemigo} HP | Pociones: {pociones} ---")
    
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")
    
    opcion = input("Por favor, elija una opción (1-3): ")
    

    while not (opcion.isdigit() and (opcion == "1" or opcion == "2" or opcion == "3")):
        print("Error: Por favor, ingrese un número válido (1, 2 o 3).")
        opcion = input("Por favor, elija una opción (1-3): ")
    
    
    if opcion == "1":
        if vida_enemigo < 20:
            daño_final = ataque_pesado_base * 1.5
            print("¡GOLPE CRÍTICO!")
        else:
            daño_final = float(ataque_pesado_base)
        
        vida_enemigo = vida_enemigo - int(daño_final)
        print(f"¡Atacaste al enemigo por {daño_final} puntos de daño!")

    elif opcion == "2":
        print("¡-Tiraste una ráfaga de golpes!")
        for i in range(3):
            vida_enemigo = vida_enemigo - 5
            print(" > Diste un golpe por 5 de daño")

    elif opcion == "3":
        if pociones > 0:
            vida_gladiador = vida_gladiador + 30
            pociones = pociones - 1 
            print(f"¡Te curaste! Vida actual: {vida_gladiador}")
        else:
            print("¡Te quedaste sin pociones! Perdes el turno.")

    if vida_enemigo > 0:
        vida_gladiador = vida_gladiador - daño_enemigo
        print(f"¡Fuiste atacado por el enemigo por {daño_enemigo} puntos de daño!")

if vida_gladiador > 0:
    print(f"\n¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("\nDERROTA. El enemigo te vencio.")

"""
              

    
    