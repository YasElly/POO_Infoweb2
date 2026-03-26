entrada = input()
soma = 0
numeros = ['0','1','2','3','4','5','6','7','8','9']
for caractere in entrada:
    if caractere in numeros:
        soma += int(caractere)

print(f"Soma = {soma}")