from datetime import date

dataatual = f'{date.today().day}/{date.today().month}/{date.today().year}'
gasto = {}
dados = []
ganho = []

while True:
    gasto['nome'] = str(input('Lugar da compra: '))
    gasto['data'] = dataatual
    gasto['valor'] = float(input('Valor da compra R$ '))
    dados.append(gasto.copy())
    gasto.clear()
    esc = str(input('Quer adicionar novo gasto?[S/N] ')).upper().strip()
    if esc == 'N':
        break
print(dados)
