import sqlite3

conn = sqlite3.connect('Bikes.db')


def drop_table(table_name):
    conn = sqlite3.connect('Bikes.db')
    c = conn.cursor()

    c.execute(f"DROP TABLE IF EXISTS {table_name}")

    conn.commit()
    conn.close()


def delete_row(table_name, row_id):
    # Cria uma conexão com o banco de dados
    conn = sqlite3.connect('Bikes.db')
    c = conn.cursor()

    # Executa o comando SQL para deletar a linha com o id fornecido
    c.execute(f"DELETE FROM {table_name} WHERE id = ?", (row_id,))

    # Salva as alterações no banco de dados
    conn.commit()

    # Fecha a conexão
    conn.close()

delete_row('usuarios',2)


