# Desafio Técnico - Processamento de Arquivos com Python

Este projeto contém três scripts em Python que processam um arquivo de entrada com dados de usuários, realizando as seguintes operações:

1. Identificar o usuário com o maior ou menor tamanho de "inbox" (`size`).

como usar:


Para encontrar o usuário com o maior tamanho:

python3 max_min_size.py input


Para encontrar o usuário com o menor tamanho:

python3 max_min_size.py input -min


2. Ordenar os usuários por nome de e-mail.


Para ordenar os usuários em ordem alfabética crescente:

python3 order_by_username.py input | head -n 3


Para ordenar os usuários em ordem decrescente:

python3 order_by_username.py input -desc | head -n 3


3. Identificar os usuários que estão em uma faixa específica de mensagens.


Para encontrar usuários com uma quantidade de mensagens entre 50 e 200:

python3 between_msgs.py input 50 200



## Requisitos

- **Python 3**: Certifique-se de que você tem o Python 3 instalado e certifique-se de testar todos os arquivos em um ambiente linux.
  
  Para verificar, execute:
  ```bash
  python3 --version
