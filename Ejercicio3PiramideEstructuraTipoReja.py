def piramide_reja():
    try:
        n = int(input("Introduce la altura de la pirámide: "))
    except ValueError:
        print("Introduce un numero valido")
        exit()
    for i in range(1, n + 1):
        espacios_iniciales = " " * (n - i)
        if i == 1:
            print(espacios_iniciales + "*")
        elif i == n:
            print(espacios_iniciales + "*" * (2 * i - 1))
        else:
            espacios_huecos = " " * ((2 * i - 1) - 2)
            print(espacios_iniciales + "*" + espacios_huecos + "*")
piramide_reja()


