from flask import Flask, render_template, redirect, request, flash
import json

app = Flask('__name__')
app.config['SECRET_KEY'] = 'IGNORE'


@app.route('/')

def home():
    return render_template('cadastrarUsuario.html')

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

            if nome == 'adm' and senha == '000':
                return render_template("cadastrarUsuario.html")
            
            if usuario['nome'] == nome or usuario['email'] == email and usuario['senha'] == senha:
                return render_template('home.html')
            
            if cont >= len(usuarios):
                flash('Usuario Invalido')
                return redirect('/')


@app.route('/cadastrarUsuario', methods=['POST'])
def cadastrarUsuario():
    user = []
    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')
    user = [

        {
            "nome": nome,
            "email": email,
            "senha": senha
        }
    ]
    with open('usuarios.json') as usuariosTemp:
            usuarios = json.load(usuariosTemp)

    usuariosNovo= usuarios + user
    with open('usuarios.json', 'w') as gravarTemp:
        json.dump(usuariosNovo, gravarTemp, indent= 5)
        
    return render_template("login.html")



if __name__ in "__main__":
    app.run(debug=True)