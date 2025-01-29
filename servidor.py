from flask import Flask, render_template, request, session, url_for
from werkzeug.utils import redirect

import dao

app = Flask(__name__)
app.secret_key = '707070'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/inserirusuario', methods=['POST'])
def inserir_user():
    email = request.form.get('email')
    senha = request.form.get('senha')
    nome = request.form.get('nome')

    if dao.usuario_existe(email):
        msg = 'Usuário já possui cadastro'
    else:
        if dao.inserirusuario(email, nome, senha):
            msg = 'Usuário cadastrado com sucesso'
        else:
            msg = 'Problemas ao cadastrar usuário'
    return render_template('login.html', mensagem=msg)

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    senha = request.form.get('senha')

    resultado = dao.verificarlogin(email, senha)

    if len(resultado) > 0:
        session['login'] = email
        return render_template('user_page.html', user=resultado[0][1])
    else:
        msg = 'Senha ou login incorretos'
        return render_template('login.html', msglogin=msg)

@app.route('/sair')
def fazer_logout():
    session.pop('login', None)
    return render_template('home.html')

@app.route('/pagelogin')
def mostrar_page_login():
    return render_template('login.html')

@app.route('/pagecadastrar')
def mostrar_page_cadastrar():
    return render_template('register.html')

@app.route('/pageagua', methods=['GET','POST'])
def mostrar_page_agua():
    return render_template('hidratacao.html')

@app.route('/pageimc', methods=['GET','POST'])
def mostrar_page_imc():
    return render_template('imc.html')

@app.route('/pageddsaude', methods=['GET','POST'])
def mostrar_page_ddsaude():
    return render_template('dados_saude.html')

@app.route('/pagetmb', methods=['GET','POST'])
def mostrar_page_tmb():
    dados_user = dao.recuperar_dados_user(session['login'])
    #fazer a parte de calcular
    imc = dados_user[0] / dados_user[1]
    return render_template('tmb.html', imc=imc)

@app.route('/pagemetas', methods=['GET','POST'])
def mostrar_page_metas():
    return render_template('metas.html')

@app.route('/pageuser')
def mostrar_page_user():
    email = session.get('email')
    if email:
        return render_template('user_page.html', user=email)
    else:
        return render_template('login.html', msglogin='Por favor, faça login primeiro.')

@app.route('/imc', methods=['POST'])
def calcular_imc():
    peso = request.form.get('peso')
    if ',' in peso:
        peso = peso.replace(',', '.')

    altura = request.form.get('altura')
    if ',' in altura:
        altura = altura.replace(',', '.')

    peso = float(peso)
    altura = float(altura)
    imc = peso / (altura ** 2)
    imc_arredondado = round(imc, 2)
    return render_template('imc.html', imc=imc_arredondado)

@app.route('/agua', methods=['POST'])
def calcular_agua():
    peso = request.form.get('peso')
    if ',' in peso:
        peso = peso.replace(',', '.')
    peso = float(request.form.get('peso'))
    agua = peso * 35
    agua_arredondada = round(agua)
    return render_template('hidratacao.html', agua=agua_arredondada)

@app.route('/tbm', methods=['POST'])
def calcular_tbm():
    peso = request.form.get('peso')
    if ',' in peso:
        peso = peso.replace(',', '.')
    altura = request.form.get('altura')
    if ',' in altura:
        altura = altura.replace(',', '.')
    idade = request.form.get('idade')
    sexo = request.form.get('sexo')

    peso = float(peso)
    altura = float(altura)
    idade = int(idade)

    if sexo == 'masculino':
        tbm = 88.36 + (13.4 * peso) + (4.8 * altura) - (5.7 * idade)
    else:
        tbm = 447.6 + (9.2 * peso) + (3.1 * altura) - (4.3 * idade)

    tbm_arredondado = round(tbm, 2)

    return render_template('tmb.html', tmb=tbm_arredondado)


@app.route('/inserirdados', methods=['POST'])
def inserir_dados():
    altura = request.form.get('')
    peso = request.form.get('')
    alt = request.form.get('')
    alt = request.form.get('')
    login = session['login']

    if dao.inserirdados(altura,alt,alt,alt,login):
        return render_template('userpage.html')
    else:
        asdasd




if __name__ == '__main__':
    app.run(debug=True)
