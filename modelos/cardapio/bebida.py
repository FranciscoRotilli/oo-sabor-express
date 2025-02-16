from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    '''
    Representa uma bebida do cardápio.
    
    Atributos:
    - nome: str -> Nome da bebida.
    - preco: float -> Preço da bebida.
    - tamanho: str -> Tamanho da bebida.
    '''
    def __init__(self, nome, preco, tamanho):
        '''Método construtor da classe Bebida.'''
        super().__init__(nome, preco)
        self._tamanho = tamanho

    def __str__(self):
        '''Retorna uma representação em string do objeto Bebida.'''
        return f'Bebida: {self._nome} - R$ {self._preco} - {self._tamanho}'
    
    def aplicar_desconto(self):
        '''Aplica um desconto de 8% no preço da bebida.'''
        self._preco -= (self._preco * 0.08)