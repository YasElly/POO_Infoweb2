from models.cliente import Cliente
from models.clientedao import ClienteDAO

from models.servico import Servico
from models.servicodao import ServicoDAO

from models.profissional import Profissional
from models.profissionaldao import ProfissionalDAO


class Service:

    __clienteDAO = ClienteDAO()
    __servicoDAO = ServicoDAO()
    __profissionalDAO = ProfissionalDAO()

    #CLIENTE
    @staticmethod
    def cliente_inserir(nome, email, fone, senha):
        obj = Cliente(1, nome, email, fone, senha)
        Service.__clienteDAO.inserir(obj)

    @staticmethod
    def cliente_listar():
        return Service.__clienteDAO.listar()

    @staticmethod
    def cliente_listar_id(id):
        return Service.__clienteDAO.listar_id(id)
    
    @staticmethod
    def cliente_listar_nome(nome):
        return Service.__clienteDAO.listar_nome(nome)

    @staticmethod
    def cliente_atualizar(id, nome, email, fone, senha):
        obj = Cliente(id, nome, email, fone, senha)
        Service.__clienteDAO.atualizar(obj)

    @staticmethod
    def cliente_excluir(id):
        Service.__clienteDAO.excluir(id)

    #SERVICO
    @staticmethod
    def servico_inserir(descricao, valor):
        obj = Servico(1, descricao, valor)
        Service.__servicoDAO.inserir(obj)

    @staticmethod
    def servico_listar():
        return Service.__servicoDAO.listar()

    @staticmethod
    def servico_listar_id(id):
        return Service.__servicoDAO.listar_id(id)

    @staticmethod
    def servico_listar_descricao(descricao):
        return Service.__servicoDAO.listar_descricao(descricao)

    @staticmethod
    def servico_atualizar(id, descricao, valor):
        obj = Servico(id, descricao, valor)
        Service.__servicoDAO.atualizar(obj)

    @staticmethod
    def servico_excluir(id):
        Service.__servicoDAO.excluir(id)

    #PROFISSIONAL
    @staticmethod
    def profissional_inserir(nome, email, senha, especialidade):
        obj = Profissional(1, nome, email, senha, especialidade)
        Service.__profissionalDAO.inserir(obj)

    @staticmethod
    def profissional_listar():
        return Service.__profissionalDAO.listar()

    @staticmethod
    def profissional_listar_id(id):
        return Service.__profissionalDAO.listar_id(id)

    @staticmethod
    def profissional_listar_nome(nome):
        return Service.__profissionalDAO.listar_nome(nome)

    @staticmethod
    def profissional_atualizar(id, nome, email, senha, especialidade):
        obj = Profissional(id, nome, email, senha, especialidade)
        Service.__profissionalDAO.atualizar(obj)

    @staticmethod
    def profissional_excluir(id):
        Service.__profissionalDAO.excluir(id)