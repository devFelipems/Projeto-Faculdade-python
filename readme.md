# Tec-Info – Sistema de Currículos

O **Tec-Info – Sistema de Currículos** é um protótipo funcional de uma aplicação para o gerenciamento de currículos, desenvolvido como trabalho acadêmico. A aplicação foi implementada em Python utilizando a biblioteca Tkinter (com TTK) para a interface gráfica e SQLite para o armazenamento dos dados. O sistema é modularizado, contando com telas de login, cadastro, gerenciamento (CRUD) e funcionalidades avançadas como filtro, ordenação e alternância entre modos claro e escuro.

## Funcionalidades

- **Login e Cadastro de Usuários:**  
  - Tela de autenticação com campos para usuário e senha, com responsividade para telas pequenas e grandes.
  - Tela de cadastro para registrar novos usuários, com campos para usuário, email, senha e confirmação.
  
- **Gestão de Currículos (CRUD):**  
  - Operações de cadastro, consulta, atualização e remoção de currículos.
  - Cada currículo inclui informações como nome, email, telefone, formação e experiência.
  
- **Filtro e Ordenação Avançada:**  
  - Filtro por campos específicos (ex.: nome, email, telefone, formação, experiência) com inserção de palavra‑chave.
  - Ordenação dos registros com escolha de coluna e tipo de ordenação (ascendente ou descendente).
  
- **Modo Escuro e Claro:**  
  - Alternância entre tema claro e modo escuro via menu na tela principal, para proporcionar melhor experiência visual de acordo com a preferência do usuário.
  
- **Relatórios e Detalhes:**  
  - Janela dedicada à exibição dos relatórios com todos os currículos cadastrados.
  - Visualização detalhada de cada currículo selecionado.

## Tecnologias Utilizadas

- **Linguagem:** Python 3.6
- **Interface Gráfica:** Tkinter com TTK  
- **Banco de Dados:** SQLite (banco de dados local)  
- **Organização do Código:**  
  - `main.py` — ponto de entrada da aplicação  
  - `database.py` — gerenciamento do banco de dados e execução de queries SQL  
  - `login_window.py` — tela de login  
  - `registration_window.py` — tela de cadastro de usuários  
  - `main_window.py` — interface principal com funcionalidades avançadas, incluindo filtros, modo escuro e relatórios

## Estrutura do Projeto

```plaintext
Tec-Info-Sistema-de-Curriculos/
├── README.md
├── main.py
├── database.py
├── login_window.py
├── registration_window.py
└── main_window.py
