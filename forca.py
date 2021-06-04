from funcoes_do_jogo import *
from random import randint


def forca():
    titulo_frc()
    palavra_secreta = 'banana'.upper()
    letras_acertadas = ['_' for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0
    print(len(palavra_secreta))
    print(letras_acertadas)
    print('Vamos jogar?\nElaborar frase do jogo FORCA.')

    while not enforcou and not acertou:
        chute = input('Qual letra?\nDigite aqui: ').strip().upper()  # .strip() elimina os espaços entre caracteres

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)


    if acertou:
        print('Parabéns! Você ganhou.')
    else:
        print('Você perdeu.')
    fim()


if __name__ == '__main__':
    forca()
