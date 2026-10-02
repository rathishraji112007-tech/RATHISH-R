import sqlite3


def create_history_table():
    conn = sqlite3.connect("pocketsmart.db")

    conn.execute("""
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            category TEXT,
            budget REAL,
            recommendation TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_history(user_id, category, budget, result):
    conn = sqlite3.connect("pocketsmart.db")

    conn.execute("""
        INSERT INTO history
        (user_id, category, budget, recommendation)
        VALUES (?, ?, ?, ?)
    """, (user_id, category, budget, result))

    conn.commit()
    conn.close()


def get_history(user_id):
    conn = sqlite3.connect("pocketsmart.db")

    rows = conn.execute("""
        SELECT category, budget, recommendation
        FROM history
        WHERE user_id = ?
        ORDER BY id DESC
    """, (user_id,)).fetchall()

    conn.close()

    return [
        {
            "category": row[0],
            "budget": row[1],
            "recommendation": row[2]
        }
        for row in rows
    ]


create_history_table()
