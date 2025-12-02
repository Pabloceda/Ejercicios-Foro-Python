#M
def programa_M():
    try:
        n = int(input("Introduce la altura de la M: "))
    except ValueError:
        print("Introduce un valor valido")
        exit()
    
    for i in range(n):
        for j in range(n):
            if j == 0 or j == n - 1 or (i <= n // 2 and (i == j or i + j == n - 1)):
                print("*", end="")
            else:
                print(" ", end="")
        print()
programa_M()
