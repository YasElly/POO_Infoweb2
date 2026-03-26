print("Digite uma sequência de números separados por vírgula:")
entrada = (input())
virgula = ','
partes = entrada.split(virgula)
num1 = int(partes[0])
num2 = int(partes[1])
num3 = int(partes[2])
num4 = int(partes[3])
num5 = int(partes[4])
soma = num1+num2+num3+num4+num5
print(f"Soma = {soma}")

