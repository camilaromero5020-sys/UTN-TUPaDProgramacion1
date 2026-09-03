#Tp Integrador repetitivas, condicionales y secuenciales.
#Ejercicio 1 "Caja del kiosco"
#(
nombre = input("Ingrese su nombre: ")
while nombre == "" or not nombre.isalpha():
    print ("Error, ingrese un nombre valido.")
    nombre = input("Ingrese su nombre: ")

cantidad_productos = input("Ingrese la cantidad de productos a comprar: ")
while not cantidad_productos.isdigit() or int(cantidad_productos) <= 0:
    print ("Error, ingrese una cantidad de productos valida.")
    cantidad_productos = input("Ingrese la cantidad de productos a comprar: ")

cantidad_productos = int(cantidad_productos)

total_sin_descuentos = 0.0
total_con_descuentos = 0.0
detalle_productos = ""

for i in range (1, cantidad_productos + 1):
    print(f"\nProducto {i}")

    precio = input("Precio: ")
    while not precio.isdigit():
        print ("Ingrese un precio valido.")
        precio = input("Precio: ")

    precio = int(precio)
    total_sin_descuentos += precio

    descuento = input("Descuento (S/N): ").lower()
    while descuento not in ['s', 'n']:
        print("Error, Ingrese 's' o 'n'.")
        descuento = input("Descuento (S/N): ").lower()

    if descuento == 's':
        precio_final = precio * 0.90
    else:
        precio_final = precio
    
    total_con_descuentos += precio_final
    detalle_productos += f" - Producto {i}: ${precio} - Descuento: {descuento}\n"


ahorro_total = total_sin_descuentos - total_con_descuentos
promedio_por_producto = total_con_descuentos / cantidad_productos

print ("")
print (f"Cliente {nombre}")
print (f"Cantidad de productos: {cantidad_productos}")
print("\nDetalle de productos:")
print(detalle_productos, end="")
print ("")
print (f"Total sin descuento: ${total_sin_descuentos:.2f}")
print (f"Total con descuenos: ${total_con_descuentos:.2f}")
print (f"Ahorro total: ${ahorro_total:.2f}")
print (f"Promedio por producto: ${promedio_por_producto:.2f}")



#Ejercicio 2 "Acceso al campus y menu seguro"

usuario_correcto = "alumno"
clave_correcta = "python123"

intentos = 1
max_intentos = 3
acceso_concedido = False

print("Bienvenido al Campus")
print ("")
while intentos <= max_intentos and not acceso_concedido:
    print(f"Intento {intentos}/{max_intentos}")
    usr = input("Usuario: ")
    clave = input("Clave: ")
    
    if usr == usuario_correcto and clave == clave_correcta:
        acceso_concedido = True
        print("Acceso concedido.")
    else:
        print("Error: credenciales inválidas.\n")
        intentos += 1

if not acceso_concedido:
    print("Cuenta bloqueada")
else:
    opcion = ""
    while opcion != "4":
        print("\n1) Estado 2) Cambiar clave 3) Mensaje 4) Salir")
        opcion_input = input("Opción: ")
        
        if not opcion_input.isdigit():
            print("Error: ingrese un número válido.")
        elif int(opcion_input) < 1 or int(opcion_input) > 4:
            print("Error: opción fuera de rango.")
        else:
            opcion = opcion_input
            
            # Opción 1: Ver estado
            if opcion == "1":
                print("Inscripto")
                
            # Opción 2: Cambiar clave
            elif opcion == "2":
                nueva_clave = input("Nueva clave: ")
                while len(nueva_clave) < 6:
                    print("Error: mínimo 6 caracteres.")
                    nueva_clave = input("Nueva clave: ")
                
                confirmacion = input("Confirmar clave: ")
                if nueva_clave == confirmacion:
                    clave_correcta = nueva_clave
                    print("Clave cambiada con éxito.")
                else:
                    print("Error: las claves no coinciden.")
                    
            # Opción 3: Mensaje motivacional
            elif opcion == "3":
                print("¡Cree en ti mismo, eres capaz de grandes cosas!")
                
            # Opción 4: Salir
            elif opcion == "4":
                print("Sesión finalizada.")




