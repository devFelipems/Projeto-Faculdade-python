import tkinter as tk
from tkinter import ttk, messagebox

class RegistrationWindow:
    def __init__(self, master, db_manager):
        self.db_manager = db_manager
        self.top = tk.Toplevel(master)
        self.top.title("Cadastro de Usuário - Tec-Info")
        self.top.geometry("350x300")
        self.top.minsize(350, 300) 
        self.top.resizable(True, True)
        self.setup_style()
        self.create_widgets()
        self.configure_grid()

    def configure_grid(self):
        self.top.columnconfigure(0, weight=1)
        self.top.rowconfigure(0, weight=1)

    def setup_style(self):
        style = ttk.Style(self.top)
        style.theme_use("clam")
        style.configure("TLabel", font=("Helvetica", 10))
        style.configure("TEntry", padding=5)
        style.configure("TButton", padding=5)

    def create_widgets(self):
        frame = ttk.Frame(self.top, padding=20)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=2)

        title_label = ttk.Label(
            frame, 
            text="Cadastro de Usuário", 
            font=("Helvetica", 14, "bold")
        )
        title_label.grid(row=0, column=0, columnspan=2, pady=10, sticky="w")

        # Campo Usuário
        user_label = ttk.Label(frame, text="Usuário:")
        user_label.grid(row=1, column=0, sticky="w", pady=5)
        self.user_entry = ttk.Entry(frame)
        self.user_entry.grid(row=1, column=1, sticky="ew", pady=5)

        # Campo Email
        email_label = ttk.Label(frame, text="Email:")
        email_label.grid(row=2, column=0, sticky="w", pady=5)
        self.email_entry = ttk.Entry(frame)
        self.email_entry.grid(row=2, column=1, sticky="ew", pady=5)

        # Campo Senha
        pass_label = ttk.Label(frame, text="Senha:")
        pass_label.grid(row=3, column=0, sticky="w", pady=5)
        self.pass_entry = ttk.Entry(frame, show="*")
        self.pass_entry.grid(row=3, column=1, sticky="ew", pady=5)

        # Campo Confirmar Senha
        conf_label = ttk.Label(frame, text="Confirmar Senha:")
        conf_label.grid(row=4, column=0, sticky="w", pady=5)
        self.conf_entry = ttk.Entry(frame, show="*")
        self.conf_entry.grid(row=4, column=1, sticky="ew", pady=5)

        # Botão de Registro
        reg_button = ttk.Button(frame, text="Registrar", command=self.register)
        reg_button.grid(row=5, column=0, columnspan=2, pady=15, sticky="ew")

    def register(self):
        username = self.user_entry.get().strip()
        email = self.email_entry.get().strip()
        password = self.pass_entry.get().strip()
        confirm = self.conf_entry.get().strip()

        if not (username and email and password and confirm):
            messagebox.showerror("Erro", "Todos os campos são obrigatórios.")
            return

        if password != confirm:
            messagebox.showerror("Erro", "As senhas não coincidem.")
            return

        success = self.db_manager.register_user(username, email, password)
        if success:
            messagebox.showinfo("Sucesso", "Usuário registrado com sucesso!")
            self.top.destroy()
        else:
            messagebox.showerror("Erro", "Falha no registro. Usuário ou email já existente.")
