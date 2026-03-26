import sqlite3
import random

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()
rand_saldo = random.randint(500, 5000)
rand_cpf = random.randint(100000, 999999)

cursor.execute("""CREATE TABLE IF NOT EXISTS contas_bancarias 
               (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
               titular TEXT NOT NULL,
               saldo FLOAT NOT NULL,
               cpf TEXT NOT NULL UNIQUE
               )""")

cursor.execute("""INSERT INTO contas_bancarias
               (titular, saldo, cpf) VALUES
               (?, ?, ?)""",
               ('Cassio', rand_saldo, rand_cpf))


# cursor.execute("""DELETE FROM contas_bancarias WHERE titular = 'Paolo'""")

cursor.execute("""SELECT id, titular, saldo FROM contas_bancarias""")
contas = cursor.fetchall()
cursor.execute("""UPDATE contas_bancarias
               SET saldo = 9000
               WHERE id = 15""")
cursor.execute("""SELECT id, titular, saldo FROM contas_bancarias WHERE id = 15""")
conta_renato = cursor.fetchall()

#--- Vizualization ---
for conta in contas:
    id, titular, saldo = conta
    if id == 15:
        print(f"""ID: {id}
titular: {titular}
saldo: {saldo}
""")
for conta in conta_renato:
    id, titular, saldo = conta
    print(f"""ID: {id}
titular: {titular}
saldo: {saldo}
""")
    
conexao.commit()