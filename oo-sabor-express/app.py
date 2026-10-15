"""Sabor Express: servidor local (só biblioteca padrão do Python 3).

    python app.py              abre o site em http://localhost:8000
    python app.py --terminal   mostra o exemplo no terminal
"""
import json
import os
import sys
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from modelos.restaurante import Restaurante, criar_item

PASTA = os.path.dirname(os.path.abspath(__file__))
ARQUIVO = os.path.join(PASTA, 'dados.json')
PORTA = int(os.environ.get('PORT', 8000))


def exemplo():
    Restaurante.restaurantes.clear()
    r = Restaurante('praça', 'Gourmet')
    r.adicionar_no_cardapio(criar_item({'tipo': 'Bebida', 'nome': 'Suco de laranja', 'preco_original': 5.0, 'tamanho': 'Grande', 'desconto': 8}))
    r.adicionar_no_cardapio(criar_item({'tipo': 'Prato', 'nome': 'Paozinho', 'preco_original': 2.0, 'descricao': 'O melhor pão da cidade', 'desconto': 5}))
    r.adicionar_no_cardapio(criar_item({'tipo': 'Sobremesa', 'subtipo': 'Gelado', 'nome': 'Sorvetao', 'preco_original': 15.0, 'tamanho': 'Grande', 'descricao': 'Um docinho gelato!', 'desconto': 2}))


def salvar():
    with open(ARQUIVO, 'w', encoding='utf-8') as f:
        json.dump([r.para_dict() for r in Restaurante.restaurantes], f, ensure_ascii=False, indent=2)


def carregar():
    Restaurante.restaurantes.clear()
    try:
        with open(ARQUIVO, encoding='utf-8') as f:
            for d in json.load(f):
                Restaurante.de_dict(d)
    except (FileNotFoundError, ValueError, KeyError):
        exemplo()


def lista():
    return [r.para_dict() for r in Restaurante.restaurantes]


def rota(metodo, caminho, corpo):
    """Trata a API. Cada ação que altera dados devolve a lista atualizada."""
    p = caminho.strip('/').split('/')[1:]
    if p == ['restaurantes'] and metodo == 'GET':
        return lista()
    if p == ['restaurantes'] and metodo == 'POST':
        if not corpo.get('nome', '').strip() or not corpo.get('categoria', '').strip():
            raise ValueError('Informe nome e categoria.')
        Restaurante(corpo['nome'].strip(), corpo['categoria'].strip())
    elif p == ['reset'] and metodo == 'POST':
        exemplo()
    elif len(p) >= 2 and p[0] == 'restaurantes':
        r = Restaurante.restaurantes[int(p[1])]
        resto = p[2:]
        if not resto and metodo == 'DELETE':
            Restaurante.restaurantes.remove(r)
        elif resto == ['alternar'] and metodo == 'POST':
            r.alternar_estado()
        elif resto == ['itens'] and metodo == 'POST':
            r.adicionar_no_cardapio(criar_item({**corpo, 'preco_original': corpo.get('preco')}))
        elif len(resto) == 2 and resto[0] == 'itens' and metodo == 'DELETE':
            r._cardapio.pop(int(resto[1]))
        elif len(resto) == 3 and resto[0] == 'itens' and resto[2] == 'desconto' and metodo == 'POST':
            r._cardapio[int(resto[1])].aplicar_desconto(corpo.get('percentual'))
        elif resto == ['avaliacoes'] and metodo == 'POST':
            if not r.receber_avaliacao(corpo.get('cliente', ''), corpo.get('nota')):
                raise ValueError('Informe o cliente e uma nota inteira de 1 a 5.')
        else:
            raise LookupError
    else:
        raise LookupError
    salvar()
    return lista()


class Handler(BaseHTTPRequestHandler):
    def responder(self, status, conteudo, tipo='application/json; charset=utf-8'):
        dados = conteudo if isinstance(conteudo, bytes) else json.dumps(conteudo, ensure_ascii=False).encode()
        self.send_response(status)
        self.send_header('Content-Type', tipo)
        self.send_header('Content-Length', str(len(dados)))
        self.end_headers()
        self.wfile.write(dados)

    def tratar(self, metodo):
        if metodo == 'GET' and not self.path.startswith('/api'):
            with open(os.path.join(PASTA, 'static', 'index.html'), 'rb') as f:
                return self.responder(200, f.read(), 'text/html; charset=utf-8')
        try:
            tam = int(self.headers.get('Content-Length', 0))
            corpo = json.loads(self.rfile.read(tam) or '{}')
            self.responder(200, rota(metodo, self.path.split('?')[0], corpo))
        except (ValueError, KeyError, TypeError) as e:
            self.responder(400, {'erro': str(e) or 'Dados inválidos.'})
        except (LookupError, IndexError):
            self.responder(404, {'erro': 'Não encontrado.'})

    def do_GET(self): self.tratar('GET')
    def do_POST(self): self.tratar('POST')
    def do_DELETE(self): self.tratar('DELETE')
    def log_message(self, *args): pass


if __name__ == '__main__':
    if '--terminal' in sys.argv:
        exemplo()
        Restaurante.listar_restaurantes()
        print()
        Restaurante.restaurantes[0].exibir_cardapio()
    else:
        carregar()
        servidor = ThreadingHTTPServer(('127.0.0.1', PORTA), Handler)
        url = f'http://localhost:{PORTA}'
        print(f'Sabor Express rodando em {url} (Ctrl+C para parar)')
        threading.Timer(0.5, lambda: webbrowser.open(url)).start()
        try:
            servidor.serve_forever()
        except KeyboardInterrupt:
            print('\nEncerrado.')
