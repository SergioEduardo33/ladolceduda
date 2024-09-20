from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Conectar ao banco de dados SQLite
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Rota para a página principal com o formulário
@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        produto = request.form['produto']
        quantidade = request.form['quantidade']
        valor = request.form['valor']
        data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        conn = get_db_connection()
        conn.execute('INSERT INTO vendas (produto, quantidade, valor, data_hora) VALUES (?, ?, ?, ?)',
                     (produto, quantidade, valor, data_hora))
        conn.commit()
        conn.close()
        return redirect(url_for('registros'))

    return render_template('index.html')

# Rota para visualizar registros
@app.route('/registros')
def registros():
    conn = get_db_connection()
    vendas = conn.execute('SELECT * FROM vendas').fetchall()
    conn.close()
    return render_template('registros.html', vendas=vendas)

# Rota para deletar registro
@app.route('/delete/<int:id>')
def delete(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM vendas WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('registros'))

# Rota para editar registro
@app.route('/edit', methods=('POST',))
def edit():
    id = request.form['id']
    produto = request.form['produto']
    quantidade = request.form['quantidade']
    valor = request.form['valor']

    conn = get_db_connection()
    conn.execute('UPDATE vendas SET produto = ?, quantidade = ?, valor = ? WHERE id = ?',
                 (produto, quantidade, valor, id))
    conn.commit()
    conn.close()
    
    return redirect(url_for('registros'))

if __name__ == '__main__':
    app.run(debug=True)
