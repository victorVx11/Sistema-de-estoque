import tkinter as tk  # Biblioteca usada para criar janelas.
import customtkinter as ctk
from tkinter import ttk, messagebox
import sqlite3



# Comandos para iniciar o programa:
# cd .\Sistema_de_Estoque
# py main.py


# Abre a primeira janela de login.
def abrir_login():
    tela_login = tk.Frame(
        janela,
        bg="#f1f5f9"
    )
    tela_login.place(
        relx=0,
        rely=0,
        relwidth=1,
        relheight=1
    )

    # Faixa superior.
    faixa_superior = tk.Frame(
        tela_login,
        bg="#3757BE",
        height=55
    )
    faixa_superior.place(
        x=0,
        y=0,
        relwidth=1
    )

    # Faixa lateral.
    faixa_lateral = tk.Frame(
        tela_login,
        bg="#3757BE",
        width=55
    )
    faixa_lateral.place(
        x=0,
        y=0,
        relheight=1
    )

    # Título da tela de login.
    titulo_login = tk.Label(
        tela_login,
        text="Tela de Login",
        font=("Arial", 28, "bold"),
        bg="#f1f5f9",
        fg="#030303"
    )
    titulo_login.pack(pady=60)

    # Caixa onde o usuário informa o login.
    label_usuario = tk.Label(
        tela_login,
        text="Usuário",
        font=("Arial", 12),
        bg="#f1f5f9"
    )
    label_usuario.pack()

    entrada_usuario = tk.Entry(
        tela_login,
        font=("Arial", 14),
        width=25
    )
    entrada_usuario.pack(pady=(5, 15))

    # Caixa onde o usuário informa a senha.
    label_senha = tk.Label(
        tela_login,
        text="Senha",
        font=("Arial", 12),
        bg="#f1f5f9"
    )
    label_senha.pack()

    entrada_senha = tk.Entry(
        tela_login,
        font=("Arial", 14),
        width=25,
        show="*"
    )
    entrada_senha.pack(pady=(5, 15))

    def verificar_login():
        usuario = entrada_usuario.get().strip()
        senha = entrada_senha.get().strip()

        if usuario == "adm" and senha =="1234":
            tela_login.destroy()
        else:
            messagebox.showerror(
                "Erro de login",
                "Usuario ou senha incorretos."
            )

    ctk.CTkButton(
        tela_login,
        text="Entrar",
        command=verificar_login,
        width=200,
        height=45,
        corner_radius=18,
        fg_color="#163c9e",
        hover_color="#eef2f5",
        font=("Arial", 14, "bold")
    ).pack(pady=10)


