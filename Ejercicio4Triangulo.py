altura = int(input("Introduce la altura de la escalera: "))
for i in range(1, altura + 1):
    for j in range(1, altura + 1):
        if i == altura or i == j or j == 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()