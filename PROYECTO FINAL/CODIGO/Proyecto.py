import random
import os
# =====================================
# TUPLAS (Reemplaza tus definiciones actuales con esto)
# =====================================
MENU_PRINCIPAL = ("Jugar", "Salir")
MENU_JUEGO = ("Ingresar letra", "Pedir pista", "Rendirse")
DIFICULTADES = ("FACIL", "MEDIA", "DIFICIL")
# =====================================
# LIMPIAR PANTALLA
# =====================================
def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

# =====================================
# CATEGORÍAS
# =====================================
categorias = {
    "PROGRAMACION": ["PYTHON", "JAVA", "VARIABLE"],
    "TECNOLOGIA": ["COMPUTADORA", "ROUTER", "SOFTWARE"],
    "UNIVERSIDAD": ["ESTUDIANTE", "PROFESOR", "FACULTAD"],
    "ANIMALES": ["PERRO", "GATO", "ELEFANTE"],
    "PAISES": ["ECUADOR", "COLOMBIA", "ARGENTINA"],
    "DEPORTES": ["FUTBOL", "TENIS", "NATACION"],
    "FRUTAS": ["MANZANA", "PERA", "BANANO"],
    "COLORES": ["AZUL", "VERDE", "ROJO"],
    "PROFESIONES": ["MEDICO", "ABOGADO", "ARQUITECTO"],
    "VEHICULOS": ["AUTOMOVIL", "CAMION", "MOTOCICLETA"]
}

# =====================================
# MENÚ PRINCIPAL (MANTENIDO)
# =====================================
def menu():
    limpiar()
    print("="*60)
    print("         JUEGO DEL AHORCADO    ")
    print("="*60)
    print("\n Bienvenido jugador")
    print(" Adivina la palabra antes de perder")
    print("\n1.  Jugar")
    print("2.  Salir")

# =====================================
# SELECCIONAR CATEGORÍA (PRIMERO)
# =====================================
def elegir_categoria():

    lista = list(categorias.keys())

    print("\n ELIGE UNA CATEGORÍA")
    print("-"*45)

    for i, c in enumerate(lista, 1):
        print(f"{i}. {c}")

    print(f"{len(lista)+1}. CATEGORIA ALEATORIA")

    op = input("\n Selecciona categoría: ")

    if op.isdigit() and 1 <= int(op) <= len(lista):
        cat = lista[int(op)-1]
    else:
        cat = random.choice(lista)

    return cat

# =====================================
# SELECCIONAR DIFICULTAD (SEGUNDO)
# =====================================
def elegir_dificultad():
    print("\n SELECCIONA DIFICULTAD")
    print("-" * 45)
    for i, dif in enumerate(DIFICULTADES, 1):
        print(f"{i}. {dif}")

    op = input("\n Selecciona dificultad: ")
    if op.isdigit() and 1 <= int(op) <= len(DIFICULTADES):
        return DIFICULTADES[int(op) - 1]
    return "MEDIA"

# =====================================
# GENERAR PALABRA SEGÚN CAT + DIFICULTAD
# =====================================
def obtener_palabra(cat, dif):
    lista = categorias[cat]
    
    # Filtramos según la longitud
    if dif == "FACIL": 
        filtradas = [p for p in lista if len(p) <= 4]
    elif dif == "MEDIA": 
        filtradas = [p for p in lista if 5 <= len(p) <= 7]
    else: # DIFICIL
        filtradas = [p for p in lista if len(p) >= 8]
    
    # IMPORTANTE: Si filtradas está vacía, usamos la lista original
    if len(filtradas) > 0:
        return random.choice(filtradas)
    else:
        return random.choice(lista)

# =====================================
# MENSAJE MOTIVADOR INICIAL
# =====================================
def inicio_juego(cat, dif, palabra):

    limpiar()
    print("="*60)
    print(" INICIANDO PARTIDA")
    print("="*60)

    print(f"\n Categoría seleccionada: {cat}")
    print(f" Dificultad: {dif}")

    print("\n El reto ha comenzado...")
    print(" Palabra oculta lista")

    print("\n " + " ".join(["_" for _ in palabra]))

