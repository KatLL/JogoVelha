# declarando as listas que compõem o início do jogo
tictac1 = [1, 2, 3]
tictac2 = [4, 5, 6]
tictac3 = [7, 8, 9]


formato1 = '--+---+--'
formato2 = '|'

# Imprimindo tabuleiro
print('\n', tictac1[0], formato2, tictac1[1], formato2, tictac1[2], '\n', formato1, '\n', tictac2[0], formato2, tictac2[1], formato2, tictac2[2], '\n', formato1, '\n', tictac3[0], formato2, tictac3[1], formato2, tictac3[2])

jogada1 = int(
    (input('\nJogador 1, escolha a posição que deseja marcar com X: ')))

for tictac1s in tictac1:
    jogada = int(tictac1s)

    if jogada == jogada1:
        tictac1[tictac1s-1] = 'X'

for tictac2s in tictac2:
    jogada = int(tictac2s)
    if jogada == jogada1:
        tictac2[tictac2s-4] = 'X'

for tictac3s in tictac3:
    jogada = int(tictac3s)
    if jogada == jogada1:
        tictac3[tictac3s-7] = 'X'
   
   #tentar usar com o try e except
   # else:
    #    print('Você deve preencher uma posição válida.')

print('\n', tictac1[0], formato2, tictac1[1], formato2, tictac1[2], '\n', formato1, '\n', tictac2[0], formato2, tictac2[1], formato2, tictac2[2], '\n', formato1, '\n', tictac3[0], formato2, tictac3[1], formato2, tictac3[2])
