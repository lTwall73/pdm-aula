import math


numero = float(input('Digite um numero para calcular a raiz quadrada: '))

if numero >= 0:
    raiz_quadrada = math.sqrt(numero)
    print(f'A RAIZ QUADRADA DE {numero} É: {raiz_quadrada}')
else:
    print('Não é possivel calcular a raiz quadrada de zero ou numero negativo.')



