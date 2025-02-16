from modelos.cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    '''
    Representa uma sobremesa do cardápio.

    Atributos:
    - nome: str -> Nome da sobremesa.
    - preco: float -> Preço da sobremesa.
    - tamanho: str -> Tamanho da sobremesa.
    - descricao: str -> Descrição da sobremesa.
    - tipo: str -> Tipo da sobremesa.
    '''
    def __init__(self, nome, preco, tamanho, descricao, tipo):
        '''Método construtor da classe Sobremesa.'''
        super().__init__(nome, preco)
        self._tamanho = tamanho
        self._descricao = descricao
        self._tipo = tipo

    def __str__(self):
        '''Retorna uma representação em string do objeto Sobremesa.'''
        return f'Sobremesa: {self._nome} - R$ {self._preco} - {self._tamanho} - {self._descricao} - {self._tipo}'
    
    def aplicar_desconto(self):
        '''Aplica um desconto de 15% no preço da sobremesa.'''
        self._preco -= (self._preco * 0.15)