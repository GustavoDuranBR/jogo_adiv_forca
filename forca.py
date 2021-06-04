from funcoes_do_jogo import *

def forca():
    titulo_frc()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)
    
    enforcou = False
    acertou = False
    erros = 0


    print('Vamos jogar?\n')

    while not acertou and not enforcou:
        chute = pede_chute()

        if chute in palavra_secreta:
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)
            print(desenha_forca)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    if acertou:
        imprime_vencedor()
    else:
        imprime_perdedor(palavra_secreta)

    fim()


if __name__ == '__main__':
    forca()
