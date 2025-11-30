def diamante_hueco():
    try:
        n = int(input("Introduce la altura del diamante: "))
    except ValueError:
        print("Introduce un numero valido")
        exit()

    # Mitad superior
    for i in range(1, n + 1):
        # Espacios a la izquierda (igual que en el sólido)
        espacios_iniciales = " " * (n - i)
        
        if i == 1:
            # La primera punta es solo un asterisco
            print(espacios_iniciales + "*")
        else:
            # Filas intermedias: asterisco + hueco + asterisco
            # El hueco se calcula restando los 2 asteriscos del ancho total (2*i - 1)
            # Ancho total - 2 = (2*i - 1) - 2 = 2*i - 3
            espacios_huecos = " " * ((2 * i - 1) - 2)
            print(espacios_iniciales + "*" + espacios_huecos + "*")

    # Mitad inferior (espejo de la superior, sin repetir la fila central)
    for i in range(n - 1, 0, -1):
        espacios_iniciales = " " * (n - i)
        
        if i == 1:
            print(espacios_iniciales + "*")
        else:
            espacios_huecos = " " * ((2 * i - 1) - 2)
            print(espacios_iniciales + "*" + espacios_huecos + "*")

diamante_hueco()