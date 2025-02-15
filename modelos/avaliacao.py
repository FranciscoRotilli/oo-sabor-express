class Avaliacao:
    '''
    Representa uma avaliação feita por um cliente.
    
    Parâmetros:
    - cliente: str -> Nome do cliente que fez a avaliação.
    - nota: float -> Nota atribuída pelo cliente.
    '''
    def __init__(self, cliente, nota):
        self._cliente = cliente
        self._nota = nota