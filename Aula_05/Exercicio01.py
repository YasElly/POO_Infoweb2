class Água:
    def __init__(self):
        self.mes = 0
        self.ano = 0
        self.consumo = 0
        valor = 0
    def calculo(self):
        if self.consumo <= 10:
            valor = 38
        elif 11 <= self.consumo <= 20:
            valor = 38 + (self.consumo - 10) * 5
        else:  # acima de 20
            valor = 38 + (10 * 5) + (self.consumo - 20) * 6
        return valor

agua = Água()
agua.mes = int(input("Digite o mês (em números): "))
agua.ano = int(input("Digite o ano (em números):  "))
agua.consumo = float(input("Digite o consumo (em m³) do período selecionado: "))
conta = agua.calculo()
print(f"O valor da conta de {agua.mes}/{agua.ano} é igual a {conta:.2f}")
