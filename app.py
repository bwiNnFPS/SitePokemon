from flask import Flask, render_template, request, redirect
lista=[]

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('Home.html', Titulo='Bem vindo ao site de Pokemon')

@app.route('/pokemon')
def pokemon():
    return render_template('Pokemon.html', Banana='Melhores Pokemon')

@app.route('/sobre')
def sobre():
    return render_template('Sobre.html', Banana='Sobre nosso site')

@app.route('/cadastro')
def cadastro():
    return render_template('Cadastro.html', Banana='Cadastro de pokemon')

@app.route('/exibir')
def exibir():
    return render_template('Exibir.html', Banana='pokemons cadastrados', lista=lista)

@app.route('/criar', methods=['POST'])
def criar():
    numero = request.form['numero']
    nome = request.form['nome']
    tipo = request.form['tipo']
    altura = request.form['altura']
    peso = request.form['peso']
    pokemon = [numero, nome, tipo, altura, peso]
    lista.append(pokemon)
    return  redirect ('/exibir')

if __name__ == '__main__':
    app.run()
