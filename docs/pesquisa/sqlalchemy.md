# SQL Alchemy

# O que é a biblioteca SQLAlchemy?

A **SQLAlchemy** é uma biblioteca Python descrita oficialmente como:

> “O Kit de Ferramentas SQL de Python e o Mapeador Relacional de Objetos”

A biblioteca fornece recursos para:

- conexão com bancos de dados;
- execução de comandos SQL;
- construção programática de consultas;
- mapeamento objeto-relacional (ORM).

Segundo a documentação oficial, a SQLAlchemy é dividida principalmente em duas partes:

- SQLAlchemy Core
- SQLAlchemy ORM

---

# Desenvolvimento

## 1. Qual é o objetivo principal da biblioteca?

O principal objetivo da SQLAlchemy é permitir que aplicações Python consigam:

- conectar-se a bancos de dados relacionais;
- executar comandos SQL;
- mapear objetos Python para tabelas do banco;
- realizar consultas utilizando ORM;
- gerenciar persistência de dados.

A documentação oficial informa que a biblioteca oferece ferramentas para trabalhar tanto com SQL tradicional quanto com programação orientada a objetos.

---

## 2. Que tipo de banco de dados ela permite acessar?

Nos materiais pesquisados, foi possível identificar que a SQLAlchemy trabalha com bancos de dados relacionais através de “dialects”.

A documentação menciona suporte a diferentes backends relacionais utilizando engines e dialetos específicos.

Portanto, com base apenas nas referências fornecidas, a SQLAlchemy é indicada para bancos de dados relacionais.

---

## 3. Ela é mais indicada para bancos relacionais ou não relacionais?

A SQLAlchemy é indicada para bancos relacionais.

A biblioteca foi desenvolvida para trabalhar com:
- tabelas;
- relacionamentos;
- consultas SQL;
- mapeamento objeto-relacional.

### Suporte a Bancos Não Relacionais

Nos materiais fornecidos não foi encontrada uma explicação oficial sobre suporte a bancos não relacionais (NoSQL).

Portanto, com base apenas nas referências utilizadas, foi possível identificar apenas suporte para bancos relacionais.

---

## 4. A biblioteca trabalha com SQL puro, ORM ou ambos?

Segundo a documentação oficial, a SQLAlchemy possui suporte tanto para SQL quanto para ORM.

A documentação divide a biblioteca em:

### SQLAlchemy Core

Responsável por:

- construção de comandos SQL;
- gerenciamento de conexões;
- execução de queries.

### SQLAlchemy ORM

Responsável por:

- mapear classes Python para tabelas;
- persistência de objetos;
- consultas orientadas a objetos.

Portanto, a SQLAlchemy trabalha com:

- SQL puro;
- ORM.

---

# O que é ORM?

ORM (Object Relational Mapping), ou Mapeamento Objeto-Relacional, é uma técnica utilizada para aproximar aplicações orientadas a objetos de bancos de dados relacionais.

As ORMs:
- convertem tabelas em objetos;
- geram consultas SQL automaticamente;
- facilitam o desenvolvimento;
- aumentam a produtividade.

Na SQLAlchemy, a ORM permite que tabelas do banco sejam representadas por classes Python.

---

# Vantagens da SQLAlchemy

Com base nos materiais pesquisados, foi possível identificar:

- suporte a SQL e ORM;
- flexibilidade de utilização;
- arquitetura dividida entre Core e ORM;
- integração com aplicações Python;
- construção avançada de consultas;
- modularização do código;
- suporte a consultas programáticas.

---

# Desvantagens da SQLAlchemy

Nos materiais analisados não foram encontradas desvantagens explícitas oficialmente documentadas.

Entretanto, foi possível observar que:
- a biblioteca possui maior complexidade;
- exige conhecimento de ORM;
- possui sintaxe mais avançada em comparação com bibliotecas simples de acesso direto.

---

# Padrão ORM Utilizado

A SQLAlchemy utiliza principalmente o padrão:

## Data Mapper

Características:
- separação entre entidades e acesso ao banco;
- maior modularização;
- código mais organizado;
- recomendado para aplicações maiores e mais complexas.

---

# Comparação entre SQLAlchemy ORM e SQL puro

| Aspecto | SQL Puro | SQLAlchemy ORM |
|---|---|---|
| Escrita manual de SQL | Sim | Não obrigatória |
| Mapeamento de objetos | Não | Sim |
| Complexidade | Menor inicialmente | Maior |
| Produtividade | Menor | Maior |
| Modularização | Menor | Maior |

---

## 5. Como é feita a instalação?

Nos materiais fornecidos foi encontrada referência à seção de instalação da documentação oficial.

### Exemplo

```bash
pip install SQLAlchemy
```

---

## 6. Como é criado um exemplo simples de conexão?

A documentação oficial apresenta exemplos utilizando `create_engine()`.

### Exemplo

```python
from sqlalchemy import create_engine

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
```

Nesse exemplo:

- `create_engine()` cria a conexão com o banco;
- `sqlite+pysqlite` representa o dialeto utilizado;
- `:memory:` cria um banco SQLite em memória;
- `echo=True` exibe os comandos SQL executados.

---

## 7. Como executar uma consulta `SELECT` simples?

A documentação oficial apresenta consultas utilizando `select()`.

### Exemplo

```python
from sqlalchemy import select

stmt = select(User).where(User.name == "spongebob")
```

Nesse exemplo:

- `select()` cria uma consulta SQL;
- `where()` adiciona uma condição;
- `User` representa uma classe mapeada pelo ORM.

---

# Exemplo de Modelo ORM

A documentação oficial também apresenta exemplos de definição de modelos ORM.

## Exemplo

```python
class User(Base):
    __tablename__ = "user_account"
```

Nesse exemplo:

- `User` representa uma entidade da aplicação;
- `__tablename__` define o nome da tabela no banco.

---

# Características da SQLAlchemy

Durante a pesquisa foi possível identificar algumas características da biblioteca:

- suporte a SQL;
- suporte a ORM;
- construção programática de consultas;
- gerenciamento de conexões;
- mapeamento objeto-relacional;
- integração com aplicações Python.

---

# Limitações da Pesquisa

Como solicitado, este trabalho foi produzido apenas com base nas informações presentes nos links fornecidos.

Por esse motivo, algumas informações não foram encontradas oficialmente nos materiais analisados:

- lista completa de bancos suportados;
- limitações técnicas oficiais;
- comparação detalhada com outras bibliotecas;
- análise de desempenho;
- cenários avançados de uso.

---

# Conclusão

A biblioteca SQLAlchemy é uma solução utilizada para conectar aplicações Python a bancos de dados relacionais. Sua principal função é permitir a execução de comandos SQL e o uso de ORM dentro de aplicações Python.

Durante a pesquisa foi possível observar que a biblioteca oferece uma arquitetura dividida entre Core e ORM, permitindo diferentes formas de interação com bancos de dados.

Os exemplos encontrados na documentação oficial demonstram recursos para criação de conexões, consultas SQL e definição de modelos ORM.

Apesar de algumas informações mais avançadas não terem sido encontradas explicitamente nos materiais fornecidos, foi possível identificar que a SQLAlchemy é uma biblioteca bastante completa para desenvolvimento de aplicações Python com persistência de dados.

---

# Referências

## Repositórios e Documentações

- https://github.com/sqlalchemy/sqlalchemy

- https://www.sqlalchemy.org/