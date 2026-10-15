from modelos.cardapio.item_cardapio import ItemCardapio


class Sobremesa(ItemCardapio):
    CAMPOS = ('subtipo', 'tamanho', 'descricao')

    def __init__(self, nome, preco, tipo, tamanho, descricao):
        super().__init__(nome, preco)
        self.subtipo = tipo
        self.tamanho = tamanho
        self.descricao = descricao

    def detalhe(self):
        return ' · '.join(x for x in (self.subtipo, self.tamanho, self.descricao) if x)