# Ejercicio 3 "Agenda de Turnos con Nombres (sin listas)"
operador = input("Nombre del operador: ")
while not operador.isalpha():
    print("Error: Ingrese un nombre válido (solo letras).")
    operador = input("Nombre del operador: ")

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

opcion = ""

while opcion != "5":
    print("AGENDA DE TURNOS")
    print("1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")

    print ("")
    
    opcion_input = input("Seleccione una opción: ")
    while not opcion_input.isdigit() or int(opcion_input) < 1 or int(opcion_input) > 5:
        print("Error: Ingrese una opción válida (1-5).")
        opcion_input = input("Seleccione una opción: ")
        
    opcion = opcion_input

    # OPCIÓN 1:RESERVAR TURNO
    if opcion == "1":
        dia_input = input("Elija el día (1 = Lunes, 2 = Martes): ")
        while not dia_input.isdigit() or dia_input not in ["1", "2"]:
            print("Error: Elija 1 para Lunes o 2 para Martes.")
            dia_input = input("Elija el día (1 = Lunes, 2 = Martes): ")
            
        paciente = input("Nombre del paciente: ")
        while not paciente.isalpha():
            print("Error: El nombre debe contener solo letras.")
            paciente = input("Nombre del paciente: ")
            
        if dia_input == "1":
            if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                print("Error: El paciente ya tiene un turno reservado para el Lunes.")
            elif lunes1 == "":
                lunes1 = paciente
                print("Turno reservado en Lunes (Turno 1).")
            elif lunes2 == "":
                lunes2 = paciente
                print("Turno reservado en Lunes (Turno 2).")
            elif lunes3 == "":
                lunes3 = paciente
                print("Turno reservado en Lunes (Turno 3).")
            elif lunes4 == "":
                lunes4 = paciente
                print("Turno reservado en Lunes (Turno 4).")
            else:
                print("No hay turnos disponibles para el Lunes.")
                
        elif dia_input == "2":
            if paciente == martes1 or paciente == martes2 or paciente == martes3:
                print("Error: El paciente ya tiene un turno reservado para el Martes.")
            elif martes1 == "":
                martes1 = paciente
                print("Turno reservado en Martes (Turno 1).")
            elif martes2 == "":
                martes2 = paciente
                print("Turno reservado en Martes (Turno 2).")
            elif martes3 == "":
                martes3 = paciente
                print("Turno reservado en Martes (Turno 3).")
            else:
                print("No hay turnos disponibles para el Martes.")

    # OPCIÓN 2:CANCELAR TURNO
    elif opcion == "2":
        dia_input = input("Elija el día (1 = Lunes, 2 = Martes): ")
        while not dia_input.isdigit() or dia_input not in ["1", "2"]:
            print("Error: Elija 1 para Lunes o 2 para Martes.")
            dia_input = input("Elija el día (1 = Lunes, 2 = Martes): ")
            
        paciente = input("Nombre del paciente a cancelar: ")
        while not paciente.isalpha():
            print("Error: El nombre debe contener solo letras.")
            paciente = input("Nombre del paciente a cancelar: ")
            
        cancelado = False
        if dia_input == "1":
            if lunes1 == paciente:
                lunes1 = ""
                cancelado = True
            elif lunes2 == paciente:
                lunes2 = ""
                cancelado = True
            elif lunes3 == paciente:
                lunes3 = ""
                cancelado = True
            elif lunes4 == paciente:
                lunes4 = ""
                cancelado = True
        elif dia_input == "2":
            if martes1 == paciente:
                martes1 = ""
                cancelado = True
            elif martes2 == paciente:
                martes2 = ""
                cancelado = True
            elif martes3 == paciente:
                martes3 = ""
                cancelado = True
                
        if cancelado:
            print(f"Turno de {paciente} cancelado exitosamente.")
        else:
            print("No se encontró al paciente en el día seleccionado.")

    # OPCIÓN 3:VER AGENDA
    elif opcion == "3":
        dia_input = input("Elija el día a consultar (1 = Lunes, 2 = Martes): ")
        while not dia_input.isdigit() or dia_input not in ["1", "2"]:
            print("Error: Elija 1 para Lunes o 2 para Martes.")
            dia_input = input("Elija el día a consultar (1 = Lunes, 2 = Martes): ")
            
        if dia_input == "1":
            print("AGENDA LUNES")
            print(f"Turno 1: {lunes1 if lunes1 != '' else '(libre)'}")
            print(f"Turno 2: {lunes2 if lunes2 != '' else '(libre)'}")
            print(f"Turno 3: {lunes3 if lunes3 != '' else '(libre)'}")
            print(f"Turno 4: {lunes4 if lunes4 != '' else '(libre)'}")
        elif dia_input == "2":
            print("AGENDA MARTES")
            print(f"Turno 1: {martes1 if martes1 != '' else '(libre)'}")
            print(f"Turno 2: {martes2 if martes2 != '' else '(libre)'}")
            print(f"Turno 3: {martes3 if martes3 != '' else '(libre)'}")

    # OPCIÓN 4:VER RESUMEN GENERAL
    elif opcion == "4":
        # Cont Lunes
        lunes_ocupados = 0
        if lunes1 != "": lunes_ocupados += 1
        if lunes2 != "": lunes_ocupados += 1
        if lunes3 != "": lunes_ocupados += 1
        if lunes4 != "": lunes_ocupados += 1
        lunes_disponibles = 4 - lunes_ocupados

        # Cont Martes
        martes_ocupados = 0
        if martes1 != "": martes_ocupados += 1
        if martes2 != "": martes_ocupados += 1
        if martes3 != "": martes_ocupados += 1
        martes_disponibles = 3 - martes_ocupados

        print("RESUMEN GENERAL")
        print(f"Lunes: {lunes_ocupados} ocupados, {lunes_disponibles} disponibles")
        print(f"Martes: {martes_ocupados} ocupados, {martes_disponibles} disponibles")
        
        if lunes_ocupados > martes_ocupados:
            print("Día con más turnos: Lunes")
        elif martes_ocupados > lunes_ocupados:
            print("Día con más turnos: Martes")
        else:
            print("Día con más turnos: Empate")

    # OPCIÓN 5:CERRAR SISTEMA
    elif opcion == "5":
        print(f"Sistema cerrado. Operador: {operador}")



