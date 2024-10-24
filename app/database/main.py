from sqlite3 import connect

class Databaser:

    def __init__(self, db_file):
        self.db = connect(db_file)
        self.cursor = self.db.cursor()

    def start_database(self):
        # CREATE TABLES HERE
        # EXAMPLE:
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tg_id INTEGER,
            username TEXT,
            is_admin INTEGER DEFAULT 0
            )
            """
        )
        self.db.commit()

    # USAGE EXAMPLE:
    def add_user(self, tg_id: int, username: str) -> None:
        self.cursor.execute("INSERT INTO users (tg_id, username) VALUES (?, ?)", (tg_id, username,))
        self.db.commit()

databaser = Databaser("./app/database/database.db")
def start_db():
    databaser.start_database()
    print("Database started!")