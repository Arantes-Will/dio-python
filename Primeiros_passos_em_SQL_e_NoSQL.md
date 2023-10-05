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
-  = (igualdade)
- '<>' ou != (desigualdade)
- '>' (maior que)
- '<' (menor que)
- '>=' (maior ou igual que)
- '<=' (menor ou igual que)
- LIKE (comparação de padrões)
- IN (pertence a uma lista de valores)
- BETWEEN (dentro de um intervalo)
- AND (e lógico)
- OR (ou lógico)

#### Exemplos
```
CREATE TABLE usuarios (
  id INT,
  nome VARCHAR(255) NOT NULL COMMENT 'Nome do usuário',
  email VARCHAR(255) NOT NULL UNIQUE COMMENT 'Endereço de e-mail do usuário',
  data_nascimento DATE NOT NULL COMMENT 'Data de nascimento do usuário',
  endereco VARCHAR(50) NOT NULL COMMENT 'Endereço do Cliente'
);

CREATE TABLE viagens.destinos (
  id INT,
  nome VARCHAR(255) NOT NULL UNIQUE COMMENT 'Nome do destino',
  descricao VARCHAR(255) NOT NULL COMMENT 'Descrição do destino'
);

CREATE TABLE viagens.reservas (
  id INT COMMENT 'Identificador único da reserva',
  id_usuario INT COMMENT 'Referência ao ID do usuário que fez a reserva',
  id_destino INT COMMENT 'Referência ao ID do destino da reserva',
  data DATE COMMENT 'Data da reserva',
  status VARCHAR(255) DEFAULT 'pendente' COMMENT 'Status da reserva (confirmada, pendente, cancelada, etc.)'
);

-- Inserts --
INSERT INTO viagens.usuarios (id, nome, email, data_nascimento, endereco) VALUES 
(1, 'João Silva', 'joao@example.com', '1990-05-15', 'Rua A, 123, Cidade X, Estado Y'),
(2, 'Maria Santos', 'maria@example.com', '1985-08-22', 'Rua B, 456, Cidade Y, Estado Z'),
(3, 'Pedro Souza', 'pedro@example.com', '1998-02-10', 'Avenida C, 789, Cidade X, Estado Y');

INSERT INTO viagens.destinos (id, nome, descricao) VALUES 
(1, 'Praia das Tartarugas', 'Uma bela praia com areias brancas e mar cristalino'),
(2, 'Cachoeira do Vale Verde', 'Uma cachoeira exuberante cercada por natureza'),
(3, 'Cidade Histórica de Pedra Alta', 'Uma cidade rica em história e arquitetura');

INSERT INTO viagens.reservas (id, id_usuario, id_destino, data, status) VALUES 
(1, 1, 2, '2023-07-10', 'confirmada'),
(2, 2, 1, '2023-08-05', 'pendente'),
(3, 3, 3, '2023-09-20', 'cancelada');

-- Selects --

-- Selecionar todos os registros da tabela "usuarios"
SELECT * FROM usuarios;

-- Selecionar apenas o nome e o email dos usuários
SELECT nome, email FROM usuarios;

-- Selecionar os usuários que possuem o nome "João Silva"
SELECT * FROM usuarios WHERE nome = 'João Silva';

-- Selecionar os usuários que nasceram antes de uma determinada data
SELECT * FROM usuarios WHERE data_nascimento < '1990-01-01';

-- Like
SELECT * FROM usuarios WHERE nome LIKE '%Silva%';
SELECT * FROM usuarios WHERE nome LIKE 'Jo_o%';

```
##### UPDATE

```
UPDATE {{tabela}}
SET *** Dentro dele que é inserido as colunas e os valores que vão ser atualizados dentro da nossa tabela
{{coluna1}} = {{novo_valor_1}},
{{coluna2}} = {{novo_valor_2}},
WHERE
{{condicao}}
```
##### DELETE

```
DELETE FROM
  {{tabela}}
WHERE
  {{condicao}};
```
#### Exemplos
```
-- Update --
UPDATE usuarios SET endereco = 'Nova Rua, 123' WHERE email = 'joao@example.com';

-- delete --
DELETE FROM reservas WHERE status = 'cancelada';

```

#### Alterando e Excluindo Tabelas

##### Drop Table
O comando DROP TABLE é usado no SQL - para remover uma tabela existente de um banco de dados relacional.
Ele exclui permanentemente a tabela
```
DROP TABLE {{tabela}}

```

##### Alter Table
A cláusula ALTER TABLE é usada no SQL para modificar a estrutura de uma tabela existente em um banco de dados relacional.

Ela permite:
-  Adicionar, alterar ou excluir colunas
- Modificar as restrições e índices
- Renomear a tabela, entre outras alterações

```
ALTER TABLE {{tabela}}

``` 
## 💻 Chaves Primárias e Estrangeiras


#### Chave Primária
A chave primária é um atributo ou um conjunto de atributos que identifica de forma exclusiva cada registro de nossa tabela, é responsavel por garantir a integridade
dos nossos dados, pois impede a duplicação de registros e ajuda na recuperação de informações.

```
CREATE TABLE {{tabela}}
(ID PRIMARY KEY AUTOINCREMENT, ...); *** Com o auto incremento o banco é responsavel pela criação dos IDS
ALTER TABLE {{tabela}}
MODIFY COLUMN ID INT PRIMARY KEY;

```

- Identifica exclusivamente
- Não pode conter valores nulos (NULL)
- Uma tabela pode ter apenas uma chave primária

#### Chave Estrangeira
É usada para estabelecer e manter a integridade dos dados entre tabelas relacionadas.
- Pode ser numa (NOT NULL); *** registro órfão
- É possível ter mais de uma (ou nenhuma) em uma tabela.

```
CREATE TABLE {{tabela}} (
id INT PRIMARY KEY,
chave_estrangeira INT,
FOREIGN KEY (chave_estrangeira) REFERENCES {{ outra tabela }} (id)
);

```

Caso precisarmos fazer uma alteração de tabela, ao invés de alterarmos uma coluna, vamos adicionar uma CONSTRAINT que são responsáveis por manter
a integridade referêncial dos nossos dados

```
ALTER TABLE {{tabela}}
ADD CONSTRAINT {{ nome_constraint }}
FOREIGN KEY (ID_)
REFERENCES {{outra_tabela}} (ID)

```

Restrições
- ON DELETE especifica o que acontece com os registros dependentes quando um registro pai é excluido
- ON UPDATE define o comportamento dos registros dependentes quando um registro pai é atualizado
- CASCADE, SET NULL, SET DEFAULT e RESTRICT
  























