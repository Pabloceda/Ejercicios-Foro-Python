def diamante_hueco():
    try:
        n = int(input("Introduce la altura del diamante: "))
    except ValueError:
        print("Introduce un numero valido")
        exit()

    for i in range(1, n + 1):
        espacios_iniciales = " " * (n - i)
        
        if i == 1:
            print(espacios_iniciales + "*")
        else:
            espacios_huecos = " " * ((2 * i - 1) - 2)
            print(espacios_iniciales + "*" + espacios_huecos + "*")

    for i in range(n - 1, 0, -1):
        espacios_iniciales = " " * (n - i)
        
        if i == 1:
            print(espacios_iniciales + "*")
        else:
            espacios_huecos = " " * ((2 * i - 1) - 2)
            print(espacios_iniciales + "*" + espacios_huecos + "*")

diamante_hueco()