class País:
    def __init__(self):
        self.nome = 0
        self.populacao = 0
        self.area = 0
    def calculo(self):
        return self.populacao / self.area
    
pais = País()
pais.nome = input("Digite o nome do país: ")
pais.populacao = int(input("Digite a população do país selecionado: "))
pais.area = float(input("Digite a área (em km²) do país selecionado: "))
densidade = pais.calculo()
print(f"A densidade demográfica do(a) {pais.nome} é de {densidade:.2f} hab/km²")