#Ejercicio 4 — “Escape Room: La Bóveda”
agente = input("Nombre del agente: ")
while not agente.isalpha():
    print("Error: Ingrese un nombre válido (solo letras).")
    agente = input("Nombre del agente: ")

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

forzar_seguidas = 0

print(f"\n¡Bienvenido Agente {agente}! La misión para abrir la bóveda empieza ya.")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not (alarma and tiempo <= 3):
    print("\n----------------------------------------")
    print(f"ESTADO: Energía: {energia} | Tiempo: {tiempo} | Cerraduras abiertas: {cerraduras_abiertas}/3")
    print(f"Alarma: {'ACTIVADA' if alarma else 'Desactivada'} | Código: '{codigo_parcial}'")
    print("----------------------------------------")
    print("1. Forzar cerradura (-20 energía, -2 tiempo)")
    print("2. Hackear panel (-10 energía, -3 tiempo)")
    print("3. Descansar (+15 energía, -1 tiempo)")
    
    opcion_input = input("Seleccione una acción (1-3): ")
    while not opcion_input.isdigit() or int(opcion_input) < 1 or int(opcion_input) > 3:
        print("Error: Seleccione una opción válida (1, 2 o 3).")
        opcion_input = input("Seleccione una acción (1-3): ")
        
    opcion = int(opcion_input)

    if opcion == 1:
        forzar_seguidas += 1
        
        energia -= 20
        tiempo -= 2
        
        if forzar_seguidas == 3:
            print("¡LA CERRADURA SE TRABÓ! Anti-spam detectado. Se activa la alarma.")
            alarma = True
        else:
            # Riesgo de alarma energía menor a 40
            riesgo_activado = False
            if energia < 40 and not alarma:
                print("¡Riesgo de alarma por baja energía!")
                num_input = input("Elija un número de seguridad (1-3): ")
                while not num_input.isdigit() or int(num_input) < 1 or int(num_input) > 3:
                    print("Error: Elija un número entre 1 y 3.")
                    num_input = input("Elija un número de seguridad (1-3): ")
                
                if int(num_input) == 3:
                    print("¡Elegiste el número incorrecto! Alarma activada.")
                    alarma = True
                    riesgo_activado = True

            if not riesgo_activado and not alarma:
                cerraduras_abiertas += 1
                print(f"¡Cerradura forzada con éxito! ({cerraduras_abiertas}/3)")

    # OPCIÓN 2:HACKEAR PANEL
    elif opcion == 2:
        forzar_seguidas = 0 
        
        energia -= 10
        tiempo -= 3
        
        print("Iniciando hackeo de panel...")
        for paso in range(1, 5):
            codigo_parcial += "A"
            print(f"> Paso {paso}/4: Progreso del código -> {codigo_parcial}")
            
        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print(f"¡Código suficiente completado ({len(codigo_parcial)} caracteres)! Se abre 1 cerradura de forma automática.")

    # OPCIÓN 3:DESCANSAR
    elif opcion == 3:
        forzar_seguidas = 0
        
        energia += 15
        if energia > 100:
            energia = 100
            
        tiempo -= 1
        
        if alarma:
            energia -= 10
            print("Descansaste, pero el estrés de la alarma encendida te hace perder 10 de energía extra.")
        else:
            print("Descansaste un poco y recuperaste energía.")

