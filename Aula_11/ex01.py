class Time:
    def __init__(self, id, nome, estado):
        self.set_id(id)
        self.set_nome(nome)
        self.set_estado(estado)
    def set_id(self,id):
        if id<0: raise ValueError("Id deve ser positivo")
        self.__id = id
    def set_nome(self,nome):
        if nome =="": raise ValueError("Nome não pode ser vazio")
        self.__nome = nome
    def set_estado(self,estado): 
        if estado =="": raise ValueError("Estado não pode ser vazio")
        self.__estado = estado
        