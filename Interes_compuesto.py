

C = int(input("Digite su capital: "))

n = 0
D = 2 * C


while ( C < D ):
    C = C + 0.05 * C
    n = n + 1
    print(" Mes" + str (n))
    print("Capital " + str (C))

print("El mes donde el capital se duplica es : " + str(n))