numeros = []
pares = []
impares = []

for i in range(5):
    num = int(input("Digite um número: "))
    numeros.append(num)
    if num % 2 == 0: pares.append(num)
    else: impares.append(num)

print("Números pares: ", pares)
print("Números ímpares: ", impares)

media = sum(numeros) / len(numeros)
print("Média geral: ", media)
