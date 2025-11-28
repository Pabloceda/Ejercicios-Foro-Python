def diamante_hueco():
    try:
        n = int(input("Introduce la altura del diamante: "))
    except ValueError:
        print("Introduce un numero valido")
        exit()

    # La altura y anchura total es 2n - 1
    tamano = 2 * n - 1
    centro = n - 1

    for i in range(tamano):
        linea = ""
        for j in range(tamano):
            # Calculamos la distancia Manhattan desde el centro
            distancia = abs(i - centro) + abs(j - centro)
            
            # Imprimimos asterisco si estamos en el borde (distancia == n-1)
            # o si estamos en el centro exacto (distancia == 0)
            if distancia == n - 1:
                linea += "*"
            else:
                linea += " "
        print(linea)

diamante_hueco()
