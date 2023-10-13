import sqlite3

def create_connection():
    conn = sqlite3.connect("user_balances.db")
    cursor = conn.cursor()
    return conn, cursor

def close_connection(conn):
    conn.commit()
    conn.close()

def get_balance(user_id):
    conn, cursor = create_connection()

    cursor.execute("SELECT balance FROM balances WHERE user_id = ?", (user_id,))
    result = cursor.fetchone()

    close_connection(conn)

    if result:
        return result[0]
    else:
        return 0

def update_balance(user_id, new_balance):
    conn, cursor = create_connection()

    cursor.execute("UPDATE balances SET balance = ? WHERE user_id = ?", (new_balance, user_id))

    close_connection(conn)

def definition(user_id):
    conn, cursor = create_connection()
    balance = 1000

    # checks if the user exists in db
    cursor.execute("SELECT * FROM balances WHERE user_id = ?", (user_id,))
    if cursor.fetchone() is not None: #if yes
        return #returns

    # if yes defines user in db
    cursor.execute("INSERT INTO balances (user_id, balance) VALUES (?, ?)", (user_id, balance))
    close_connection(conn)