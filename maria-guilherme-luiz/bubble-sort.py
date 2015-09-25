import matplotlib.pyplot as plt
cartas = [11, 18, 3, 1, 16, 12, 6, 19, 5, 0, 14, 4, 17, 9, 13, 7, 10, 15, 2, 8] # lista das cartas
print("Lista original", cartas) # mostra escrito Lista original e depois mostra a lista de cartas inicial
plt.figure()
x = range (0, 20)
plt.plot(x, cartas, 'ok')
plt.title ('range-x-cartas')
plt.xlabel ('range')
plt.ylabel ('cartas')
plt.savefig ('fig/bubble-inicio.png')
plt.close ()
a = 0
N = 20 # numero de cartas
for i in range(0, N - 1, 1): # i variando de 0 ate N - 1 exclusive de 1 em 1, sendo ate N - 1 porque o intervalo final do python e aberto
    for j in range(i + 1, N, 1): # j variando de i + 1 ate N exclusive de 1 em 1, sendo ate N porque o intervalo final do python e aberto
        plt.figure()
        plt.plot(x, cartas, 'ok')
        plt.plot(i, cartas [i], 'or')
        plt.plot(j, cartas [j], 'ob')
        plt.title ('range-x-cartas')
        plt.xlabel ('range')
        plt.ylabel ('cartas')
        a = a + 1
        plt.savefig ('fig/bubble-it-{}.png'.format(a))
        plt.close()
        if cartas[i] > cartas[j]: # se a carta [i] for maior que a carta[j]:
            temp = cartas[i] #  a carta[i] em temp, para mover a carta[i] para um local temporario temp
            cartas[i] = cartas[j] # colocar a carta[j] em carta[i], para mover a carta[j] para a posicao da carta[i]
            cartas[j] = temp # colocar temp em carta[j], para mover a carta[i] que esta em temp para a posicao da carta[j]
            plt.figure()
            plt.plot(x, cartas, 'ok')
            plt.title ('range-x-cartas')
            plt.xlabel ('range')
            plt.ylabel ('cartas')
            a = a + 1
            plt.savefig ('fig/bubble{}.png'.format(a))
            plt.close()
print("Lista em ordem crescente", cartas) # mostra escrito Lista em ordem crescente e depois mostra a lista das cartas ordenadas em ordem crescente
print ("Cinco menores valores", cartas[0: 5: 1])
print ("cinco maiores valores", cartas[15: 20: 1])
plt.figure()
plt.plot(x, cartas, 'ok')
plt.title ('range-x-cartas')
plt.xlabel ('range')
plt.ylabel ('cartas')
plt.savefig ('fig/bubble-fim.png')
plt.close ()
