#init
class PlayList:
    def __init__(self, id, nome, descricao):
        self.set_id(id)
        self.set_nome(nome)
        self.set_descricao(descricao)
    def set_id(self, id):
        if id<0: raise ValueError('O ID deve ser positivo')
        self.__id = id
    def set_nome(self, nome):
        if len(nome) == 0: raise ValueError('O nome não pode ser vazio')
        self.__nome = nome
    def set_descricao(self, descricao):
        if len(descricao) == 0: raise ValueError()
        self.__descricao = descricao
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_descricao(self): return self.__descricao
    def __str__(self):
        return f" Id: {self.__id} | Nome da Playlist: {self.__nome} | Descrição: {self.__descricao} "
    
class Musica:
    def __init__(self, id, titulo, artista, album):
        self.set_id(id)
        self.set_titulo(titulo)
        self.set_artista(artista)
        self.set_album(album)
    def set_id(self, id):
        if id<0: raise ValueError("O ID deve ser positivo")
        self.__id = id
    def set_titulo(self, titulo):
        if len(titulo) == 0: raise ValueError()
        self.__titulo = titulo
    def set_artista(self, artista):
        if len(artista) == 0: raise ValueError()
        self.__artista = artista
    def set_album(self, album):
        if album == '': raise ValueError()
        self.__album = album
    def get_id(self): return self.__id
    def get_titulo(self): return self.__titulo
    def get_artista(self): return self.__artista
    def get_album(self): return self.__album
    def __str__(self):
        return f" Id: {self.__id} | ITítulo: {self.__titulo} | Artista: {self.__artista} | Álbum: {self.__album} "

class PlayListItem:
    def __init__(self, id, idPlayList, idMusica, sequencia):
        self.set_id(id)
        self.set_idPlayList(idPlayList)
        self.set_idMusica(idMusica)
        self.set_sequencia(sequencia)
    def set_id(self, id):
        if id<0: raise ValueError('O ID deve ser positivo')
        self.__id = id
    def set_idPlayList(self, idPlayList):
        if idPlayList<0: raise ValueError('O ID deve ser positivo')
        self.__idPlayList = idPlayList
    def set_idMusica(self, idMusica):
        if idMusica<0: raise ValueError('O ID deve ser positivo')
        self.__idMusica = idMusica
    def set_sequencia(self, sequencia):
        if sequencia < 0: raise ValueError()
        self.__sequencia = sequencia
    def get_id(self): return self.__id
    def get_idPlayList(self): return self.__idPlayList
    def get_idMusica(self): return self.__idMusica
    def get_sequencia(self): return self.__sequencia
    def __str__(self):
        return f" Id: {self.__id} | Id da Playlist: {self.__idPlayList} | Id da Música: {self.__idMusica} | Sequência: {self.__sequencia} "

