from modelos.avaliacao import Avaliacao

class Restaurante:
    '''Representa um restaurante e suas características.'''
    restaurantes = []

    def __init__(self, nome, categoria):
        '''
        Construtor da classe Restaurante.

        Parâmetros:
        - nome: str -> Nome do restaurante.
        - categoria: str -> Categoria do restaurante.
        '''
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        '''Retorna uma representação em string do objeto Restaurante.'''
        return f'Restaurante {self._nome} - {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        '''Exibe uma lista com os restaurantes cadastrados.'''
        print(f'{"Nome".ljust(25)} | {"Categoria".ljust(25)} | {"Avaliação".ljust(25)} | Status')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        '''Retorna um emoji correspondente ao status do restaurante.'''
        return '✅' if self._ativo else '❌'

    def alternar_status(self):
        '''Alterna o status do restaurante antre ativo e inativo.'''
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        '''
        Registra uma avaliação para o restaurante.

        Parâmetros:
        - cliente: str -> Nome do cliente que fez a avaliação.
        - nota: float -> Nota atribuída ao restaurante. (Entre 0 e 5)
        '''
        if 0 <= nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        '''Calcula e retorna a média das avaliações do restaurante.'''
        return round(sum([avaliacao._nota for avaliacao in self._avaliacao]) / len(self._avaliacao), 1) if self._avaliacao else 'Sem Avaliações'