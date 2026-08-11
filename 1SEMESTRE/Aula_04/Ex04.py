print("Digite uma sequência de números separados por vírgula:")
entrada = (input())
virgula = ','
partes = entrada.split(virgula)
soma = 0
for numero in partes:
    soma += int(numero)
print(f"Soma = {soma}")
