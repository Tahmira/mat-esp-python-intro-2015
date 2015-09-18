cartas = [11, 18, 3, 1, 16, 12, 6, 19, 5, 0, 14, 4, 17, 9, 13, 7, 10, 15, 2, 8] # lista das cartas
print("Lista original", cartas) # mostra escrito Lista original e depois mostra a lista de cartas inicial
N = 20 # numero de cartas
for i in range(0, N - 1, 1): # i variando de 0 ate N - 1 exclusive de 1 em 1, sendo ate N - 1 porque o intervalo final do python e aberto
    for j in range(i + 1, N, 1): # j variando de i + 1 ate N exclusive de 1 em 1, sendo ate N porque o intervalo final do python e aberto
        if cartas[i] > cartas[j]: # se a carta [i] for maior que a carta[j]:
            temp = cartas[i] #  a carta[i] em temp, para mover a carta[i] para um local temporario temp
            cartas[i] = cartas[j] # colocar a carta[j] em carta[i], para mover a carta[j] para a posicao da carta[i]
            cartas[j] = temp # colocar temp em carta[j], para mover a carta[i] que esta em temp para a posicao da carta[j]
print("Lista em ordem crescente", cartas) # mostra escrito Lista em ordem crescente e depois mostra a lista das cartas ordenadas em ordem crescente
