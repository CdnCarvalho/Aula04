# Verifica maior idade
# idade = int(input('Informe sua idade: '))

# if idade >= 18:
#     print('Você é maior de idade')
# else:
#     print('Você é menor de idade')


# Testando mais condições
# Teste de pontos

# pontos = int(input('Quantos pontos? '))

# if pontos >= 100:
#     print('Nível máximo!')
# elif pontos >= 50:
#     print('Nível Bom!')
# elif pontos >= 25:
#     print('Pontuação ruim')
# else:
#     print('Pontuação Baixa')


# Verificação de login
# usuario = input('Informe o usuário: ').lower()
# senha = input('Digite a senha: ')

# print(usuario)

# if usuario == 'admin' and senha == '1234':
#     print('O pai tá on')
# else:
#     print('Ops! Usuário ou senha incorreto!')


# Condição para brinde
# compra = float(input('Valor da compra: '))
# cliente_frequente = input('Cliente frequente? [S/N]').lower()

# if compra >= 1000 or cliente_frequente == 's':
#     print('Tem direito a brinde')
# else:
#     print('Sem Brinde!')


nota = float(input('Informe a nota: '))
frequencia = float(input('Informe a freqência: '))

if nota >= 7:
    if frequencia >= 75:
        print('APROVADO')
    else:
        print('Boa nota, mas reporvado por falta')
else:
    print('Reprovado por nota!')       

