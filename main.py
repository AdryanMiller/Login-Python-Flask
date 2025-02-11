from flask import Flask, render_template, redirect, request, flash
import json

app = Flask('__name__')
app.config['SECRET_KEY'] = 'IGNORE'

@app.route('/')

def home():
    return render_template('login.html')

@app.route('/login', methods =['POST'])
def login():

    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')
    
    with open('usuarios.json') as usuariosTemp:
        usuarios = json.load(usuariosTemp)

        cont= 0
        for usuario in usuarios:

            cont += 1
            if usuario['nome'] == nome and usuario['email'] == email and usuario['senha'] == senha:
                return render_template('home.html')
            
            if cont >= len(usuarios):
                flash('Usuario Invalido')
                return redirect('/')






if __name__ in "__main__":
    app.run(debug=True)