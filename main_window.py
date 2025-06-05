import tkinter as tk
from tkinter import ttk, messagebox

def apply_dark_mode(style):
    # Aplica estilo para modo escuro
    style.configure("TFrame", background="#2E2E2E")
    style.configure("TLabelframe", background="#2E2E2E", foreground="#FFFFFF")
    style.configure("TLabelframe.Label", background="#2E2E2E", foreground="#FFFFFF")
    style.configure("TLabel", background="#2E2E2E", foreground="#FFFFFF")
    style.configure("TEntry", fieldbackground="#3E3E3E", foreground="#FFFFFF", padding=5)
    style.configure("TButton", background="#3E3E3E", foreground="#FFFFFF", padding=5)

def apply_light_mode(style):
    # Aplica estilo para modo claro (padrão)
    style.configure("TFrame", background="#f0f0f0")
    style.configure("TLabelframe", background="#f0f0f0", foreground="#000000")
    style.configure("TLabelframe.Label", background="#f0f0f0", foreground="#000000")
    style.configure("TLabel", background="#f0f0f0", foreground="#000000")
    style.configure("TEntry", fieldbackground="#ffffff", foreground="#000000", padding=5)
    style.configure("TButton", background="#ffffff", foreground="#000000", padding=5)

class MainWindow:
    def __init__(self, username, db_manager):
        self.username = username
        self.db_manager = db_manager
        self.dark_mode = False
        self.root = tk.Tk()
        self.root.title("Tec-Info - Sistema de Currículos")
        self.root.geometry("1000x700")
        self.root.resizable(True, True)
        self.setup_menu()
        self.setup_style()
        self.create_widgets()
        self.populate_treeview()
        self.configure_grid()

    def configure_grid(self):
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

    def setup_menu(self):
        menu_bar = tk.Menu(self.root)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Sair", command=self.root.destroy)
        file_menu.add_command(label="Alternar Tema", command=self.toggle_theme)
        menu_bar.add_cascade(label="Arquivo", menu=file_menu)
        self.root.config(menu=menu_bar)

    def setup_style(self):
        self.style = ttk.Style(self.root)
        apply_light_mode(self.style)
        self.root.configure(background="#f0f0f0")

    def toggle_theme(self):
        if self.dark_mode:
            self.dark_mode = False
            apply_light_mode(self.style)
            self.root.configure(background="#f0f0f0")
        else:
            self.dark_mode = True
            apply_dark_mode(self.style)
            self.root.configure(background="#2E2E2E")

    def create_widgets(self):
        top_frame = ttk.Frame(self.root, padding=10)
        top_frame.pack(fill="x", pady=10)
        welcome_label = ttk.Label(top_frame, text=f"Bem-vindo, {self.username}!", font=("Helvetica", 16))
        welcome_label.pack()

        search_frame = ttk.Frame(self.root, padding=10)
        search_frame.pack(fill="x", padx=20)
        search_label = ttk.Label(search_frame, text="Pesquisar:")
        search_label.pack(side="left", padx=(0, 10))
        self.search_entry = ttk.Entry(search_frame)
        self.search_entry.pack(side="left", fill="x", expand=True)
        search_button = ttk.Button(search_frame, text="Buscar", command=self.filter_records)
        search_button.pack(side="left", padx=5)
        clear_search_button = ttk.Button(search_frame, text="Limpar filtros", command=self.populate_treeview)
        clear_search_button.pack(side="left", padx=5)

        advanced_frame = ttk.Frame(self.root, padding=10)
        advanced_frame.pack(fill="x", padx=20)
        filter_label = ttk.Label(advanced_frame, text="Filtrar por:")
        filter_label.pack(side="left", padx=(0, 5))
        self.filter_column = ttk.Combobox(advanced_frame, state="readonly", 
                                  values=["Todos", "nome", "email", "telefone", "formacao", "experiencia"])
        self.filter_column.current(0)
        self.filter_column.pack(side="left", padx=(0, 10))
        keyword_label = ttk.Label(advanced_frame, text="Palavra‑chave:")
        keyword_label.pack(side="left", padx=(0, 5))
        self.keyword_entry = ttk.Entry(advanced_frame)
        self.keyword_entry.pack(side="left", padx=(0, 10), fill="x", expand=True)
        order_label = ttk.Label(advanced_frame, text="Ordenar por:")
        order_label.pack(side="left", padx=(0, 5))
        self.order_column = ttk.Combobox(advanced_frame, state="readonly", 
                                 values=["", "nome", "email", "telefone", "formacao", "experiencia"])
        self.order_column.current(0)
        self.order_column.pack(side="left", padx=(0, 10))
        self.order_type = ttk.Combobox(advanced_frame, state="readonly", values=["ASC", "DESC"])
        self.order_type.current(0)
        self.order_type.pack(side="left", padx=(0, 10))
        advanced_filter_button = ttk.Button(advanced_frame, text="Aplicar Filtro Avançado", command=self.advanced_filter)
        advanced_filter_button.pack(side="left", padx=5)

        # Frame para cadastro/edição de currículos
        form_frame = ttk.LabelFrame(self.root, text="Cadastro / Edição de Currículos", padding=10)
        form_frame.pack(fill="x", padx=20, pady=10)
        ttk.Label(form_frame, text="Nome:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.entry_nome = ttk.Entry(form_frame, width=30)
        self.entry_nome.grid(row=0, column=1, padx=10, pady=5)
        ttk.Label(form_frame, text="Email:").grid(row=0, column=2, padx=10, pady=5, sticky="e")
        self.entry_email = ttk.Entry(form_frame, width=30)
        self.entry_email.grid(row=0, column=3, padx=10, pady=5)
        ttk.Label(form_frame, text="Telefone:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_telefone = ttk.Entry(form_frame, width=30)
        self.entry_telefone.grid(row=1, column=1, padx=10, pady=5)
        ttk.Label(form_frame, text="Formação:").grid(row=1, column=2, padx=10, pady=5, sticky="e")
        self.entry_formacao = ttk.Entry(form_frame, width=30)
        self.entry_formacao.grid(row=1, column=3, padx=10, pady=5)
        ttk.Label(form_frame, text="Experiência:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.entry_experiencia = ttk.Entry(form_frame, width=33)
        self.entry_experiencia.grid(row=2, column=1, padx=10, pady=5)
        buttons_frame = ttk.Frame(form_frame)
        buttons_frame.grid(row=3, column=0, columnspan=4, pady=10)
        self.btn_add = ttk.Button(buttons_frame, text="Cadastrar", command=self.add_record)
        self.btn_add.grid(row=0, column=0, padx=5)
        self.btn_update = ttk.Button(buttons_frame, text="Atualizar", command=self.update_record)
        self.btn_update.grid(row=0, column=1, padx=5)
        self.btn_delete = ttk.Button(buttons_frame, text="Remover", command=self.delete_record)
        self.btn_delete.grid(row=0, column=2, padx=5)
        self.btn_clear = ttk.Button(buttons_frame, text="Limpar", command=self.clear_form)
        self.btn_clear.grid(row=0, column=3, padx=5)
        self.btn_details = ttk.Button(buttons_frame, text="Visualizar Detalhes", command=self.open_detail_window)
        self.btn_details.grid(row=0, column=4, padx=5)

        # Frame de listagem dos currículos
        list_frame = ttk.LabelFrame(self.root, text="Lista de Currículos", padding=10)
        list_frame.pack(fill="both", expand=True, padx=20, pady=10)
        columns = ("ID", "Nome", "Email", "Telefone", "Formação", "Experiência")
        self.tree = ttk.Treeview(list_frame, columns=columns, show="headings", height=10)
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center", width=100)
        self.tree.column("Nome", width=150)
        self.tree.column("Email", width=200)
        self.tree.column("Formação", width=150)
        self.tree.column("Experiência", width=150)
        self.tree.pack(fill="both", expand=True)
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        # Botão na parte inferior para geração de relatório
        bottom_frame = ttk.Frame(self.root, padding=10)
        bottom_frame.pack(pady=10)
        self.btn_report = ttk.Button(bottom_frame, text="Gerar Relatório", command=self.open_report_window)
        self.btn_report.pack()

    def populate_treeview(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        records = self.db_manager.fetch_curriculos()
        for record in records:
            self.tree.insert("", "end", values=record)

    def filter_records(self):
        search_term = self.search_entry.get().strip().lower()
        for row in self.tree.get_children():
            self.tree.delete(row)
        records = self.db_manager.fetch_curriculos()
        for record in records:
            if search_term in str(record).lower():
                self.tree.insert("", "end", values=record)

    def advanced_filter(self):
        # Coleta os parâmetros dos controles avançados
        column = self.filter_column.get()
        keyword = self.keyword_entry.get().strip()
        order_by = self.order_column.get().strip()
        order_type = self.order_type.get().strip()
        if column == "Todos":
            column = None
        records = self.db_manager.fetch_filtered_curriculos(filter_column=column,
                                                              filter_value=keyword,
                                                              order_by=order_by,
                                                              order_type=order_type)
        for row in self.tree.get_children():
            self.tree.delete(row)
        for record in records:
            self.tree.insert("", "end", values=record)

    def clear_form(self):
        self.entry_nome.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_telefone.delete(0, tk.END)
        self.entry_formacao.delete(0, tk.END)
        self.entry_experiencia.delete(0, tk.END)
        self.selected_record = None

    def add_record(self):
        nome = self.entry_nome.get().strip()
        email = self.entry_email.get().strip()
        telefone = self.entry_telefone.get().strip()
        formacao = self.entry_formacao.get().strip()
        experiencia = self.entry_experiencia.get().strip()
        if nome and email:
            try:
                self.db_manager.add_curriculo(nome, email, telefone, formacao, experiencia)
                messagebox.showinfo("Sucesso", "Currículo cadastrado com sucesso!")
                self.populate_treeview()
                self.clear_form()
            except Exception as e:
                messagebox.showerror("Erro", f"Falha ao cadastrar: {e}")
        else:
            messagebox.showerror("Erro", "Nome e Email são obrigatórios.")

    def on_tree_select(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            record = self.tree.item(selected_item)["values"]
            self.selected_record = record
            self.entry_nome.delete(0, tk.END)
            self.entry_nome.insert(0, record[1])
            self.entry_email.delete(0, tk.END)
            self.entry_email.insert(0, record[2])
            self.entry_telefone.delete(0, tk.END)
            self.entry_telefone.insert(0, record[3])
            self.entry_formacao.delete(0, tk.END)
            self.entry_formacao.insert(0, record[4])
            self.entry_experiencia.delete(0, tk.END)
            self.entry_experiencia.insert(0, record[5])

    def update_record(self):
        if self.selected_record:
            record_id = self.selected_record[0]
            nome = self.entry_nome.get().strip()
            email = self.entry_email.get().strip()
            telefone = self.entry_telefone.get().strip()
            formacao = self.entry_formacao.get().strip()
            experiencia = self.entry_experiencia.get().strip()
            if nome and email:
                try:
                    self.db_manager.update_curriculo(record_id, nome, email, telefone, formacao, experiencia)
                    messagebox.showinfo("Sucesso", "Currículo atualizado com sucesso!")
                    self.populate_treeview()
                    self.clear_form()
                except Exception as e:
                    messagebox.showerror("Erro", f"Falha ao atualizar: {e}")
            else:
                messagebox.showerror("Erro", "Nome e Email são obrigatórios para atualizar.")
        else:
            messagebox.showerror("Erro", "Selecione um registro para atualizar.")

    def delete_record(self):
        if self.selected_record:
            record_id = self.selected_record[0]
            answer = messagebox.askyesno("Confirmar", "Deseja realmente remover este currículo?")
            if answer:
                try:
                    self.db_manager.delete_curriculo(record_id)
                    messagebox.showinfo("Sucesso", "Currículo removido com sucesso!")
                    self.populate_treeview()
                    self.clear_form()
                except Exception as e:
                    messagebox.showerror("Erro", f"Falha ao remover: {e}")
        else:
            messagebox.showerror("Erro", "Selecione um registro para remover.")

    def open_report_window(self):
        ReportWindow(self.db_manager)

    def open_detail_window(self):
        if self.selected_record:
            DetailWindow(self.selected_record)
        else:
            messagebox.showerror("Erro", "Selecione um registro para visualizar os detalhes.")

    def run(self):
        self.root.mainloop()

# Janela de Relatórios
class ReportWindow:
    def __init__(self, db_manager):
        self.db_manager = db_manager
        self.top = tk.Toplevel()
        self.top.title("Relatórios de Currículos - Tec-Info")
        self.top.geometry("800x500")
        self.setup_style()
        self.create_widgets()
        self.populate_treeview()

    def setup_style(self):
        style = ttk.Style(self.top)
        style.theme_use("clam")
        self.top.configure(background="#f0f0f0")

    def create_widgets(self):
        report_frame = ttk.LabelFrame(self.top, text="Todos os Currículos", padding=10)
        report_frame.pack(fill="both", expand=True, padx=20, pady=20)
        columns = ("ID", "Nome", "Email", "Telefone", "Formação", "Experiência")
        self.tree_report = ttk.Treeview(report_frame, columns=columns, show="headings")
        for col in columns:
            self.tree_report.heading(col, text=col)
            self.tree_report.column(col, anchor="center", width=100)
        self.tree_report.column("Nome", width=150)
        self.tree_report.column("Email", width=200)
        self.tree_report.column("Formação", width=150)
        self.tree_report.column("Experiência", width=150)
        self.tree_report.pack(fill="both", expand=True)
        close_btn = ttk.Button(self.top, text="Fechar", command=self.top.destroy)
        close_btn.pack(pady=10)

    def populate_treeview(self):
        for row in self.tree_report.get_children():
            self.tree_report.delete(row)
        records = self.db_manager.fetch_curriculos()
        for record in records:
            self.tree_report.insert("", "end", values=record)

# Janela de Detalhes do Currículo
class DetailWindow:
    def __init__(self, record):
        self.record = record
        self.top = tk.Toplevel()
        self.top.title("Detalhes do Currículo - Tec-Info")
        self.top.geometry("400x300")
        self.create_widgets()

    def create_widgets(self):
        fields = ["ID", "Nome", "Email", "Telefone", "Formação", "Experiência"]
        for i, field in enumerate(fields):
            label_field = ttk.Label(self.top, text=f"{field}:", font=("Helvetica", 10, "bold"))
            label_field.grid(row=i, column=0, padx=10, pady=5, sticky="e")
            label_value = ttk.Label(self.top, text=str(self.record[i]), font=("Helvetica", 10))
            label_value.grid(row=i, column=1, padx=10, pady=5, sticky="w")
