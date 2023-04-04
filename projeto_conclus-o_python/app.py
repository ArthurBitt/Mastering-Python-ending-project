from flask import Flask, render_template, request, redirect, url_for, flash, session,make_response
import sqlite3
import secrets
import random


app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'
global bikes, usuario_valido, obter_id_usuario
bikes = []

# Rota para a página de login
@app.route('/')
def index():
    response = make_response(render_template('index.html'))
    response.set_cookie('aluguel_feito', '', expires=0)
    return response

# Rota admin
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        # Se a requisição for um POST, atualize o estoque da bicicleta
        bike_id = request.form['bike_id']
        operacao = request.form['operacao']

        conn = sqlite3.connect('Bikes.db')
        c = conn.cursor()

        # Se a operação for aumentar, incremente 1 no estoque da bicicleta
        if operacao == 'aumentar':
            c.execute(
                "UPDATE bicicletas SET estoque = estoque + 1 WHERE id = ?", (bike_id,))
        # Se a operação for diminuir, verifique se o estoque atual é maior que zero antes de decrementar
        elif operacao == 'diminuir':
            c.execute("SELECT estoque FROM bicicletas WHERE id = ?", (bike_id,))
            estoque = c.fetchone()[0]
            if estoque > 0:
                c.execute(
                    "UPDATE bicicletas SET estoque = estoque - 1 WHERE id = ?", (bike_id,))
                flash('Estoque atualizado com sucesso!')
            else:
                flash('Estoque indisponível!')

        conn.commit()
        conn.close()

    # Recupere a lista de bicicletas do banco de dados
    conn = sqlite3.connect('Bikes.db')
    c = conn.cursor()
    c.execute("SELECT * FROM bicicletas")
    bikes = c.fetchall()
    conn.close()
    return render_template('admin.html', bikes=bikes)

    # Renderize o template admin e passe a lista de bicicletas como argumento
    return render_template('admin.html', bikes=bikes)

#diminuir o estoque
@app.route('/diminuir_estoque/<int:bike_id>', methods=['POST',])
def diminuir_estoque(bike_id):
    conn = sqlite3.connect('Bikes.db')
    c = conn.cursor()

    # Verifica se a bike existe no banco de dados
    c.execute("SELECT * FROM bicicletas WHERE id = ?", (bike_id,))
    bike = c.fetchone()
    if bike is None:
        flash('Bike não encontrada.', 'error')
        return redirect(url_for('admin'))

    # Verifica se há estoque disponível para diminuir
    if bike[3] <= 0:
        flash('Estoque insuficiente.', 'error')
    else:
        # Diminui o estoque da bike
        c.execute("UPDATE bicicletas SET estoque = ? WHERE id = ?",
                  (bike[3] - 1, bike_id))
        conn.commit()
        print('Estoque atualizado com sucesso!', 'success')

    conn.close()
    return redirect(url_for('admin'))

#aumentar o estoque
@app.route('/aumentar_estoque/<int:bike_id>', methods=['POST'])
def aumentar_estoque(bike_id):
    conn = sqlite3.connect('Bikes.db')
    c = conn.cursor()

    # Verifica se a bike existe no banco de dados
    c.execute("SELECT * FROM bicicletas WHERE id = ?", (bike_id,))
    bike = c.fetchone()
    if bike is None:
        flash('Bike não encontrada.', 'error')
        return redirect(url_for('admin'))

    # Aumenta o estoque da bike
    c.execute("UPDATE bicicletas SET estoque = ? WHERE id = ?",
              (bike[3] + 1, bike_id))
    conn.commit()
    print('Estoque atualizado com sucesso!', 'success')

    conn.close()
    return redirect(url_for('admin'))

# deletar e inserir bicicletas
@app.route('/deletar_bike/<int:bike_id>')
def deletar_bike(bike_id):
    conn = sqlite3.connect('Bikes.db')
    c = conn.cursor()

    # Verifica se a bike existe no banco de dados
    c.execute("SELECT * FROM bicicletas WHERE id = ?", (bike_id,))
    bike = c.fetchone()
    if bike is None:
        flash('Bike não encontrada.', 'error')
    else:
        # Deleta a bike do banco de dados
        c.execute("DELETE FROM bicicletas WHERE id = ?", (bike_id,))
        conn.commit()
        flash('Bike deletada com sucesso!', 'success')

    conn.close()
    return redirect(url_for('admin'))

