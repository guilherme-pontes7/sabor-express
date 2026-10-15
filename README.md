# Sabor Express

Projeto de Programação Orientada a Objetos em Python: um sistema para gerenciar restaurantes, cardápios e avaliações.

## O que o projeto faz

- Cadastra restaurantes, ativa e desativa cada um e calcula a nota média.
- Monta o cardápio com pratos, bebidas e sobremesas.
- A loja define manualmente o desconto (em %) de cada item.
- Clientes avaliam de 1 a 5 e a avaliação aparece com estrelas, por exemplo `Pedro: 3 de 5 ⭐️⭐️⭐️`.

## Conceitos de POO usados

- **Classe abstrata:** `ItemCardapio` não pode ser instanciada.
- **Herança:** `Prato`, `Bebida` e `Sobremesa` herdam de `ItemCardapio`.
- **Polimorfismo:** cada tipo de item monta o próprio `detalhe()`.
- **Encapsulamento:** atributos privados e `@property` nas classes.

## Estrutura

    app.py            servidor local (biblioteca padrão do Python)
    modelos/          classes Restaurante, Avaliacao e itens do cardápio
    static/           interface usada pelo servidor local
    demo/index.html   versão estática (mesma lógica em JavaScript) para publicar online

## Rodando localmente (versão Python)

Requer Python 3.8 ou mais novo.

    python app.py

O site abre em http://localhost:8000. No Windows, também dá para dar dois cliques em `iniciar.bat`.
Para ver só o exemplo no terminal: `python app.py --terminal`.

## Demo online

A pasta `demo/` roda direto no navegador, sem servidor, e guarda os dados no próprio navegador do visitante.

