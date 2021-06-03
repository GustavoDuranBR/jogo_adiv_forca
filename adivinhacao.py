from funcoes_do_jogo import *
from random import randint


def advinhacao():
    tentativas = 3

    num_secreto = randint(1, 10)

    titulo_adv()

    print('Vamos jogar?\nTente adivinhar o número que estou pensando.')

    for rodada in range(1, tentativas + 1):
        print(f'Rodada {rodada} de {tentativas}')
        palpite = int(input('Digite o seu palpite: '))
        if palpite < 1 or palpite > 100:
            print('Digite um número entre 1 e 100!')
            continue

        if palpite == num_secreto:
            print(f'Parabéns...Você acertou.')
            break
        else:
            if palpite < num_secreto:
                print('O número que eu estou pensando é maior.')
            else:
                print('O número que eu estou pensando é menor.')

    print(f'O número que eu pensei foi {num_secreto}')
    fim()


if __name__ == '__main__':
    advinhacao()
