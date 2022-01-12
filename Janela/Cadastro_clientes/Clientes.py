import sqlite3
import tkinter as tk
import pandas as pd

#----------------------------------------------
#Para criação do banco de dados retira o comentário (#) da linha 9 à 23 somente a primeira vez que rodar o cód,
#depois, basta comentar novamente.

#Criando o Banco de Dados
# conexao = sqlite3.connect('Clientes.db')
#
# c = conexao.cursor()
#
# c.execute(''' CREATE TABLE clientes (
#     Nome text,
#     Sobrenome text,
#     Email text,
#     Telefone text
#     )
# ''')
#
# conexao.commit()
# conexao.close()
#-----------------------------------------------
#Criando as funções

def cadastrar_cliente():
    conexao = sqlite3.connect('Clientes.db')
    c = conexao.cursor()
    c.execute("INSERT INTO clientes VALUES (:nome,:sobrenome,:email,:telefone)",
         {
        'nome': entry_nome.get(),
        'sobrenome': entry_sobrenome.get(),
        'email': entry_email.get(),
        'telefone': entry_telefone.get()
            }
              )

    conexao.commit()
    conexao.close()

    #criando uma função para limpar a tela após inserir registros
    entry_nome.delete(0, "end")
    entry_sobrenome.delete(0, "end")
    entry_email.delete(0, "end")
    entry_telefone.delete(0, "end")

#Criando a função para exportar as informações do banco em formato xlxs
def exportar_cliente():
    conexao = sqlite3.connect('Clientes.db')
    c = conexao.cursor()

    c.execute("SELECT *, oid FROM clientes") #Criando um select da tabela clientes
    clientes_cadastrados = c.fetchall() #Onde eu utilizo a estrutura fetchall para retornar todos os dados da mesma
    clientes_cadastrados = pd.DataFrame(clientes_cadastrados, columns=['Nome','Sobrenome','Email','Telefone','Id_banco']) #em seguida transformo a variável em um Dataframe
    clientes_cadastrados.to_excel('banco_clientes.xlsx') #Para que assim eu possa exportar como Excel

    conexao.commit()
    conexao.close()


#-----------------------------------------------
janela = tk.Tk() #estartando a janela
janela.title("Cadastro de Clientes") #Inserindo um título na janela

#Criando as Labels:
label_nome = tk.Label(janela, text="Nome")
label_nome.grid(row=0, column=0, padx=10, pady=10)

label_sobrenome = tk.Label(janela, text="Sobrenome")
label_sobrenome.grid(row=1, column=0, padx=10, pady=10)

label_email = tk.Label(janela, text="Email")
label_email.grid(row=2, column=0, padx=10, pady=10)

label_telefone = tk.Label(janela, text="Telefone")
label_telefone.grid(row=3, column=0, padx=10, pady=10)

#-------------------------------------------------------
#Entrys
entry_nome = tk.Entry(janela, text="Nome", width=30)
entry_nome.grid(row=0, column=2, padx=10, pady=10)

entry_sobrenome = tk.Entry(janela, text="Sobrenome", width=30)
entry_sobrenome.grid(row=1, column=2, padx=10, pady=10)

entry_email = tk.Entry(janela, text="Email", width=30)
entry_email.grid(row=2, column=2, padx=10, pady=10)

entry_telefone = tk.Entry(janela, text="Telefone", width=30)
entry_telefone.grid(row=3, column=2, padx=10, pady=10)

#Botões
botao_Cadastrar = tk.Button(janela, text="Cadastrar Cliente", command = cadastrar_cliente)
botao_Cadastrar.grid(row=4, column=0, padx=10, pady=10, columnspan=2, ipadx=80)

botao_exportar = tk.Button(janela, text="Exportar Cliente", command = exportar_cliente)
botao_exportar.grid(row=4, column=2, padx=10, pady=10, columnspan=2, ipadx=80)

#Obs: ipadx=80 - Basicamente serve para alargar uma estrutura especifíca
janela.mainloop()