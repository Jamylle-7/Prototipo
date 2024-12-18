import psycopg2

def conectardb():
    con = psycopg2.connect(
        host='localhost',
        database='+saude',
        user='postgres',
        password='12345'
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

def verificarlogin(email, senha):
    conexao = conectardb()
    cur = conexao.cursor()
    cur.execute(f"SELECT email, nome FROM usuarios WHERE email = '{email}' AND senha = '{senha}'")
    recset = cur.fetchall()
    cur.close()
    conexao.close()
    return recset

def inserirdados(altura, peso, idade, sexo):
    conexao = conectardb()
    cur = conexao.cursor()
    exito = False
    try:
        sql = f"INSERT INTO usuarios (altura, peso, idade, sexo) VALUES ('{altura}', '{peso}', '{idade}', '{sexo}')"
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

