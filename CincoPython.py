
matriz = []
for i in range(3):
    nome = input("Digite o nome do aluno {}: ".format(i+1))
    notas = []
    for j in range(4):
        nota = float(input("Digite a nota {}: ".format(j+1)))
        notas.append(nota)
    matriz.append([nome, notas])

maior_media = 0
menor_media = 10
nome_maior_media = ""
nome_menor_media = ""

for aluno in matriz:
    nome = aluno[0]
    notas = aluno[1]
    media = sum(notas) / len(notas)
    print("Aluno: {} - Média: {:.2f}".format(nome, media))
    if media > maior_media:
        maior_media = media
        nome_maior_media = nome
    if media < menor_media:
        menor_media = media
        nome_menor_media = nome

print("O aluno com a maior média é: ", nome_maior_media)
print("O aluno com a menor média é: ", nome_menor_media)
