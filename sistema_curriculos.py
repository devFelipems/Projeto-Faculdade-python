import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

#  Parte do banco de dados
def criar_banco():
    conn = sqlite3.connect('curriculos.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS curriculos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT NOT NULL,
            area_interesse TEXT NOT NULL,
            experiencia TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

#  Algumas funções de crud
def adicionar_curriculo(nome, email, telefone, area, experiencia):
    conn = sqlite3.connect('curriculos.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO curriculos (nome, email, telefone, area_interesse, experiencia)
        VALUES (?, ?, ?, ?, ?)
    ''', (nome, email, telefone, area, experiencia))
    conn.commit()
    conn.close()

def listar_curriculos():
    conn = sqlite3.connect('curriculos.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM curriculos')
    dados = cursor.fetchall()
    conn.close()
    return dados

def atualizar_curriculo(id, nome, email, telefone, area, experiencia):
    conn = sqlite3.connect('curriculos.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE curriculos
        SET nome=?, email=?, telefone=?, area_interesse=?, experiencia=?
        WHERE id=?
    ''', (nome, email, telefone, area, experiencia, id))
    conn.commit()
    conn.close()

def remover_curriculo(id):
    conn = sqlite3.connect('curriculos.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM curriculos WHERE id=?', (id,))
    conn.commit()
    conn.close()

# Utilizando o tkinter para criar a interface gráfica

# Tela de login
def tela_login():
    def verificar_login():
        usuario = entrada_usuario.get()
        if usuario:
            login.destroy()
            tela_principal()
        else:
            messagebox.showwarning("Erro", "Digite um nome de usuário.")

    login = tk.Tk()
    login.title("Login")

    tk.Label(login, text="Nome de usuário:").pack(pady=5)
    entrada_usuario = tk.Entry(login)
    entrada_usuario.pack(pady=5)
    tk.Button(login, text="Entrar", command=verificar_login).pack(pady=10)

    login.mainloop()

# Tela principal do sistema
def tela_principal():
    def abrir_adicionar():
        janela = tk.Toplevel()
        janela.title("Adicionar Currículo")

        tk.Label(janela, text="Nome:").pack()
        entrada_nome = tk.Entry(janela)
        entrada_nome.pack()

        tk.Label(janela, text="Email:").pack()
        entrada_email = tk.Entry(janela)
        entrada_email.pack()

        tk.Label(janela, text="Telefone:").pack()
        entrada_telefone = tk.Entry(janela)
        entrada_telefone.pack()

        tk.Label(janela, text="Área de Interesse:").pack()
        entrada_area = tk.Entry(janela)
        entrada_area.pack()

        tk.Label(janela, text="Experiência:").pack()
        entrada_experiencia = tk.Entry(janela)
        entrada_experiencia.pack()

        def salvar():
            adicionar_curriculo(
                entrada_nome.get(),
                entrada_email.get(),
                entrada_telefone.get(),
                entrada_area.get(),
                entrada_experiencia.get()
            )
            messagebox.showinfo("Sucesso", "Currículo cadastrado com sucesso!")
            janela.destroy()

        tk.Button(janela, text="Salvar", command=salvar).pack(pady=10)

    def abrir_listar():
        janela = tk.Toplevel()
        janela.title("Listar Currículos")

        tree = ttk.Treeview(janela, columns=("ID", "Nome", "Email", "Telefone", "Área", "Experiência"), show="headings")
        for col in tree["columns"]:
            tree.heading(col, text=col)
        tree.pack()

        for item in listar_curriculos():
            tree.insert("", "end", values=item)

        def editar():
            selecionado = tree.selection()
            if not selecionado:
                messagebox.showwarning("Atenção", "Selecione um currículo para editar.")
                return
            item = tree.item(selecionado)["values"]
            abrir_editar(item)

        def deletar():
            selecionado = tree.selection()
            if not selecionado:
                messagebox.showwarning("Atenção", "Selecione um currículo para remover.")
                return
            item = tree.item(selecionado)["values"]
            remover_curriculo(item[0])
            messagebox.showinfo("Sucesso", "Currículo removido com sucesso!")
            janela.destroy()
            abrir_listar()

        tk.Button(janela, text="Editar", command=editar).pack(side="left", padx=10, pady=10)
        tk.Button(janela, text="Remover", command=deletar).pack(side="left", padx=10, pady=10)

    def abrir_editar(item):
        janela = tk.Toplevel()
        janela.title("Editar Currículo")

        tk.Label(janela, text="Nome:").pack()
        entrada_nome = tk.Entry(janela)
        entrada_nome.insert(0, item[1])
        entrada_nome.pack()

        tk.Label(janela, text="Email:").pack()
        entrada_email = tk.Entry(janela)
        entrada_email.insert(0, item[2])
        entrada_email.pack()

        tk.Label(janela, text="Telefone:").pack()
        entrada_telefone = tk.Entry(janela)
        entrada_telefone.insert(0, item[3])
        entrada_telefone.pack()

        tk.Label(janela, text="Área de Interesse:").pack()
        entrada_area = tk.Entry(janela)
        entrada_area.insert(0, item[4])
        entrada_area.pack()

        tk.Label(janela, text="Experiência:").pack()
        entrada_experiencia = tk.Entry(janela)
        entrada_experiencia.insert(0, item[5])
        entrada_experiencia.pack()

        def salvar_edicao():
            atualizar_curriculo(
                item[0],
                entrada_nome.get(),
                entrada_email.get(),
                entrada_telefone.get(),
                entrada_area.get(),
                entrada_experiencia.get()
            )
            messagebox.showinfo("Sucesso", "Currículo atualizado com sucesso!")
            janela.destroy()

        tk.Button(janela, text="Salvar Alterações", command=salvar_edicao).pack(pady=10)

    def abrir_relatorios():
        janela = tk.Toplevel()
        janela.title("Relatórios")

        tree = ttk.Treeview(janela, columns=("ID", "Nome", "Email", "Telefone", "Área", "Experiência"), show="headings")
        for col in tree["columns"]:
            tree.heading(col, text=col)
        tree.pack()

        for item in listar_curriculos():
            tree.insert("", "end", values=item)

    principal = tk.Tk()
    principal.title("Sistema de Controle de Currículos")

    tk.Label(principal, text="Bem-vindo ao Sistema de Curriculos da Tec-Info").pack(pady=10)

    tk.Button(principal, text="Adicionar Currículo", width=30, command=abrir_adicionar).pack(pady=5)
    tk.Button(principal, text="Listar/Editar/Remover Currículos", width=30, command=abrir_listar).pack(pady=5)
    tk.Button(principal, text="Gerar Relatório", width=30, command=abrir_relatorios).pack(pady=5)

    principal.mainloop()

# Executando o sistema
if __name__ == "__main__":
    criar_banco()
    tela_login()
