from datetime import datetime
from datetime import timedelta

class Treino:
    def __init__(self, id, data, distancia, tempo):
        self.set_id(id)
        self.set_data(data)
        self.set_distancia(distancia)
        self.set_tempo(tempo)
    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo")
        self.__id = id
    def set_data(self, data):
        if not isinstance(data, datetime): raise ValueError("Data inválida")
        self.__data = data
    def set_distancia(self, distancia):
        if distancia <= 0: raise ValueError("Distância deve ser positiva")
        self.__distancia = distancia
    def set_tempo(self, tempo):
        if not isinstance(tempo, timedelta): raise ValueError("Tempo inválido")
        self.__tempo = tempo
    def get_id(self): return self.__id    
    def get_data(self): return self.__data    
    def get_distancia(self): return self.__distancia    
    def get_tempo(self): return self.__tempo    
    def __str__(self):
        return f"{self.__id} - {self.__data} - {self.__distancia} - {self.__tempo} - "
    def pace(self):
        pace = self.__tempo/self.__distancia
        return self.pace

#x = Paciente(1, "Eduardo", "09808909812", "84900090909", datetime(1990, 10, 5))
#print(x)
#print(x.idade())    
class PacienteUI:
    __pacientes = []  # atributo - fora do init - não tem objetos de PacienteUI
    @staticmethod     # quando não acessa o atributo
    def main():
        op = 0
        while op != 9:
            op = PacienteUI.menu()
            if op == 1: PacienteUI.inserir()
            if op == 2: PacienteUI.listar()
            if op == 3: PacienteUI.atualizar()
            if op == 4: PacienteUI.excluir()
            if op == 5: PacienteUI.pesquisar()
            if op == 6: PacienteUI.aniversariantes() 

    @staticmethod
    def menu():
        print("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir, 5-Pesquisar, 6-Aniversariantes, 9-Fim")
        return int(input("Escolha uma opção: "))
    
    @classmethod      # quando acessa o atributo - usa o cls
    def inserir(cls):
        id = int(input("Informe o id: "))
        nome = input("Informe o nome: ")
        cpf = input("Informe o cpf: ")
        fone = input("Informe o telefone: ")
        nasc = datetime.strptime(input("Informe a data de nascimento dd/mm/aaaa: "), "%d/%m/%Y")
        x = Treino(id, nome, cpf, fone, nasc)
        cls.__pacientes.append(x)

    @classmethod
    def listar(cls):
        if len(cls.__pacientes) == 0: print("Nenhum paciente cadastrado")
        else:
            for x in cls.__pacientes: print(x, x.idade())

    @classmethod
    def atualizar(cls):
               for x in cls.__pacientes:
                id = int(input("Informe o id do paciente a ser atualizado: "))
                if x.get_id() == id:
                    nome = input("Informe o novo nome: ")
                    cpf = input("Informe o novo cpf: ")
                    fone = input("Informe o novo telefone: ")
                    nasc = datetime.strptime(input("Informe a nova data de nascimento dd/mm/aaaa: "), "%d/%m/%Y")
                    x.set_nome(nome)
                    x.set_cpf(cpf)
                    x.set_fone(fone)
                    x.set_nascimento(nasc)