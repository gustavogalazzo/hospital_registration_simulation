# Projeto de Gerenciamento de Exames Médicos
Este repositório contém o código do nosso projeto de gerenciamento de exames médicos, desenvolvido em Python utilizando o framework SQLAlchemy ORM para mapeamento de tabelas no banco de dados SQLite. O projeto inclui funcionalidades para cadastrar médicos, pacientes, exames e consultar exames de pacientes específicos.

## Índice
- Descrição
-  Tecnologias Utilizadas

## Descrição
O objetivo deste projeto é criar um sistema para gerenciar exames médicos. O sistema permite cadastrar médicos, pacientes e exames, vinculando cada exame a um médico e a um paciente. Além disso, é possível consultar todos os exames de um determinado paciente.

### Funcionalidades
1. **Cadastrar Médico:** Adicionar novos médicos ao banco de dados.
2. **Cadastrar Paciente:** Adicionar novos pacientes ao banco de dados.
3. **Cadastrar Exame:** Registrar novos exames, vinculando-os a médicos e pacientes existentes.
4. **Consultar Exames por Paciente:** Listar todos os exames realizados por um determinado paciente.

### Estrutura do Banco de Dados
#### Tabela PACIENTE
```
CREATE TABLE IF NOT EXISTS PACIENTE (
    ID INTEGER PRIMARY KEY,
    NOME VARCHAR(255),
    CPF VARCHAR(255),
    IDADE INTEGER
);
```
#### Tabela MEDICO
```
CREATE TABLE IF NOT EXISTS MEDICO (
    ID INTEGER PRIMARY KEY,
    NOME VARCHAR(255),
    CRM VARCHAR(255),
    ESPECIALIZACAO VARCHAR(255)
);
```
#### Tabela EXAME
```
CREATE TABLE IF NOT EXISTS EXAME (
    ID INTEGER PRIMARY KEY,
    ID_MEDICO INTEGER,
    ID_PACIENTE INTEGER,
    DESCRICAO VARCHAR(255),
    RESULTADO VARCHAR(255)
);
```

## Tecnologias Utilizadas
- Python: Linguagem de programação principal.
- SQLite: Banco de dados relacional utilizado.
- SQLAlchemy ORM: Framework utilizado para mapeamento objeto-relacional.