class UI:
    #listas
    playlists = []
    musicas = []
    itens = []

    @staticmethod
    def main():
        op = -1
        while op !=0:
            op = UI.menu()
            if op == 1: UI.inserir_playlist()
            if op == 2: UI.listar_playlists()
            if op == 3: UI.atualizar_playlist()
            if op == 4: UI.excluir_playlist()
            if op == 5: UI.inserir_musica()
            if op == 6: UI.listar_musicas()
            if op == 7: UI.atualizar_musica()
            if op == 8: UI.excluir_musica()
            if op == 9: UI.listar_musica_playlist()
            if op == 10: UI.transferir()
            if op == 11: UI.inserir_item()
            if op == 12: UI.listar_itens()
        print('Programa Encerrado. Volte sempre :)')
    
    @staticmethod
    def menu():
        print('1 - Inserir Playlist')
        print('2 - Listar Playlists')
        print('3 - Atualizar Playlist')
        print('4 - Excluir Playlist')
        print('5 - Inserir Musica')
        print('6 - Listar Musicas')
        print('7 - Atualizar Musica')
        print('8 - Excluir Musica')
        print('9 - Listar Musicas de uma Playlist')
        print('10 - Transferir Musica')
        print('11 - Adicionar Item')
        print('12 - Listar Itens')
        print('0 - Sair')
        return int(input('Escolha: '))

    @classmethod
    def inserir_playlist(cls):
        id = int(input("Id da Playlist: "))
        nome = input("Nome da Playlist: ")
        descricao = input("Descrição da Playlist: ")

        x = PlayList(id, nome, descricao) 
        cls.playlists.append(x) 
        print('Playlist Adicionada!')

    @classmethod
    def listar_playlists(cls):
        if len(cls.playlists) == 0:
            print("Não há playlists cadastradas ")
        for x in cls.playlists:
            print (x)
    
    @classmethod
    def atualizar_playlist(cls):
        id = int(input("Id da Playlist: "))
        for x in cls.playlists:
            if x.get_id == id:
                nome_novo = input("Novo nome da playlist: ")
                descricao_nova = ("Nova descrição da playlist: ")
                x.set_nome(nome_novo)
                x.set_descricao(descricao_nova)
                print("Playlist Atualizada!")

    @classmethod
    def excluir_playlist(cls):
        id = int(input("Id da Playlist: "))
        for x in cls.playlists:
            if x.get_id == id:
                cls.playlists.remove(x)

                for item in cls.itens[:]:
                    if item.get_idPlayList == id:
                        cls.itens.remove(item)
                print("Playlist Removida!")

    @classmethod
    def inserir_musica(cls):
        id = int(input("Id da Música: "))
        titulo = input("Título: ")
        artista = input("Artista: ")
        album = input("Álbum: ")

        x = Musica(id, titulo, artista, album) 
        cls.musicas.append(x) 
        print('Música Adicionada!')

    @classmethod
    def listar_musicas(cls):
        if len(cls.musicas) == 0:
            print("Não há músicas cadastradas ")
        for x in cls.musicas:
            print (x)

    @classmethod
    def atualizar_musica(cls):
        id = int(input("Id da Música: "))
        for x in cls.musicas:
            if x.get_id == id:
                novo_titulo = input('Novo Título: ')
                novo_artista = input('Novo Artista: ')
                novo_album = input('Novo Álbum: ')
                x.set_titulo(novo_titulo)
                x.set_artista(novo_artista)
                x.set_album(novo_album)
                print("Música Atualizada!")

    @classmethod
    def excluir_musica(cls):
        id = int(input("Id da Música: "))
        if len(cls.musicas) == 0:
            print("Não há músicas cadastradas.")
        for x in cls.musicas:
            if x.get_id == id:
                cls.musicas.remove(x)

                for item in cls.itens:
                    if item.get_idMusica() == id:
                        cls.itens.remove(item)
                print('Música Removida!')

    @classmethod
    def listar_musica_playlist(cls):
        id = int(input('ID da Playlist: '))

        for x in cls.musicas:
            if x.get_idPlaylist() == id:
                print(x)
    
    @classmethod
    def transferir(cls):
        id = int(input("Id da Música: "))
        nova_playlist = int(input("Id da Playlist para qual a música será transferida: "))
        for item in cls.itens:
            if item.get_idMusica() == id:
                item.set_idPlayList(nova_playlist)
                print("Música Transferida! ")
    
    @classmethod
    def inserir_item(cls):
        id = int(input("Id do Item: "))
        idPlayList = int(input("Id da Playlist: "))
        idMusica = int(input("Id da Música: "))
        sequencia = int(input("Sequência: "))

        x = PlayListItem(id, idPlayList, idMusica, sequencia)
        cls.itens.append(x)
        print("Item Adicionado!")

    @classmethod
    def listar_itens(cls):
        if len(cls.itens) == 0:
            print("Não há itens cadastrados ")
        else:
            for x in cls.itens:
                print(x)

UI.main()
