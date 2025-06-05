import sqlite3

class DatabaseManager:
    def __init__(self, db_name="curriculos.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_users_table()
        self.create_curriculos_table()

    def create_users_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        );
        """
        self.conn.execute(query)
        self.conn.commit()

    def create_curriculos_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS curriculos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT,
            formacao TEXT,
            experiencia TEXT
        );
        """
        self.conn.execute(query)
        self.conn.commit()

    # Operações CRUD para "curriculos"
    def add_curriculo(self, nome, email, telefone, formacao, experiencia):
        query = "INSERT INTO curriculos (nome, email, telefone, formacao, experiencia) VALUES (?, ?, ?, ?, ?)"
        self.conn.execute(query, (nome, email, telefone, formacao, experiencia))
        self.conn.commit()

    def fetch_curriculos(self):
        cursor = self.conn.execute("SELECT * FROM curriculos")
        return cursor.fetchall()

    def update_curriculo(self, record_id, nome, email, telefone, formacao, experiencia):
        query = "UPDATE curriculos SET nome=?, email=?, telefone=?, formacao=?, experiencia=? WHERE id=?"
        self.conn.execute(query, (nome, email, telefone, formacao, experiencia, record_id))
        self.conn.commit()

    def delete_curriculo(self, record_id):
        query = "DELETE FROM curriculos WHERE id=?"
        self.conn.execute(query, (record_id,))
        self.conn.commit()

    # Operações para gerenciamento de usuários
    def register_user(self, username, email, password):
        query = "INSERT INTO usuarios (username, email, password) VALUES (?, ?, ?)"
        try:
            self.conn.execute(query, (username, email, password))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError as e:
            print("Erro ao registrar usuário:", e)
            return False

    def authenticate_user(self, username, password):
        query = "SELECT * FROM usuarios WHERE username=? AND password=?"
        cursor = self.conn.execute(query, (username, password))
        return cursor.fetchone()

    # Método para filtragem avançada e ordenação
    def fetch_filtered_curriculos(self, filter_column=None, filter_value=None, order_by=None, order_type="ASC"):
        query = "SELECT * FROM curriculos"
        params = []
        if filter_column and filter_value:
            query += " WHERE {} LIKE ?".format(filter_column)
            params.append(f"%{filter_value}%")
        if order_by:
            query += " ORDER BY {} {}".format(order_by, order_type)
        cursor = self.conn.execute(query, params)
        return cursor.fetchall()