# =====================================
# AYUDA SEGÚN DIFICULTAD
# =====================================
def ayuda(palabra, mostrada, usadas, dif):

    if dif == "FACIL":
        cant = 2
    elif dif == "MEDIA":
        cant = 1
    else:
        cant = 0

    letras = list(set(palabra))
    elegidas = random.sample(letras, min(cant, len(letras)))

    for l in elegidas:
        usadas.add(l)
        for i in range(len(palabra)):
            if palabra[i] == l:
                mostrada[i] = l

# =====================================
# TABLERO
# =====================================
def tablero(cat, dif, mostrada, usadas, intentos):

    print("\n" + "-"*60)
    print(f" Categoría: {cat}")
    print(f" Dificultad: {dif}")
    print(" Palabra:", " ".join(mostrada))
    print(" Letras usadas:", " ".join(sorted(usadas)))
    print(f" Intentos restantes: {6-intentos}")
    print("-"*60)

# =====================================
# VALIDACIÓN
# =====================================
def validar(l):
    return len(l) == 1 and l.isalpha()

# =====================================
# DIBUJO
# =====================================
def dibujo(i):

    d = [
        "-----\n|   |\n    |\n    |\n    |\n=====",
        "-----\n|   |\nO   |\n    |\n    |\n=====",
        "-----\n|   |\nO   |\n|   |\n    |\n=====",
        "-----\n|   |\nO   |\n/|  |\n    |\n=====",
        "-----\n|   |\nO   |\n/|\\ |\n    |\n=====",
        "-----\n|   |\nO   |\n/|\\ |\n/   |\n=====",
        "-----\n|   |\nO   |\n/|\\ |\n/ \\ |\n====="
    ]

    print(d[i])

# =====================================
# VICTORIA
# =====================================
def victoria(mostrada):
    return "_" not in mostrada

# =====================================
# FINAL DEL JUEGO
# =====================================
def fin(ganaste, palabra):

    while True:
        limpiar()

        if ganaste:
            print(" ¡VICTORIA! ")
        else:
            print(" HAS PERDIDO ")

        print("\n Palabra:", palabra)

        print("\n1. Jugar otra vez")
        print("2. Menú principal")
        print("3. Salir")

        op = input("\n Selecciona: ")

        if op == "1":
            jugar()
            return
        elif op == "2":
            return
        elif op == "3":
            print("\n ¡Gracias por jugar! Esperamos verte pronto.")
            exit()

# =====================================
# JUEGO PRINCIPAL
# =====================================
def jugar():

    menu()

    op = input("\n Selecciona: ")

    if op != "1":
        print("\n Gracias por jugar")
        exit()

    cat = elegir_categoria()

    dif = elegir_dificultad()

    palabra = obtener_palabra(cat, dif)

    mostrada = ["_"] * len(palabra)
    usadas = set()
    intentos = 0

    ayuda(palabra, mostrada, usadas, dif)

    inicio_juego(cat, dif, palabra)

    input("\n Enter para comenzar...")

    while True:

        limpiar()
        dibujo(intentos)
        tablero(cat, dif, mostrada, usadas, intentos)

        print("\n1. Letra")
        print("2. Pista")
        print("3. Rendirse")

        op = input("\n Selecciona: ")

        if not op.isdigit():
            continue

        op = int(op)

        if op == 2:

            ocultas = [i for i in range(len(palabra)) if mostrada[i] == "_"]

            if ocultas:
                pos = random.choice(ocultas)
                letra = palabra[pos]

                for i in range(len(palabra)):
                    if palabra[i] == letra:
                        mostrada[i] = letra

                usadas.add(letra)

                if victoria(mostrada):
                    fin(True, palabra)
                    return

            continue

        if op == 3:
            fin(False, palabra)
            return

        letra = input("\n Letra: ").upper()

        if not validar(letra):
            continue

        if letra in usadas:
            print("\n Ya usaste esa letra")
            input("\n Enter...")
            continue

        usadas.add(letra)

        if letra in palabra:
            for i in range(len(palabra)):
                if palabra[i] == letra:
                    mostrada[i] = letra
        else:
            intentos += 1

        if victoria(mostrada):
            fin(True, palabra)
            return

        if intentos >= 6:
            fin(False, palabra)
            return

# =====================================
# EJECUCIÓN
# =====================================
while True:
    jugar()