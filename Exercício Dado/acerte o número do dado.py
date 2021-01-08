from modulos.numeros.leianumeros import leiaint, leiaInRange
from modulos.strings.escrita import linha, cabeçalho
from random import randint
from colorama import init

numdado = randint(1,6)
init()
cont = 1

cabeçalho(txt='NÚMERO DO DADO',tam=42)
print(f'{"O Computador Joguou Um Dado.":^42}')
print(f'{"Você Consegue Adivinhar Qual?":^42}')
linha()

while True:
    num = int(leiaint('Digite um Número Entre 1 e 6: ','\033[31mERRO! Digite Um Número Inteiro Válido.\033[m',cor=True))
    n = leiaInRange(num,1,6,'\033[31mERRO! Digite Um Número Entre 1 e 6.\033[m',cor=True)
    if n:
        if num == numdado:
            if cont == 1:
                print('Você Acertou Com 1 Tentativa.')
            else:
                print(f'Você Acertou Com {cont} Tentativas.')
            linha()
            while True:
                r = str(input('Você Quer Continuar? [S/N] ')).lower()
                if r in 'sn':
                    break
            if r == 'n':
                    linha()
                    break
            else:
                linha()
                numdado = randint(1,6)
                cont = 0
        else:
            if num > numdado:
                print('\033[33mMenos...\033[m')
            else:
                print('\033[32mMais...\033[m')
            linha()
        cont += 1
print('Volte Sempre.')