print("\n========================================")
if cerraduras_abiertas == 3:
    print(f"¡VICTORIA! El agente {agente} ha abierto las 3 cerraduras y saqueado la bóveda.")
elif alarma and tiempo <= 3 and cerraduras_abiertas < 3:
    print(f"DERROTA (Bloqueo): La alarma sonó con poco tiempo restante. La bóveda se bloqueó permanentemente.")
elif energia <= 0 or tiempo <= 0:
    print(f"DERROTA: El agente {agente} se ha quedado sin {'energía' if energia <= 0 else 'tiempo'}.")
print("========================================")


#Ejercicio 5 — “Escape Room:"La Arena del Gladiador" 
nombre = input("Nombre del Gladiador: ")
while not nombre.isalpha():
    print("Error: Solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ")

vida_jugador = 100      
vida_enemigo = 100      
pociones = 3            
dano_pesado = 15         
dano_enemigo = 12       
turno_gladiador = True  

print("---INICIO DEL COMBATE---")

while vida_jugador > 0 and vida_enemigo > 0:
    print(f"\n{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    print("Elige acción:")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")
    
    opcion_input = input("Opción: ")
    while not opcion_input.isdigit() or int(opcion_input) < 1 or int(opcion_input) > 3:
        print("Error: Ingrese un número válido (1-3).")
        opcion_input = input("Opción: ")
        
    opcion = int(opcion_input)

    if opcion == 1:
        if vida_enemigo < 20:
            dano_final = float(dano_pesado * 1.5) 
            print("¡GOLPE CRÍTICO!")
        else:
            dano_final = float(dano_pesado)
            
        vida_enemigo -= int(dano_final)
        print(f"¡Atacaste al enemigo por {dano_final:.1f} puntos de daño!")

    elif opcion == 2:
        print(">> ¡Inicias una ráfaga de golpes!")
        for _ in range(3):
            vida_enemigo -= 5
            print("> Golpe conectado por 5 de daño")

    elif opcion == 3:
        if pociones > 0:
            vida_jugador += 30
            pociones -= 1
            print(f"Te curaste 30 HP. Te quedan {pociones} pociones.")
        else:
            print("¡No quedan pociones! Pierdes el turno.")

    if vida_enemigo > 0:
        vida_jugador -= dano_enemigo
        print(f"¡El enemigo te atacó por {dano_enemigo} puntos de daño!")

print("\n========================================")
if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en el combate.")
print("========================================")