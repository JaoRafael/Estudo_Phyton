'''test = []
test.append('João')
test.append(36)
galera = []
galera.append(test[:])
test[0] = 'Camila'
test[1] = 28

galera.append(test[:])
print(galera)
galera = [['João', 36], ['Camila', 28], ['Guilherme', 27], ['Nathalia', 25]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')'''

galera = []
dado = []
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade?: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai +=1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')