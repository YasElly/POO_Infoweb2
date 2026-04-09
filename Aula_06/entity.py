#Entidades
class Aluno:
    def __init__(self):
        self.__nome = "" #atributos escondidos
        self.__matricula = "" #atributos encapsulados
    def set_nome(self, valor):
        if len(valor)<3: raise ValueError("Nome deve ter pelo menos 2 letras")
        self.__nome = valor
    def get_nome(self):
        return self.__nome
    def set_matricula(self, valor):
        if len(valor)<5: raise ValueError("Nome deve ter pelo menos 5 caracteres")
        self.__matricula = valor
    def get_matricula(self):
        return self.__matricula
    def ano_ingresso(self):
        return int(self.__matricula[:4])
    
class UI:
    def main():
        #Programa principal
        x=Aluno()
        #x.nome= input("Digite o nome:")
        x.set_nome = input("Informe o nome: ")
        #x.matricula = input("Digite a matrícula")
        x.set_matricula(input("Informe a matrícula: "))
        ano = x.ano_ingresso()
        print(f"O aluno {x.get_nome()}, de matrícula {x.get_matricula()}")
        print(f"Entrou no IF em {ano}")
UI.main()