from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')

restaurante_praca.receber_avaliacao('João', 4)
restaurante_praca.receber_avaliacao('Maria', 3)
restaurante_praca.receber_avaliacao('José', 5)
restaurante_praca.receber_avaliacao('Felipe', 5)
restaurante_praca.receber_avaliacao('Tamara', 5)
restaurante_praca.receber_avaliacao('Camila', 5)
restaurante_praca.receber_avaliacao('Gabriel', 5)


def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()