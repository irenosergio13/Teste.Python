numeros = []

for i in range(5):
    num = int(input("Digite um número: "))
    numeros.append(num)

maior = numeros[0]
menor = numeros[0]
for num in numeros:
    if num > maior:
        maior = num
    if num < menor:
        menor = num

print("O número maior é: ", maior)
print("O número menor é: ", menor)
