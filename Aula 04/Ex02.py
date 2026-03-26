print("Digite dois valores inteiros separados por um operador +, -, * ou /")
entrada = (input())
if "+" in entrada:
    operador = "+"
if "-" in entrada:
    operador = "-"
if "*" in entrada:
    operador = "*"
if "/" in entrada:
    operador = "/"
partes = entrada.split(operador)
num1 = int(partes[0])
num2 = int(partes[1])
if operador == '+':
    resultado = num1 + num2
elif operador == '-':
    resultado = num1 - num2
elif operador == '*':
    resultado = num1 * num2
elif operador == '/':
    resultado = num1 / num2
print(f"O resultado da operação é {resultado}")
