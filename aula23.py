try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados digitados')
except ZeroDivisionError:
    print('Não é possivel dividir um número por Zero(0)')
except KeyboardInterrupt:
    print('Usuário preferiu não informar os dados')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('É noiz, tamo junto!')