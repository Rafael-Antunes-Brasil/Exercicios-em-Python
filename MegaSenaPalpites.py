from random import randint
from time import sleep
sorteio = []
listafinal = []
print('-='*15)
print('{:^30}'.format('JOGA NA MEGA SENA'))
print('-='*15)
sleep(1)
quantidade = int(input('Quantos jogos você quer que eu sorteie? '))
print('-='*15)
total = 1
while total <= quantidade:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in sorteio:
            sorteio.append(num)
            cont += 1
        if cont >= 6:
            break
    sorteio.sort()
    listafinal.append(sorteio[:])
    total += 1
    sorteio.clear()
print('~'*6, 'SORTEANDO', '~'*6)
for i, l in enumerate(listafinal):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('~'*6, 'BOA SORTE', '~'*6)
