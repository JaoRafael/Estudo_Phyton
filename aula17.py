'''num = [2, 5, 9, 1]
num[0] = 7
num.append(11)
num.sort(reverse=True)
num.insert(2,2)
if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 4')
num.remove(2)
print(num)
print(f'Essa lista tem {len(num)} elementos')'''

valores = []
'''valores.append(5)
valores.append(9)
valores.append(4)
valores.append(7)'''
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('END')