class País:
    def __init__(self):
        self.nome = 0
        self.populacao = 0
        self.area = 0
    def calculo(self):
        return self.populacao / self.area

maior_densidade = 0
pais_maior = ""

for i in range(10):
    print(f"País {i+1}")

    pais = País()
    pais.nome = input("Digite o nome do país: ")
    pais.populacao = int(input("Digite a população: "))
    pais.area = float(input("Digite a área (km²): "))

    densidade = pais.calculo()

    print(f"Densidade: {densidade:.2f} hab/km²")

    if densidade > maior_densidade:
        maior_densidade = densidade
        pais_maior = pais.nome

print(f"O país com maior densidade é: {pais_maior}")
print(f"Densidade: {maior_densidade:.2f} hab/km²")
