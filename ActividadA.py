def calcular_cuadrados(n):
    suma_total = 0
    for numero in range(1, n+1):
        cuadrado = 0
        for j in range(numero):
            cuadrado += numero
        suma_total += cuadrado
        print(f"Número: {numero} | Cuadrado: {cuadrado} | metodo: {suma_total}")


n = int(input("Ingrese un número entero positivo: "))


calcular_cuadrados(n)