def criar_banco():
    conexao = sqlite3.connect("estoque.db")
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            preco REAL NOT NULL
        )
    """)

    # conexao conecta o programa ao banco chamado estoque.db.
    # cursor permite executar comandos dentro do banco.
    conexao.commit()
    conexao.close()


def limpar_conteudo():
    for elemento in conteudo.winfo_children():
        elemento.destroy()


def abrir_cadastro():
    limpar_conteudo()

    # Caixas onde serão informados os dados do produto.
    tk.Label(
        conteudo,
        text="Cadastrar produto",
        font=("Arial", 22, "bold"),
        bg="#f1f5f9",
        fg="#1e293b"
    ).pack(pady=(40, 25))

    tk.Label(
        conteudo,
        text="Nome do produto:",
        font=("Arial", 13),
        bg="#f1f5f9",
        fg="#334155"
    ).pack()

    # entrada_nome ficará com o texto informado pelo usuário.
    entrada_nome = ctk.CTkEntry(
        conteudo,
        width=350,
        height=40,
        placeholder_text="Exemplo: Arroz"
    )
    entrada_nome.pack(pady=(5, 15))

    tk.Label(
        conteudo,
        text="Quantidade:",
        font=("Arial", 13),
        bg="#f1f5f9",
        fg="#334155"
    ).pack()

    entrada_quantidade = ctk.CTkEntry(
        conteudo,
        width=350,
        height=40,
        placeholder_text="Exemplo: 10"
    )
    entrada_quantidade.pack(pady=(5, 15))

    tk.Label(
        conteudo,
        text="Preço:",
        font=("Arial", 13),
        bg="#f1f5f9",
        fg="#334155"
    ).pack()

    entrada_preco = ctk.CTkEntry(
        conteudo,
        width=350,
        height=40,
        placeholder_text="Exemplo: 15.90"
    )
    entrada_preco.pack(pady=(5, 20))

    def salvar_produtos():
        nome = entrada_nome.get().strip()
        quantidade_texto = entrada_quantidade.get().strip()
        preco_texto = entrada_preco.get().strip().replace(",", ".")

        if nome == "" or quantidade_texto == "" or preco_texto == "":
            messagebox.showwarning(
                "Campos vazios",
                "Preencha todos os campos."
            )
            return

        try:
            quantidade = int(quantidade_texto)
            preco = float(preco_texto)
        except ValueError:
            messagebox.showerror(
                "Dados inválidos",
                "Digite um número inteiro na quantidade e um número no preço."
            )
            return

        if quantidade < 0 or preco < 0:
            messagebox.showwarning(
                "Valores inválidos",
                "A quantidade e o preço não podem ser negativos."
            )
            return

        conexao = sqlite3.connect("estoque.db")
        cursor = conexao.cursor()

        cursor.execute(
            """
            INSERT INTO produtos (nome, quantidade, preco)
            VALUES (?, ?, ?)
            """,
            (nome, quantidade, preco)
        )

        conexao.commit()
        conexao.close()

        entrada_nome.delete(0, tk.END)
        entrada_quantidade.delete(0, tk.END)
        entrada_preco.delete(0, tk.END)

        messagebox.showinfo(
            "Sucesso",
            "Produto cadastrado com sucesso!"
        )

    # Cria o botão de salvar produto.
    ctk.CTkButton(
        conteudo,
        text="Salvar produto",
        command=salvar_produtos,
        width=200,
        height=45,
        corner_radius=18,
        fg_color="#16a34a",
        hover_color="#15803d",
        font=("Arial", 14, "bold")
    ).pack(pady=10)

#janela Tabelas com os produtos
def abrir_produtos():
    limpar_conteudo()
    tk.Label(
        conteudo,
        text="Produtos Cadastrados",
        font=("Arial", 22, "bold"),
        bg="#f1f5f9",
        fg="#1e293b"
    ).pack(pady=(40, 25))


#Tabelas dos Produtos
    tabela = ttk.Treeview(
        conteudo,
        columns = ("id","nome","quantidade","preco"),
        show = "headings"
    )

    tabela.heading("id",text="ID",)
    tabela.heading("nome",text="Nome")
    tabela.heading("quantidade",text="Quantidade")
    tabela.heading("preco",text="Preço")

    tabela.column(
        "id",
        width=70,
        anchor="center"
    )
    tabela.column(
            "nome",
            width=250,
            anchor="center"
    )
    tabela.column(
            "quantidade",
            width=120,
            anchor="center"
        )
    tabela.column(
            "preco",
            width=120,
            anchor="center"
        )


    conexao = sqlite3.connect("estoque.db")
    cursor = conexao.cursor()
    cursor.execute( """

        SELECT  id,nome, quantidade, preco
        FROM produtos
            """)
            
    produtos = cursor.fetchall()
    conexao.close()

    for produto in produtos:
        tabela.insert("", "end", values=produto)

    tabela.pack()

    #Botao de excluir o produto na Tabela 
    def excluir_produto():
        selecionado = tabela.selection()

        if not selecionado:
            messagebox.showwarning(
                "Nenhum produto selecionado",
                "Selecione um produto da tabela para excluir."
            )
            return

        item_selecionado = selecionado[0]
        valores = tabela.item(item_selecionado, "values")
        id_produto = valores[0]

        conexao = sqlite3.connect("estoque.db")
        cursor = conexao.cursor()

        cursor.execute(
            "DELETE FROM produtos WHERE id = ?",
            (id_produto,)
        )

        conexao.commit()
        conexao.close()
        tabela.delete(item_selecionado)

        messagebox.showinfo(
            "Produto excluído",
            "O produto foi excluído com sucesso!"
        )

#criando o botao
    ctk.CTkButton(
    conteudo,
    text="Excluir produto",
    command=excluir_produto,
    width=200,
    height=45,
    corner_radius=18,
    fg_color="#dc2626",
    hover_color="#b91c1c"
    ).pack(pady=15)
   

def abrir_movimentacoes():
    limpar_conteudo()
    tk.Label(
        conteudo,
        text="Entrada e sainda de estoque",
        font=("Arial",22,"bold"),
        bg="#f1f5f9",
        fg="#1e293b"
    ).pack(pady=(40,25))

    entrada_id = ctk.CTkEntry(
        conteudo,
         width=350,
         height=40,
         placeholder_text="Exemplo: 1"
         )
    entrada_id.pack(pady=(5, 20))

    #Quantidade de saida 
    tk.Label(
        conteudo,
        text="Quantidade",
        font=("Arial",22,"bold"),
        bg="#f1f5f9",
        fg="#1e293b"
    ).pack(pady=(20,15))

    entrada_quantidade =ctk.CTkEntry(
        conteudo,   
        width=350,
        height=40,
        placeholder_text="Exemplo: 10"

    )
    entrada_quantidade.pack(pady=(5, 20))

    def registrar_entrada():
        try:
            id_produto = int(entrada_id.get())
            Qnt = int(entrada_quantidade.get())
        except ValueError:
            messagebox.showwarning(
                "Dados inválidos",
                "Digite um ID e uma quantidade válidos."
            )
            return

        if Qnt <= 0:
            messagebox.showwarning(
                "Quantidade inválida",
                "A quantidade deve ser maior que zero."
            )
            return

        conexao = sqlite3.connect("estoque.db")
        cursor = conexao.cursor()

        cursor.execute(
            "SELECT id FROM produtos WHERE id = ?",
            (id_produto,)
        )
        if cursor.fetchone() is None:
            conexao.close()
            messagebox.showerror("Erro", "Produto não encontrado.")
            return

        cursor.execute("""
            UPDATE produtos
            SET quantidade = quantidade + ?
            WHERE id = ?
            """, (Qnt, id_produto))
        conexao.commit()
        conexao.close()
        entrada_id.delete(0, tk.END)
        entrada_quantidade.delete(0, tk.END)
        messagebox.showinfo("Sucesso", "Entrada registrada com sucesso!")

    def registrar_saida():
        try:
            id_produto = int(entrada_id.get())
            Qnt = int(entrada_quantidade.get())
        except ValueError:
            messagebox.showwarning(
                "Dados inválidos",
                "Digite um ID e uma quantidade válidos."
            )
            return

        if Qnt <= 0:
            messagebox.showwarning(
                "Quantidade inválida",
                "A quantidade deve ser maior que zero."
            )
            return

        conexao = sqlite3.connect("estoque.db")
        cursor = conexao.cursor()
        cursor.execute(
            "SELECT quantidade FROM produtos WHERE id = ?",
            (id_produto,)
            )

        produto = cursor.fetchone()
        if produto is None:
            conexao.close()
            messagebox.showerror("Erro", "Produto não encontrado.")
            return

        if Qnt > produto[0]:
            messagebox.showwarning(
                "Estoque insuficiente",
                "Não há quantidade suficiente para registrar essa saída."
            )
            conexao.close()
            return
        cursor.execute("""
            UPDATE produtos
            SET quantidade = quantidade - ?
            WHERE id = ?
            """, (Qnt, id_produto))
        conexao.commit()
        conexao.close()
        entrada_id.delete(0, tk.END)
        entrada_quantidade.delete(0, tk.END)

        messagebox.showinfo("Sucesso", "Saída registrada com sucesso!")

    #Button de entrada
    ctk.CTkButton(
        conteudo,
        text="Registrar entrada",
        width=200,
        height=45,
        fg_color="#00762b",
        corner_radius=18,
        command=registrar_entrada
    ).pack(pady=10)

    #Button de saida 
    ctk.CTkButton(
        conteudo,
        text="Registrar saida",
        width=200,
        height=45,
        corner_radius=18,
        fg_color="#d61515",
        command=registrar_saida
    ).pack(pady=10)


# Cria a janela principal do programa.
janela = tk.Tk()
janela.title("Sistema de Controle de Estoque")
janela.geometry("1000x600")
janela.configure(bg="#f1f5f9")

# Título.
titulo = tk.Label(
    janela,
    text="Sistema de Controle de Estoque",
    font=("Arial", 24, "bold"),
    bg="#1e3a8a",
    fg="white",
    pady=20
)
titulo.pack(fill="x")

# Menu lateral.
menu = tk.Frame(
    janela,
    bg="#172554",
    width=220
)
menu.pack(side="left", fill="y")
menu.pack_propagate(False)

# Título do menu.
tk.Label(
    menu,
    text="MENU",
    font=("Arial", 16, "bold"),
    bg="#172554",
    fg="white",
    pady=20
).pack()

botoes = [
    ("Cadastrar produto", abrir_cadastro),
    ("Listar produtos", abrir_produtos),
    ("Entrada e saída", abrir_movimentacoes),
]

for texto, comando in botoes:
    ctk.CTkButton(
        menu,
        text=texto,
        command=comando,
        height=45,
        corner_radius=18,
        fg_color="#2563eb",
        hover_color="#1d4ed8",
        text_color="white",
        font=("Arial", 14, "bold")
    ).pack(fill="x", padx=15, pady=8)

# Área principal.
conteudo = tk.Frame(
    janela,
    bg="#f1f5f9"
)
conteudo.pack(side="right", fill="both", expand=True)

tk.Label(
    conteudo,
    text="Bem-vindo ao sistema!",
    font=("Arial", 22, "bold"),
    bg="#f1f5f9",
    fg="#1e293b"
).pack(pady=(100, 10))

tk.Label(
    conteudo,
    text="Escolha uma opção no menu lateral.",
    font=("Arial", 14),
    bg="#f1f5f9",
    fg="#64748b"
).pack()


criar_banco()
#abrir_login()
janela.mainloop()   
