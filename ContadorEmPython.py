from time import sleep


def linha():
    print('-='*20)


def contador(i, f, p):

    print(f'Contagem de {i} ate {f} de {p} em {p} ')
    if i < f:
        for cont in range(i, f+1, p):
            print(cont, end=' ', flush=True)
            sleep(0.5)
        print('FIM')
    if f < i:
        for cont in range(i, f-1, -p):
            print(cont, end=' ', flush=True)
            sleep(0.5)
        print('FIM')
    linha()

linha()
contador(1, 10, 1)
sleep(1)

contador(10, 0, 2)
sleep(1)

print('Agora é a sua vez de personalizar a contagem: ')
a = int(input('Inicio: '))
b = int(input('Fim: '))
c = int(input('Passo: '))
if c == 0:
    c = 1
if c < 0:
    c *= -1
linha()
contador(a, b, c)