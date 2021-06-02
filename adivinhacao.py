from funcoes_do_jogo import *
from random import randint

acertou = False
palpite = 0

num_secreto = randint(1, 10)

titulo()

print('Vamos jogar?\nTente adivinhar o número que estou pensando.')

while not acertou:
    player = int(input('Digite o seu palpite: '))
    palpite += 1
    if player == num_secreto:
        acertou = True
    else:
        if player < num_secreto:
            print('O número que eu estou pensando é maior.')
        else:
            print('O número que eu estou pensando é menor.')

print(f'Você acerto com {palpite} tentativas.')
print(f'O número que eu pensei foi {num_secreto}')

fim()
