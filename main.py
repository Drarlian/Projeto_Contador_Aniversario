"""
Contador para a data do aniversario.

OBS: É feito para se executar no terminal pois possui o "os.system('cls')" que limpa o terminal a cada execução,
mostrando uma atualização constante do tempo restante.
"""
import datetime
from time import sleep
import os


nascimento = str(input('Digite a sua data de nascimento: dd/mm/aaaa '))

aniversario = nascimento[0:-4] + str(datetime.datetime.now().year)

aniversario = datetime.datetime.strptime(aniversario, '%d/%m/%Y')

if datetime.datetime.now().month >= aniversario.month:  # -> Determina se estamos no mês do aniversario ou se o mes já passou.
    if datetime.datetime.now().day > aniversario.day:  # -> Determina se o dia dentro do mês do aniversario já passou ou não.
        aniversario = datetime.datetime(day=aniversario.day, month=aniversario.month, year=aniversario.year + 1)

while True:
    os.system('cls')  # -> Limpa o terminal.
    data_atual = datetime.datetime.now()
    tempo_aniversario = aniversario - data_atual

    print(tempo_aniversario)
    sleep(1)
