from modelos.cardapio.item_cardapio import ItemCardapio


class Bebida(ItemCardapio):
    CAMPOS = ('tamanho',)

    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self.tamanho = tamanho or 'Médio'

    def detalhe(self):
        return f'Tamanho: {self.tamanho}'
