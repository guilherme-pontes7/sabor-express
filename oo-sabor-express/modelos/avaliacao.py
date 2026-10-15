class Avaliacao:
    """Nota de 1 a 5 dada por um cliente."""

    def __init__(self, cliente, nota):
        self._cliente = cliente
        self._nota = nota

    @property
    def estrelas(self):
        return '\u2b50\ufe0f' * self._nota

    def __str__(self):
        return f'{self._cliente}: {self._nota} de 5 {self.estrelas}'

    def para_dict(self):
        return {'cliente': self._cliente, 'nota': self._nota, 'texto': str(self)}
