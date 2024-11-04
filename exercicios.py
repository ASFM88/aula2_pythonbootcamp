# 1.Escreva um programa que soma dois números inteiros inseridos pelo usuário.

valor1_inteiro = int(input('Insira um numero inteiro: '))
valor2_inteiro = int(input('Insira um numero inteiro: '))
soma = valor1_inteiro + valor2_inteiro
print(f'A soma do valor foi {soma}')

# 2.Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

resto_divisao = soma % 5
print(f'O resto da divisão de {valor1_inteiro} pelo {valor2_inteiro} é {resto_divisao}')

# 3.Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

multiplicacao = valor1_inteiro * valor2_inteiro
print(f'O valor da multiplicação de {valor1_inteiro} pelo {valor2_inteiro} é {multiplicacao}')

# 4.Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

divisao_inteira = valor1_inteiro // valor2_inteiro
print(f'A divisão inteira de {valor1_inteiro} pelo {valor2_inteiro} é {divisao_inteira}')

# 5.Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

potencializacao = valor1_inteiro**2
print(f'O quadrado de {valor1_inteiro} é {potencializacao}')

# 6.Escreva um programa que receba dois números flutuantes e realize sua adição.

valor1_float = float(input('Insira um numero: '))
valor2_float = float(input('Insira um numero: '))
soma_float = valor1_float + valor2_float
print(f'A soma do valor foi {soma_float}')

# 7.Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

media_float = soma_float / 2
print(f'A média da soma de {valor1_float} por {valor2_float} é {media_float}')

# 8.Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

base_float = float(input("Digite a base: "))
expoente_float = int(input("Digite o expoente: "))
potencia_float = base_float ** expoente_float
print(f"{base_float} elevado a {expoente_float} é igual a {potencia_float}")

# 9.Faça um programa que converta a temperatura de Celsius para Fahrenheit.

celsius = int(input('Informe temperatuda em Celsius: '))
conversao_farenheint = (celsius * 1.8) + 32
print(f'A conversão de {celsius}°C para Farenheit é {conversao_farenheint}°F')

# 10.Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

raio = float(input('Informe o raio do circulo: '))
pi = 3.14159
area_circulo = pi * (raio**2)
print(f'A area de um circulo com raio de {raio}cm é de {area_circulo:.2f}cm²')

# 11.Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

texto1 = str(input('Insira aqui seu texto: '))
print(texto1.upper())

# 12.Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

nome_usuario = str(input('Insira aqui seu nome completo: '))
print(nome_usuario.upper())

# 13.Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

print(texto1.strip())

# 14.Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

data = str(input('Informe uma data no formato "dd/mm/aaaa": '))
print(data.split('/'))

# 15.Escreva um programa que concatene duas strings fornecidas pelo usuário.

concatenar = texto1 + nome_usuario + data
print(concatenar)

# 16.Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

valor1 = True
valor2 = False
resultado_and = valor1 and valor2
print("Resultado do AND lógico:", resultado_and)

# 17.Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

resultado_or = valor1 or valor2
print("Resultado do OR lógico:", resultado_or)

# 18.Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.

resultado_not = not valor1
print("Resultado do NOT lógico:", resultado_not)

# 19.Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

resultado_igualdade = ( valor1_inteiro == valor2_inteiro )
print("Resultado da igualdade:", resultado_igualdade)

# 20.Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

resultado_diferenca = (valor1_inteiro != valor2_inteiro)
print("Resultado da diferença:", resultado_diferenca)

# 21.Exercício 21: Conversor de Temperatura

try:
    celsius = int(input('Informe temperatuda em Celsius: '))
    conversao_farenheint = (celsius * 1.8) + 32
    print(f'A conversão de {celsius}°C para Farenheit é {conversao_farenheint}°F')
except ValueError:
    print('Por favor, digite um número válido para a temperatura')

# 22.Verificador de Palíndromo

entrada = input("Digite uma palavra ou frase: ")
if isinstance(entrada, str):
    formatado = entrada.replace(" ", "").lower()
    if formatado == formatado[::-1]:
        print("É um palíndromo.")
    else:
        print("Não é um palíndromo.")
else:
    print("Entrada inválida. Por favor, digite uma palavra ou frase.")

# 23.Calculadora Simples

try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operador = input("Digite o operador (+, -, *, /): ")
    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/' and num2 != 0:
        resultado = num1 / num2
    else:
        print("Operador inválido ou divisão por zero.")
    print("Resultado:", resultado)
except ValueError:
    print("Erro: Entrada inválida. Certifique-se de inserir números.")

# 24.Classificador de Números

try:
    numero = int(input("Digite um número: "))
    if numero > 0:
        print("Positivo")
    elif numero < 0:
        print("Negativo")
    else:
        print("Zero")
    if numero % 2 == 0:
        print("Par")
    else:
        print("Ímpar")
except ValueError:
    print("Por favor, digite um número inteiro válido.")

# 25.Conversão de Tipo com Validação

entrada_lista = input("Digite uma lista de números separados por vírgula: ")
numeros_str = entrada_lista.split(",")
numeros_int = []
try:
    for num in numeros_str:
        numeros_int.append(int(num.strip()))
    print("Lista de inteiros:", numeros_int)
except ValueError:
    print("Erro: certifique-se de que todos os elementos são números inteiros válidos.")
    