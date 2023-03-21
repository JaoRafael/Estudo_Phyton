nome = str(input('Qual o seu nome? ')).upper()
if nome == 'JOÃO':
    print(f'Não acredito, que nome bonito {nome}!!')
elif nome in 'MARIA ALICE ENZO':
    print(f'Seu nome é bem popular no Brasil {nome}')
elif nome in 'ANA FLORA LUIZA':
    print(f'Belo nome feminino {nome}!')
else:
    print(f'Seu nome é bem comum {nome}!')
print('Tenha um bom dia !')
