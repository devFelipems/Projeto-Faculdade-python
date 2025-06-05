import tkinter as tk
from tkinter import ttk, messagebox
from registration_window import RegistrationWindow

class LoginWindow:
    def __init__(self, master, on_success, db_manager):
        self.master = master
        self.db_manager = db_manager
        self.on_success = on_success
        self.master.title("Tec-Info - Login")
        self.master.geometry("350x250")
        self.master.minsize(350, 250)  
        self.master.resizable(True, True)
        self.setup_style()
        self.create_widgets()
        self.configure_grid()

    def configure_grid(self):
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

    def setup_style(self):
        style = ttk.Style(self.master)
        style.theme_use("clam")
        style.configure("TLabel", font=("Helvetica", 10))
        style.configure("TEntry", padding=5)
        style.configure("TButton", padding=5)

    def create_widgets(self):
        frame = ttk.Frame(self.master, padding=20)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=2)

        welcome_label = ttk.Label(
            frame, 
            text="Bem-vindo à Tec-Info", 
            font=("Helvetica", 14, "bold")
        )
        welcome_label.grid(row=0, column=0, columnspan=2, pady=10, sticky="w")

        # Campo Usuário
        user_label = ttk.Label(frame, text="Usuário:")
        user_label.grid(row=1, column=0, sticky="w", pady=(10, 5))
        self.user_entry = ttk.Entry(frame)
        self.user_entry.grid(row=1, column=1, sticky="ew", pady=(10, 5))

        # Campo Senha
        pass_label = ttk.Label(frame, text="Senha:")
        pass_label.grid(row=2, column=0, sticky="w", pady=5)
        self.pass_entry = ttk.Entry(frame, show="*")
        self.pass_entry.grid(row=2, column=1, sticky="ew", pady=5)

        # Botão de Login
        login_button = ttk.Button(frame, text="Login", command=self.login)
        login_button.grid(row=3, column=0, columnspan=2, pady=(15, 5), sticky="ew")

        # Botão de Cadastro
        reg_button = ttk.Button(frame, text="Cadastrar", command=self.open_registration)
        reg_button.grid(row=4, column=0, columnspan=2, pady=5, sticky="ew")

    def login(self):
        username = self.user_entry.get().strip()
        password = self.pass_entry.get().strip()
        if username and password:
            user = self.db_manager.authenticate_user(username, password)
            if user:
                messagebox.showinfo("Sucesso", "Login efetuado com sucesso!")
                self.master.destroy()
                self.on_success(username)
            else:
                messagebox.showerror("Erro", "Credenciais inválidas. Tente novamente.")
        else:
            messagebox.showerror("Erro", "Preencha os campos de usuário e senha.")

    def open_registration(self):
        RegistrationWindow(self.master, self.db_manager)
