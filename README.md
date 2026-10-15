## Sabor Express

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

## Tecnologias

![Python](https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/-FastAPI-009688?style=flat&logo=fastapi&logoColor=white)
![JSON](https://img.shields.io/badge/-JSON-000000?style=flat&logo=json&logoColor=white)


## Demo online

Link para acessar pelo navegador: https://sabor-express-seven.vercel.app

# Time

 [<img loading="lazy" src="https://avatars.githubusercontent.com/u/326724504?s=400&u=d2becdccc4d6dc7ba1fb8b17d25184ec147d26eb&v=4" width=115><br><sub>Guilherme Pontes</sub>](https://github.com/guilherme-pontes7)

