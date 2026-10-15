from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.sobremesa import Sobremesa

TIPOS_ITEM = {'Prato': Prato, 'Bebida': Bebida, 'Sobremesa': Sobremesa}


def criar_item(dados):
    """Cria um Prato, Bebida ou Sobremesa a partir de um dicionário."""
    classe = TIPOS_ITEM[dados['tipo']]
    nome = str(dados['nome']).strip()
    preco = float(dados['preco_original'])
    if not nome or preco <= 0:
        raise ValueError('Informe um nome e um preço maior que zero.')
    item = classe(nome, preco, *[str(dados.get(c, '')).strip() for c in classe.CAMPOS])
    item.aplicar_desconto(dados.get('desconto') or 0)
    return item


class Restaurante:
    """Representa um restaurante e suas características."""

    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'

    @classmethod
    def listar_restaurantes(cls):
        print(f'{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Avaliação".ljust(25)} | Status')
        for r in cls.restaurantes:
            print(f'{r._nome.ljust(25)} | {r._categoria.ljust(25)} | {str(r.media_avaliacoes).ljust(25)} | {r.ativo}')

    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'

    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        """Registra uma avaliação (nota inteira de 1 a 5). Retorna False se for inválida."""
        try:
            nota = int(nota)
        except (TypeError, ValueError):
            return False
        if str(cliente).strip() and 1 <= nota <= 5:
            self._avaliacao.append(Avaliacao(str(cliente).strip(), nota))
            return True
        return False

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        notas = [a._nota for a in self._avaliacao]
        return round(sum(notas) / len(notas), 1)

    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)
            return True
        return False

    def exibir_cardapio(self):
        print(f'Cardápio do restaurante {self._nome}\n')
        for i, item in enumerate(self._cardapio, start=1):
            desc = f' (-{item.desconto:g}%)' if item.desconto else ''
            print(f'{i}. {item.nome} | R${item.preco:.2f}{desc} | {item.detalhe()}')

    def para_dict(self):
        return {'nome': self._nome, 'categoria': self._categoria, 'ativo': self._ativo,
                'media': self.media_avaliacoes,
                'avaliacoes': [a.para_dict() for a in self._avaliacao],
                'cardapio': [i.para_dict() for i in self._cardapio]}

    @classmethod
    def de_dict(cls, d):
        r = cls(d['nome'], d['categoria'])
        r._ativo = d.get('ativo', False)
        r._avaliacao = [Avaliacao(a['cliente'], a['nota']) for a in d.get('avaliacoes', [])]
        r._cardapio = [criar_item(i) for i in d.get('cardapio', [])]
        return r
