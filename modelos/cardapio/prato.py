from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    '''
    Representa um prato do cardápio.
    
    Atributos:
    - nome: str -> Nome do prato.
    - preco: float -> Preço do prato.
    - descricao: str -> Descrição do prato.
    '''
    def __init__(self, nome, preco, descricao):
        '''Método construtor da classe Prato.'''
        super().__init__(nome, preco)
        self._descricao = descricao

    def __str__(self):
        '''Retorna uma representação em string do objeto Prato.'''
        return f'Prato: {self._nome} - R$ {self._preco} - {self._descricao}'
    
    def aplicar_desconto(self):
        '''Aplica um desconto de 5% no preço do prato.'''
        self._preco -= (self._preco * 0.05)