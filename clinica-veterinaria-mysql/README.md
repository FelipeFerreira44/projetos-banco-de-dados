# Clínica Veterinária – Modelo lógico e script físico (MySQL)

Projeto da disciplina de Arquitetura de Banco de Dados (PUCPR): modelagem de um banco relacional para uma clínica veterinária, feita no MySQL Workbench.

## O que tem aqui
- `modelo_logico_clinica.mwb`: modelo lógico (abrir no MySQL Workbench).
- `db-clinica-fisico.sql`: script gerado pelo Workbench (forward engineering) que cria o schema `db_clinica`.

## Modelo
18 tabelas, com chaves primárias/estrangeiras e índices:
`Pessoa`, `contato`, `email`, `Cliente`, `Departamento`, `Cargo`, `Funcionario`, `Animal`, `Cliente_tem_animal`, `Registro_clinico`, `Sintomas`, `Atendimento`, `Medicamento`, `Farmacia`, `medicamento_tem_farmacia`, `Cobranca`, `Forma_pagamento`, `cobranca_tem_pagamento`.

Pontos de modelagem: generalização de pessoa (clientes e funcionários), relacionamentos N:N resolvidos com tabelas associativas, e telefones/e-mails em tabelas próprias.

## Como usar
1. Abra o MySQL Workbench e conecte a um servidor MySQL 8.
2. Execute `db-clinica-fisico.sql`. Ele cria o schema `db_clinica`.

## Tecnologias
MySQL 8, MySQL Workbench, SQL (DDL).
