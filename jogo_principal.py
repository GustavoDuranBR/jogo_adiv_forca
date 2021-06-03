import adivinhacao
from Python_Inicio.Jogo_Adivinhacao import forca
from funcoes_do_jogo import *

titulo_principal()

jogo = int(input('Qual jogo?'))

if jogo == 1:
    print('*** Jogando Adivinhação ***')
    adivinhacao.advinhacao()
elif jogo == 2:
    print('*** Jogando Forca ***')
    forca.forca()


