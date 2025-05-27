# Sistema de Controle de Currículos

## Descrição

Este é um protótipo funcional de um **Sistema de Controle de Currículos** para uma agência de empregos, desenvolvido em **Python**, utilizando **Tkinter** para a interface gráfica e **SQLite** como banco de dados local.

O sistema permite gerenciar currículos de candidatos, realizando operações de **Cadastro, Edição, Remoção** e **Geração de Relatórios**.



## Tecnologias Utilizadas

- **Python**
- **Tkinter** —  Para fazer a Interface Gráfica
- **SQLite** — Para Banco de Dados Local



## Funcionalidades Principais

- **Login**: autenticação simples com nome de usuário.
- **Cadastro**: adicionar novos currículos.
- **Listagem**: visualizar todos os currículos cadastrados.
- **Edição**: atualizar informações de currículos.
- **Remoção**: excluir currículos do sistema.
- **Relatórios**: exibir todos os currículos em uma tabela organizada.



## Estrutura da Tabela no Banco de Dados

Tabela: `curriculos`

| Campo            | Tipo     | Descrição                         |
| ---------------- | -------- | --------------------------------- |
| id               | INTEGER  | Identificador único (chave primária) |
| nome             | TEXT     | Nome do candidato                 |
| email            | TEXT     | Email do candidato                |
| telefone         | TEXT     | Telefone de contato               |
| area_interesse   | TEXT     | Área profissional de interesse    |
| experiencia      | TEXT     | Descrição da experiência          |

---

## Como Executar o Sistema

### Passos para execução:

1. **Clone ou baixe** o repositório/arquivo.

2. Após baixar ou clonar basta executar o código para conseguir utilizar

```bash
python sistema_curriculos.py
