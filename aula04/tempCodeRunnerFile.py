# Condição para brinde
compra = float(input('Valor da compra'))
cliente_frequente = input('Cliente frequente? [S/N]').lower()

if compra >= 1000 or cliente_frequente == 's':
    print('Tem direito a brinde')
else:
    print('Sem Brinde!')
