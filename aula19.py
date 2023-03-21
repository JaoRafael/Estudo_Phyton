'''pessoas = {'nome': 'João', 'sexo': 'M', 'idade': 36}
for k, v in pessoas.items():
    print(f'{k} = {v}')'''
estado = {}
brasil = []
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
    