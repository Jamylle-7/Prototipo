import psycopg2

def conectardb():
    con = psycopg2.connect(
        host='dpg-cu8ghqogph6c73cpeo70-a.oregon-postgres.render.com',
        database='data_base_ktmy',
        user='data_base_ktmy_user',
        password='7VE6S6zoQ1T7Ke8XIjIydkGWPUg4ekMB'
    )
    return con

def inserirusuario(email, nome, senha):
    conexao = conectardb()
    cur = conexao.cursor()
    exito = False
    try:
        sql = f"INSERT INTO usuarios (email, nome, senha) VALUES ('{email}', '{nome}', '{senha}')"
        cur.execute(sql)
    except psycopg2.Error:
        conexao.rollback()
        print(f"Erro ao inserir usuário")
        exito = False
    else:
        conexao.commit()
        exito = True

    conexao.close()
    return exito

def usuario_existe(email):
    conexao = conectardb()
    cur = conexao.cursor()
    cur.execute(f"SELECT email FROM usuarios WHERE email = '{email}'")
    usuario = cur.fetchone()
    cur.close()
    conexao.close()
    return usuario is not None


def verificarlogin(email, senha):
    conexao = conectardb()
    cur = conexao.cursor()
    cur.execute(f"SELECT email, nome FROM usuarios WHERE email = '{email}' AND senha = '{senha}'")
    recset = cur.fetchall()
    cur.close()
    conexao.close()
    return recset

def inserirdados(altura, peso, idade, sexo, login):
    conexao = conectardb()
    cur = conexao.cursor()
    exito = False
    try:
        sql = f"INSERT INTO usuarios (altura, peso, idade, sexo, login) VALUES ('{altura}', '{peso}', '{idade}', '{sexo}', '{login}')"
        cur.execute(sql)
    except psycopg2.Error:
        conexao.rollback()
        print(f"Erro ao inserir dados do usuário")
        exito = False
    else:
        conexao.commit()
        exito = True

    conexao.close()
    return exito

def calcularimc(altura, peso):
    conexao = conectardb()
    cur = conexao.cursor()
    cur.execute(f"SELECT altura, peso FROM usuarios WHERE altura= '{altura}' AND peso = '{peso}'")
    recset = cur.fetchall()
    cur.close()
    conexao.close()
    return recset

def calcular_tbm(altura, peso, idade, sexo):
    conexao = conectardb()
    cur = conexao.cursor()
    cur.execute(f"SELECT altura, peso FROM usuarios WHERE altura= '{altura}' AND peso = '{peso}' AND idade = '{idade}' AND sexo = '{sexo}'")
    recset = cur.fetchall()
    cur.close()
    conexao.close()
    return recset


def recuperar_dados_user(login):
    conexao = conectardb()
    cur = conexao.cursor()
    cur.execute(f"SELECT altura, peso, idade, sexo FROM XXXXXX WHERE login = '{login}'")
    recset = cur.fetchall()
    cur.close()
    conexao.close()
    return recset

