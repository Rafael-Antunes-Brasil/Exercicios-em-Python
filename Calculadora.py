from time import sleep

def menu():
    print('-'*7,'MENU','-'*7,'\n'
          '1 - SOMA.\n'
          '2 - SUBTRAÇÃO.\n'
          '3 - DIVISÃO.\n'
          '4 - MULTIPLICAÇÃO.\n'
          '5 - EXPONENCIAÇÃO.\n'
          '6 - PARTE INTEIRA.\n'
          '7 - MÓDULO.')
    print('-='*10)


def escolha(esc, n1, n2):
    if esc == 1:
        resultado = n1 + n2
        return resultado
    if esc == 2:
        resultado = n1 - n2
        return resultado
    if esc == 3:
        resultado = n1 / n2
        return resultado
    if esc == 4:
        resultado = n1 * n2
        return resultado
    if esc == 5:
        resultado = n1 ** n2
        return resultado
    if esc == 6:
        resultado = n1 // n2
        return resultado
    if esc == 7:
        resultado = n1 % n2
        return resultado
    else:
        resultado = False
        return resultado


print('Bem vindo ao projeto:')
sleep(1)
print('\033[1;35;40mCALCULADORA BÁSICA\033[m')
print('-='*10)
sleep(2)
while True:
    n1 = float(input('Digite um numero: '))
    n2 = float(input('Digite outro numero: '))
    menu()
    while True:
        esc = int(input('Escolha uma das opções: '))
        res = escolha(esc,n1,n2)
        if res == False:
            print('\033[1;31mOpção Invalída!!\033[m')
        else:
            break
    print('O resultado é ', res)
    while True:
        decisao = str(input('Quer continuar?[S/N] ')).upper().strip()
        if decisao in 'SN':
            break
        print('\033[1;31mERRO! Digite S ou N\033[m')
    if decisao == 'N':
        print('Até a próxima...')
        sleep(1)
        break

