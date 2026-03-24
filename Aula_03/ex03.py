#CÍRCULO
class Circulo:
    def __init__(self):
        self.r = 0
    def calc_area(self):
        return 3.14 * self.r ** 2 #(A = PI x R²)
    def calc_circunferencia(self):
        return 2 * 3.14 * self.r #(CIRC = 2 x PI x R)
     
print("CÁLCULOS DE ÁREA E CIRCUNFERÊNCA DO CIRCULO")
x = Circulo()
print("Informe o raio do círculo")
x.r = float(input())
c = x.calc_circunferencia()
a = x.calc_area()
print(f"A área do círculo é {a:.2f}cm²")
print(f"A circunferência do círculo é {c:.2f}cm")
print(f"Círculo: raio = {x.r}, área = {x.calc_area()}, circunferência = {x.calc_circunferencia()}")


