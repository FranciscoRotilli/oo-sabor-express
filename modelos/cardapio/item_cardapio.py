from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    '''
    Representa um item do cardápio

    Atributos:
    - nome: str -> Nome do item.
    - preco: float -> Preço do item.
    '''
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    @abstractmethod
    def aplicar_desconto(self, desconto):
        pass