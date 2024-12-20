from flask import Flask, render_template, request
import dao

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/inserirusuario', methods=['POST'])
def inserir_user():
    email = request.form.get('email')
    senha = request.form.get('senha')
    nome = request.form.get('nome')

    if dao.inserirusuario(email, nome, senha):
        msg = 'Usuário cadastrado com sucesso'
    else:
        msg = 'Problemas ao cadastrar usuário'
    return render_template('register.html', mensagem=msg)

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    senha = request.form.get('senha')

    resultado = dao.verificarlogin(email, senha)
    print(resultado)
    if len(resultado) > 0:
        return render_template('user_page.html', user=resultado[0][1])
    else:
        msg = 'Senha ou login incorretos'
        return render_template('login.html', msglogin=msg)

@app.route('/pagelogin')
def mostrar_page_login():
    return render_template('login.html')

@app.route('/pagecadastrar')
def mostrar_page_cadastrar():
    return render_template('register.html')

@app.route('/pageuser')
def mostrar_page_user():
    return render_template('user_page.html')

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
    return render_template('user_page.html', imc=imc_arredondado)

@app.route('/agua', methods=['POST'])
def calcular_agua():
    peso = request.form.get('peso')
    if ',' in peso:
        peso = peso.replace(',', '.')
    peso = float(request.form.get('peso'))
    agua = peso * 35
    agua_arredondada = round(agua)
    return render_template('user_page.html', agua=agua_arredondada)

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

    return render_template('user_page.html', tmb=tbm_arredondado)

if __name__ == '__main__':
    app.run(debug=True)