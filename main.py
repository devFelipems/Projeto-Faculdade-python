import tkinter as tk
from database import DatabaseManager
from login_window import LoginWindow
from main_window import MainWindow

def main():
    db_manager = DatabaseManager()

    login_root = tk.Tk()
    def on_login_success(username):
        main_app = MainWindow(username, db_manager)
        main_app.run()

    LoginWindow(login_root, on_login_success, db_manager)
    login_root.mainloop()

if __name__ == "__main__":
    main()
