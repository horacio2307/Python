#By Juan Horacio Rivera Peña
def Decimal2binary(numero):

    Binario = ""

    while numero // 2 != 0 :

        Binario = str(numero%2) + Binario
        numero = numero // 2

    return str(numero) + Binario


valor_prueba = int(input("Ingrese el numero que desea convertir: "))

valor_binario = Decimal2binary(valor_prueba)

print(valor_binario)

