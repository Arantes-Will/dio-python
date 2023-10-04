## 💻 Conceitos Básicos e Estrutura do Banco de Dados Relacional

#### Tipo de Banco de Dados
- Relacionais / SQL
- Não Relacionais / NoSQL (Not OnlySQL)
- Orientado a Objetos
- Hierárquico

#### SGBD
Os sistemas de gerênciamento de banco de dados fornecem ferramentas e recursos para criar, manipular, consultar e administrar o banco de dados.
- C reate
- R ead
- U pdate
- D elete

## 💻 Introdução e Conceitos Básicos de SQL

#### SQL - Structured Query Language 
É uma linguagem de consulta padronizada para interação com o banco de dados
- DQL - Linguagem de consulta de Dados (SELECT) / Conseguimos recuperar uma informação
- DML - Linguagem de Manipulação de Dados (INSERT / UPDATE / DELETE) / Consultar, alterar e deletar informações
- DDL - Linguagem de Definiçao de Dados (CREATE / ALTER / DROP) / Estruturar como usamos a tabela
- DCL - Linguagem de Controle de Dados (GRANT / REVOKE) / Não é muito utilizado, permissionamentos que os usuários vão obter
- DTL - Linguagemd de Transação de Dados (BEGIN / COMMIT / ROLLBACK) / Garantimos a execução de propriedades

## 💻  MER e DER: Modelagem de Banco de Dados

#### MER e DER
O Modelo Entidade-Relacionamento (MER) é representado através de diagramas chamados Diagramas Entidade-Relacionamento (DER).

#### Entidade
As entidades são nomeadas com substantivos concretos ou abstratos que representem de forma clara sua função dentro do domínio.

#### Atributos
Os atributos são as caracteristicas e propriedades das entidades. Elas descrevem informações específicas sobre uma entidade.

Vamos utilizar como plataforma de estudo site https://app.creately.com/

#### Relacionamentos
Os relacionamentos representam as associações entre entidades

#### Cardinalidade
Se refere a forma como as nossas entidades se relacionam uma com as outras, indica o número máximo de instâncias que podemos ter numa entidade relacionada a outra entidade
- Relacionamento 1..1 (um para um)
- Relacionamento 1..n ou 1..* (um para muitos)
- Relacionamento n..n ou *..* (muitos para muitos)

Criando diagramas com IA: https://app.quickdatabasediagrams.com/#/

#### Configuração do Ambiente
https://accounts.cloudclusters.io/login/?next=https://clients.cloudclusters.io/

## 💻 Introdução a Banco de Dados Relacionais (SQL)

#### Tabelas
Ela é usada para armazenar dados de forma organizada. Cada tabela em um banco de dados relacional tem um nome único e é dividida em colunas e linhas.

#### Colunas
Uma coluna é uma estrutura dentro de uma tabela que representa um atributo específico dos dados armazenados. Cada coluna tem um nome único e um tipo de dados
associado que define o tipo de informação que pode ser armazenado nela, como número, textos, datas e etc.

#### Registros
Também conhecido como linha ou tupla, é uma instância individual de dados em uma tabela.

#### Comandos:
```
CREATE TABLE {{nome}}
  ({{coluna}} {{tipo}} {{opções}} COMMENT
{{´COMENTARIO`}});

```
Restrições de valor: 
- NOT NULL (Esta coluna é obrigatória?)
- UNIQUE (Garantimos que não terá outro registro igual)
- DEFAULT 
Chaves primárias e estrangeiras
Auto Incremento (De forma automática, auto implementamos informações)

#### Operações CRUD: 

##### CREATE

```
INSERT INTO
{{nome-tabela}}
([coluna1, coluna2, ...]) *** você pode ocultar as colunas
VALUES
([valor-coluna1,valor-coluna2,...])

```
##### READ

```
SELECT {{lista_colunas}}
FROM tabela;

Onde * retorna todas as colunas

SELECT {{lista_colunas}}
FROM tabela
WHERE {{condicao}} *** Com critério de seleção

```
- = (igualdade)
- <> ou != (desigualdade)
- > (maior que)
- < (menor que)
- >= (maior ou igual que)
- <= (menor ou igual que)
- LIKE (comparação de padrões)
- IN (pertence a uma lista de valores)
- BETWEEN (dentro de um intervalo)
- AND (e lógico)
- OR (ou lógico)



















