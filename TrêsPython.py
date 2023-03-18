while True:
    nome = input("Digite o nome do aluno: ")
    notas = []
    for i in range(4):
        nota = float(input("Digite a nota {}: ".format(i+1)))
        notas.append(nota)
    media = sum(notas)/len(notas)
    if media >= 6:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"
    print("Aluno: {} - Média: {:.2f} - Situação: {}".format(nome, media, situacao))
    continuar = input("Deseja encerrar o programa? (S/N): ")
    if continuar.upper() == "S":
        break
