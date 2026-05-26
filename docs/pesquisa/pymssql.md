# Pesquisa sobre a Biblioteca pymssql para Conexão com Banco de Dados PostgreSQL


# 1. Qual é o objetivo principal da biblioteca?

Segundo a documentação oficial, o `pymssql` é uma interface de banco de dados para Python construída sobre o FreeTDS, fornecendo uma implementação compatível com o padrão Python DB-API (PEP-249) para Microsoft SQL Server.

O principal objetivo da biblioteca é permitir que aplicações Python realizem comunicação com servidores Microsoft SQL Server. Essa comunicação inclui operações como:

- criação de conexões com o banco;
- execução de consultas SQL;
- inserção de registros;
- atualização de dados;
- remoção de informações;
- leitura de resultados retornados pelo banco.

A biblioteca atua como uma ponte entre o código Python e o servidor SQL Server, permitindo que aplicações automatizem tarefas de banco de dados.

---

# 2. Que tipo de banco de dados ela permite acessar?

A documentação informa que o `pymssql` permite acesso aos seguintes bancos de dados:

- Microsoft SQL Server
- Azure SQL Database

O SQL Server é um sistema gerenciador de banco de dados desenvolvido pela Microsoft e bastante utilizado em aplicações corporativas, sistemas empresariais e ambientes que utilizam tecnologias Microsoft.

Além disso, a documentação informa compatibilidade com Azure SQL Database, que é a versão em nuvem do SQL Server oferecida pela Microsoft Azure.

---

# 3. Ela é mais indicada para bancos relacionais ou não relacionais?

O material pesquisado mostra que a biblioteca foi criada especificamente para trabalhar com Microsoft SQL Server, que é um banco de dados relacional.

Bancos relacionais organizam dados em tabelas compostas por linhas e colunas, utilizando linguagem SQL para manipulação das informações.

Portanto, o `pymssql` é indicado para bancos relacionais.

Nos links fornecidos não foram encontradas informações sobre suporte a bancos não relacionais (NoSQL), como MongoDB, Redis ou Cassandra.

---

# 4. A biblioteca trabalha com SQL puro, ORM ou ambos?

A documentação apresenta exemplos utilizando comandos SQL diretamente através do método `cursor.execute()`. Isso mostra que o funcionamento principal da biblioteca é baseado em SQL puro.

Exemplo encontrado na documentação:

```python
cursor.execute('SELECT * FROM persons')
```

A documentação não apresenta funcionalidades próprias de ORM (Object Relational Mapping).

Com base apenas nas fontes pesquisadas:

- A biblioteca trabalha com SQL puro;
- Não foram encontradas informações sobre suporte ORM próprio nos links fornecidos.

---

# 5. Como é feita a instalação?

A instalação é realizada utilizando o gerenciador de pacotes `pip`, padrão do Python.

Comandos encontrados na documentação:

```bash
pip install -U pip
pip install pymssql
```

A documentação também informa que os pacotes oficiais distribuídos no PyPI incluem FreeTDS integrado nas wheels disponibilizadas para instalação.

O FreeTDS é uma biblioteca utilizada para realizar a comunicação entre o Python e o SQL Server.

Segundo a documentação, o `pymssql` possui suporte para múltiplos sistemas operacionais.

---

# 6. Como é criado um exemplo simples de conexão?

A documentação apresenta exemplos de criação de conexão utilizando a função `pymssql.connect()`.

Exemplo baseado na documentação oficial:

```python
import pymssql

conn = pymssql.connect(
    server='SERVIDOR',
    user='USUARIO',
    password='SENHA',
    database='BANCO'
)

cursor = conn.cursor()
```

Nesse exemplo:

- `server` representa o endereço do servidor SQL Server;
- `user` representa o usuário de acesso;
- `password` representa a senha;
- `database` representa o banco de dados utilizado.

Após a conexão, é criado um cursor com `conn.cursor()`, que será utilizado para executar comandos SQL.

---

# 7. Como executar uma consulta SELECT simples?

A documentação apresenta exemplos de execução de consultas SQL utilizando `cursor.execute()`.

Exemplo adaptado da documentação oficial:

```python
import pymssql

conn = pymssql.connect(
    server='SERVIDOR',
    user='USUARIO',
    password='SENHA',
    database='BANCO'
)

cursor = conn.cursor()

cursor.execute('SELECT * FROM persons')

for row in cursor:
    print(row)

conn.close()
```

Nesse exemplo:

1. É criada uma conexão com o banco;
2. Um cursor é criado;
3. O comando SQL `SELECT * FROM persons` é executado;
4. Os resultados são percorridos utilizando um `for`;
5. Cada linha retornada é exibida;
6. A conexão é encerrada com `conn.close()`.

A documentação também apresenta um exemplo utilizando parâmetros:

```python
cursor.execute(
    'SELECT * FROM persons WHERE salesrep=%s',
    'John Doe'
)
```

Esse modelo permite executar consultas utilizando filtros e parâmetros.

---

# Conclusão

O `pymssql` é uma biblioteca Python voltada para comunicação com Microsoft SQL Server e Azure SQL Database. A documentação mostra que a biblioteca utiliza SQL puro por meio da interface DB-API do Python, permitindo executar comandos SQL diretamente através de cursores.

A instalação é simples e realizada via `pip`, e os exemplos oficiais demonstram como criar conexões, executar consultas e manipular resultados retornados pelo banco de dados.

Além disso, a documentação destaca suporte para recursos importantes como Unicode, stored procedures, bulk copy e integração com Azure SQL Database, tornando a biblioteca adequada para aplicações que utilizam infraestrutura Microsoft SQL Server.


# Referências

## Repositórios e Documentações

- https://pymssql.readthedocs.io/en/stable/index.html
- https://github.com/pymssql/pymssql
