from models.restaurante import Restaurante
from models.cardapio.bebida import Bebida
from models.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de Melancia', 5.0, 'grande')
bebida_suco.aplicar_desconto()
prato_lanche = Prato('Misto-quente', 12.0, 'Pão, queijo e presunto')
prato_lanche.aplicar_desconto()
restaurante_praca.adicionar_itens_no_cardapio(bebida_suco)
restaurante_praca.adicionar_itens_no_cardapio(prato_lanche)


def main():
    restaurante_praca.exibir_cardapio


if __name__ == '__main__':
    main()