#
@app.route('/inserir_bike', methods=['POST'])
def inserir_bike():
    id = request.form['id']
    tipo = request.form['tipo']
    valor = request.form['valor']
    estoque = request.form['estoque']

    conn = sqlite3.connect('Bikes.db')
    c = conn.cursor()

    # Verifica se o ID já existe no banco de dados
    c.execute("SELECT * FROM bicicletas WHERE id = ?", (id,))
    bike = c.fetchone()
    if bike is not None:
        flash('ID já cadastrado.', 'error')
    else:
        # Insere a nova bike no banco de dados
        c.execute("INSERT INTO bicicletas VALUES (?, ?, ?, ?)",
                  (id, tipo, valor, estoque))
        conn.commit()
        flash('Bike cadastrada com sucesso!', 'success')

    conn.close()
    return redirect(url_for('admin'))

# Rota para processar o formulário de login
@app.route('/login', methods=['POST',])
def login():
    usuario = request.form['usuario'].lower()
    senha = request.form['senha'].lower()

    if usuario == 'admin' and senha == 'admin123':
        print('Administrador logado com sucesso!')
        return redirect(url_for('admin'))

    conn = sqlite3.connect('Bikes.db')
    c = conn.cursor()

    c.execute(
        "SELECT nome, senha FROM usuarios WHERE nome = ? AND senha = ?", (usuario, senha))
    result = c.fetchone()

    if result is not None and result[1] == senha:
        print('Login bem sucedido!')
        return redirect(url_for('lista'))
    else:
        print('Usuário ou senha inválidos.')
        return redirect(url_for('index'))

# Rota para a página de cadastro de cliente
@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

# Rota para processar o formulário de cadastro de cliente
@app.route('/cadastrar', methods=['POST',])
def cadastrar():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']

    # Abrir uma conexão com o banco de dados
    conn = sqlite3.connect('Bikes.db')
    c = conn.cursor()

    try:
        # Inserir o novo usuário no banco de dados
        c.execute(
            "INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)", (nome, email, senha))
        conn.commit()

        # Exibir mensagem de sucesso para o usuário
        flash('Cadastro realizado com sucesso!')
    except sqlite3.IntegrityError:
        # Se o nome ou o e-mail do usuário já existirem no banco de dados, exibir mensagem de erro
        flash('O nome ou o e-mail informados já estão cadastrados. Por favor, tente novamente.')

    # Fechar a conexão com o banco de dados
    conn.close()

    # Redirecionar o usuário de volta para a página inicial
    return redirect(url_for('index'))

# rota de lista de bikes, acessada somente com login
@app.route('/lista')
def lista():
    conn = sqlite3.connect('Bikes.db')
    c = conn.cursor()

    c.execute("SELECT * FROM bicicletas")
    bikes = c.fetchall()

    return render_template('lista.html', bikes=bikes)

@app.route('/alugar/<int:id>', methods = ['POST','GET'])
def alugar(id):

    # Verifica se o usuário já fez um aluguel nesta sessão
    if request.cookies.get('aluguel_feito') == 'true':
        flash('Você já fez um aluguel nesta sessão.', 'error')
        response = make_response(render_template('lista.html', bikes=bikes))
        response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '0'
        return response

    # Busca as informações da bicicleta no banco de dados
    conn = sqlite3.connect('Bikes.db')
    c = conn.cursor()
    c.execute('SELECT * FROM bicicletas WHERE id=?', (id,))
    bike = c.fetchone()

    # Verifica se o estoque é suficiente para realizar o aluguel
    if bike[3] <= 0:
        flash('Estoque indisponível.', 'error')
        response = make_response(render_template('lista.html', bikes=bikes))
        response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '0'
        return response
    else:
        # Diminui o estoque da bike
        c.execute("UPDATE bicicletas SET estoque = ? WHERE id = ?",
                (bike[3] - 1, id))
        conn.commit()
        senha = secrets.token_hex(4)
        flash(f'Segue sua senha para o cadeado eletrônico: {senha}', 'success')
        response = make_response(redirect(url_for('lista')))
        response.set_cookie('aluguel_feito', 'true')
        return response

    # Fecha a conexão com o banco de dados
    c.close()
    conn.close()

@app.route('/logout')
def logout():
    if hasattr(request, 'context'):
        session.pop('username', None)
        session.pop('aluguel_feito', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
