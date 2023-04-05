import sqlite3

# Conectar-se ao banco de dados ou criá-lo se não existir
conn = sqlite3.connect('Bikes.db')

# # Criar a tabela usuarios
# conn.execute('''CREATE TABLE usuarios
#              (id INTEGER PRIMARY KEY AUTOINCREMENT,
#              nome TEXT NOT NULL,
#              email TEXT NOT NULL,
#              senha TEXT NOT NULL);''')

# # Criar a tabela bicicletas
# conn.execute('''CREATE TABLE bicicletas
#              (id INTEGER PRIMARY KEY,
#              tipo TEXT NOT NULL,
#              valor REAL NOT NULL,
#              estoque INTEGER NOT NULL);''')

# # Criar a tabela alugueis
# conn.execute('''CREATE TABLE alugueis
#              (id INTEGER PRIMARY KEY AUTOINCREMENT,
#              client_id INTEGER NOT NULL,
#              bike_id INTEGER NOT NULL,
#              data_aluguel TEXT NOT NULL,
#              data_devolucao TEXT NOT NULL,
#              FOREIGN KEY (client_id) REFERENCES usuarios(id),
#              FOREIGN KEY (bike_id) REFERENCES bicicletas(id));''')


# conn.execute("INSERT INTO bicicletas (id, tipo, valor, estoque) \
#               VALUES (2, 'Speed Bike', 50.00, 5)")
# conn.execute("INSERT INTO bicicletas (id, tipo, valor, estoque) \
#               VALUES (3, 'Normal Bike', 20.00, 5)")

# # Inserir valores na tabela alugueis
# conn.execute("INSERT INTO alugueis (client_id, bike_id, data_aluguel, data_devolucao) \
#               VALUES (1, 1, '2023-04-01', '2023-04-08')")
# conn.execute("INSERT INTO alugueis (client_id, bike_id, data_aluguel, data_devolucao) \
#               VALUES (2, 2, '2023-04-02', '2023-04-09')")

# # Commitar as alterações e fechar a conexão com o banco de dados
# conn.commit()
# conn.close()
