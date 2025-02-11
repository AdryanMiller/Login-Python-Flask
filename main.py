from flask import Flask, render_template, redirect, request, flash

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
    
    if nome == 'adryan' and senha == '123':
        return render_template('home.html')
    else:
        flash('Usuario invalido')
        return redirect('/')

    return redirect('/')







if __name__ in "__main__":
    app.run(debug=True)