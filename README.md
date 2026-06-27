# VendaMais

## Descrição do Projeto

O objetivo deste projeto é criar uma Plataforma de Inteligência Operacional que automatize a extração de dados do ERP da VendaMais. Esses dados serão armazenados em um ambiente centralizado na nuvem e passarão por tratamentos para garantir qualidade, consistência e confiabilidade.

A plataforma também irá disponibilizar dashboards interativos, facilitando o acesso às informações e apoiando a análise dos principais indicadores pelas áreas de negócio.

Ao final, a VendaMais poderá acompanhar seus indicadores operacionais com uma defasagem máxima de 24 horas em relação aos dados de origem, sem a necessidade de processos manuais.

## Integrantes

- https://github.com/carlitosxsx 
- https://github.com/julianaseemann
- https://github.com/lorenzoponcio
- https://github.com/matheusmotta7777

## Estrutura do Repositório
```text
DAS-VENDAMAIS
├── docs
│   ├── adr
│   │   ├── ADR-001.md
│   │   ├── ADR-002.md
│   │   └── ADR-003.md
│   ├── c4
│   │   ├── imgs
│   │   ├── 01-context.md
│   │   └── 02-container.md
│   ├── pesquisa
│   │   ├── psycopg2.md
│   │   ├── pymssql.md
│   │   ├── pyodbc.md
│   │   └── sqlalchemy.md
│   ├── das2b-vendamais.pbix
│   └── image.png
├── src
│   └── triggers
│       ├── __init__.py
│       ├── extract_categoria_produto.py
│       ├── extract_cliente.py
│       ├── extract_entrega.py
│       ├── extract_estoque_movimentacao.py
│       ├── extract_estoque_saldo.py
│       ├── extract_estoque.py
│       ├── extract_pedido_item.py
│       ├── extract_pedido.py
│       ├── extract_produto.py
│       ├── extract_regiao.py
│       ├── extract_representante.py
│       ├── extract_titulo_receber.py
│       ├── extract_transportadora.py
│       ├── poc_psycopg2.py
│       ├── poc_pymssql.py
│       └── poc_sqlalchemy.py
├── .funcignore
├── .gitignore
├── function_app.py
├── host.json
├── requirements.txt
└── README.md
```

## Dashboard

Visualização de dados e indicadores do VendaMais

![alt text](image.png)