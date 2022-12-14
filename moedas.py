from cs50 import get_float

#Informar valor da compra, recebido, troco em 25, 10, 5 e 1 centavo.
compra = get_float ("Valor da compra: ")
recebido = get_float ("Valor recebido: ")
troco = recebido - compra
print(F"Troco: R$ {troco:.2f}")
moedas = {'25':0, '10':0, '5':0, '1':0}
while troco >= 0:
    if troco >= 0.25:
        troco -= 0.25
        moedas['25'] = moedas.get('25') +1
    elif troco >= 0.10:
        troco -= 0.10
        moedas['10'] = moedas.get('10') +1
    elif troco >= 0.05:
        troco -= 0.05
        moedas['5'] = moedas.get('5') +1
    elif troco > 0:
        troco -= 0.01
        moedas['1'] = moedas.get('1') +1
    else:
        break

for i in moedas:
    if moedas.get(i) > 0:
        print(f"Sendo: {moedas.get(i)} moeda(s) de {i}")
