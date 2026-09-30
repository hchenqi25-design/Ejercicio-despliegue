matriz = []

for i in range(10):
    fila = []
    for j in range(10):

        if i == j:
            fila.append(0)
        else:
            fila.append(1)
    matriz.append(fila)

for fila in matriz:
    print(fila)
