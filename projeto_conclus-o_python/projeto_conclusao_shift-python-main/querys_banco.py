import sqlite3

conn = sqlite3.connect('Bikes.db')


def select_all(table_name):
    # Cria uma conexão com o banco de dados
    conn = sqlite3.connect('Bikes.db')
    c = conn.cursor()

    # Executa o comando SQL para selecionar todos os valores da tabela
    c.execute(f"SELECT * FROM {table_name}")

    # Obtém todos os valores da tabela
    rows = c.fetchall()

    # Fecha a conexão
    conn.commit()
    conn.close()

    # Retorna os valores da tabela
    return rows

def insert_row(table_name, values):
    # Cria uma conexão com o banco de dados
    conn = sqlite3.connect('Bikes.db')
    c = conn.cursor()

    # Executa o comando SQL para inserir um novo valor na tabela
    c.execute(f"INSERT INTO {table_name} VALUES (?, ?, ?, ?)", values)

    # Salva as alterações no banco de dados
    conn.commit()

    # Fecha a conexão
    conn.close()

def update_row(table_name, values):
    # Cria uma conexão com o banco de dados
    conn = sqlite3.connect('Bikes.db')
    c = conn.cursor()

    # Executa o comando SQL para atualizar um valor na tabela
    c.execute(f"UPDATE {table_name} SET tipo = ?, valor = ?, estoque = ? WHERE id = ?", values)

    # Salva as alterações no banco de dados
    conn.commit()

    # Fecha a conexão
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

def select_row(id):
    # Cria uma conexão com o banco de dados
    conn = sqlite3.connect('Bikes.db')
    c = conn.cursor()

    # Executa o comando SQL para selecionar o valor com o ID fornecido
    c.execute("SELECT * FROM bicicletas WHERE id = ?", (id,))

    # Obtém o valor selecionado
    valor = c.fetchone()

    conn.commit()
    # Fecha a conexão
    conn.close()

    return valor