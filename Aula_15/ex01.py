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
      
class TreinoUI:
    __treinos = [] 
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = TreinoUI.menu()
            if op == 1: TreinoUI.inserir()
            if op == 2: TreinoUI.listar()
            if op == 3: TreinoUI.listar_id()
            if op == 4: TreinoUI.atualizar()
            if op == 5: TreinoUI.excluir()
            if op == 6: TreinoUI.mais_rapido() 

    @staticmethod
    def menu():
        print("1-Inserir, 2-Listar, 3-Listar ID, 4- Atualizar, 5-Excluir, 6-Mais Rápido, 9-Fim")
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
            for x in cls.__pacientes: print(x)

    @classmethod
    def listar_id(cls):
        if len(cls.__treinos) == 0: print("Nenhum treino cadastrado")
        else:
            for x in cls.__treinos: print(x)

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

    @classmethod
    def excluir(cls):
        pass

    @classmethod
    def mais_rapido(cls):
        pass
