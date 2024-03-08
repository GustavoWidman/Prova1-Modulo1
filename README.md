# Prova1-Modulo1 - Ponderada Gustavo Wagon Widman


## Descrição

Este projeto foi desenvolvido a partir da proposta entregue na prova 1 do modulo 1.

## Instalação e execução

Para instalar as dependências do projeto, comece clonando o repositório

```bash
git clone https://github.com/GustavoWidman/Prova1-Modulo1.git
```

Depois, entre na pasta do projeto, crie um ambiente virtual (venv) e ative-o.

```bash
cd Prova1-Modulo1 && python -m venv env && source env/bin/activate
```

Finalmente, instale as dependências do projeto com o comando:

```bash
pip install -r requirements.txt
```

Para rodar o projeto, execute:

```bash
python main.py
```

## Estrutura do projeto

A estrutura do projeto é composta por pastas e arquivos que organizam os comandos, classes e utilitários. Segue abaixo a estrutura do projeto, resultado do comando `tree --gitignore`

```bash
.
├── api
│   ├── __pycache__
│   └── router.py
├── caminhos.json
├── database
│   ├── main.py
│   └── __pycache__
├── index.html
├── main.py
├── README.md
└── requirements.txt
```