from abc import ABC, abstractmethod


class ItemCardapio(ABC):
    CAMPOS = ()  # campos extras de cada tipo de item

    def __init__(self, nome, preco):
        self._nome = nome
        self._preco_original = float(preco)
        self._desconto = 0.0

    @property
    def nome(self):
        return self._nome

    @property
    def desconto(self):
        return self._desconto

    @property
    def preco(self):
        return round(self._preco_original * (1 - self._desconto / 100), 2)

    def aplicar_desconto(self, percentual):
        """Define o desconto (em %) escolhido pela loja. Use 0 para remover."""
        percentual = float(percentual)
        if not 0 <= percentual < 100:
            raise ValueError('O desconto deve ficar entre 0 e 99,99%.')
        self._desconto = percentual

    @abstractmethod
    def detalhe(self):
        """Texto que descreve o item (cada tipo monta o seu)."""

    def para_dict(self):
        extras = {campo: getattr(self, campo) for campo in self.CAMPOS}
        return {'tipo': type(self).__name__, 'nome': self._nome,
                'preco_original': self._preco_original, 'preco': self.preco,
                'desconto': self._desconto, 'detalhe': self.detalhe(), **extras}

    def __str__(self):
        return self._nome
