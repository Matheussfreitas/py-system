#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit
celsius = float(input('Qual a medida de °C? '))
fahrenheit = (celsius * 9/5) + 32
print('{}°C é equivalente a {}°F'.format(celsius, fahrenheit))