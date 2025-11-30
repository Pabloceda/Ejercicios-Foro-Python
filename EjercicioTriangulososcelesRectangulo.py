def dibujar_flecha_hueca():
    try:
        n = int(input("Introduce la altura de la figura: "))
    except ValueError:
        print("Entrada inválida. Por favor, introduce un número entero.")
        exit()

    if n <= 0:
        print("La altura debe ser mayor que 0.")
        return

    # Parte superior (desde la punta superior de la base hasta el centro)
    for i in range(1, n + 1):
        # Calculamos los espacios a la izquierda
        # Para n=5: i=1 -> 8 espacios, i=2 -> 6 espacios...
        espacios_izq = " " * (2 * (n - i))
        
        if i == 1:
            # El primer punto (esquina superior derecha)
            print(espacios_izq + "*")
        else:
            # Puntos intermedios: asterisco + hueco + asterisco
            # El hueco interior crece: 1, 3, 5, 7... (fórmula 2*i - 3)
            espacios_hueco = " " * (2 * i - 3)
            print(espacios_izq + "*" + espacios_hueco + "*")

    # Parte inferior (espejo de la superior)
    for i in range(n - 1, 0, -1):
        espacios_izq = " " * (2 * (n - i))
        
        if i == 1:
            print(espacios_izq + "*")
        else:
            espacios_hueco = " " * (2 * i - 3)
            print(espacios_izq + "*" + espacios_hueco + "*")

if __name__ == "__main__":
    dibujar_flecha_hueca()
