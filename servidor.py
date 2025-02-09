from flask import *
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

@app.route('/voltar')
def voltar():
    return render_template('user_page.html')

@app.route('/pagelogin')
def mostrar_page_login():
    return render_template('login.html')

@app.route('/pagecadastrar')
def mostrar_page_cadastrar():
    return render_template('register.html')

@app.route('/pageagua', methods=['GET','POST'])
def mostrar_page_agua():
    dados_user = dao.recuperar_dados_user(session['login'])
    agua = float(dados_user[0][1]) * 35
    return render_template('hidratacao.html', agua=agua)

@app.route('/pageimc', methods=['GET','POST'])
def mostrar_page_imc():
    dados_user = dao.recuperar_dados_user(session['login'])
    peso = request.form.get('peso')
    imc = float(dados_user[0][2]) / float(dados_user[0][1]) ** 2
    return render_template('imc.html', imc=imc)

@app.route('/pageddsaude', methods=['GET','POST'])
def mostrar_page_ddsaude():
    return render_template('dados_saude.html')

@app.route('/pageuser')
def mostrar_page_user():
    email = session.get('email')
    if email:
        return render_template('user_page.html', user=email)
    else:
        return render_template('login.html', msglogin='Por favor, faça login primeiro.')


@app.route('/inserirdados', methods=['POST'])
def inserir_dados():
    altura = request.form.get('altura')
    peso = request.form.get('peso')
    idade = request.form.get('idade')
    sexo = request.form.get('sexo')
    login = session.get('login')


    if dao.inserirdados(altura, peso, idade, sexo, login):
        return render_template('user_page.html')
    else:
        return render_template('dados_saude.html', msgsaude='Erro ao inserir dados. Login não existe.')


@app.route('/adicionarmetas', methods=['POST'])
def adicionar_nova_meta():
    meta = request.form.get('meta')
    login = session.get('login')

    if dao.adicionarmetas(login,meta):
        return render_template('add_meta.html')
    else:
        return render_template('add_meta.html', msgsaude='Erro ao inserir meta.')


@app.route('/listar_metas', methods=['POST'])
def listar_meta():
    login = session['login']
    metas = dao.listarmetas(login)
    if len(metas) > 0:
        return render_template('listar_metas.html', metas=metas)
    else:
        return render_template('listar_meta.html', msgsaude='Erro ao listar meta.')

if __name__ == '__main__':
    app.run(debug=True)
