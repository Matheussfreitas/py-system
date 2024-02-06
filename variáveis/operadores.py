n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
som = n1 + n2
sub = n1 - n2
mul = n1 * n2
div = n1 / n2
divint = n1 // n2
rest = n1 % n2
pot = n1 ** n2
print('A soma é {}, a subtração é {}, a multriplicação é {}'.format(som, sub, mul))
print('E a divisão é {}, a divisão int é {}, o resto é {} e a potência é {}'.format(div, divint, rest, pot))