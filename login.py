from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox
import random

# Cores
co0 = "#DD2828"
co1 = "#FEFFFF"
co2 = "#C41F1F"
co3 = "#f34e64"
co4 = "#292525"

# Criando janela de login
janela = Tk()
janela.title("lais - Login")
janela.geometry("310x300")
janela.configure(bg=co1)
janela.resizable(False, False)

# Frames do login
frame_cima = Frame(janela, width=310, height=50, bg=co1, relief="flat")
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)
frame_baixo = Frame(janela, width=310, height=300, bg=co1, relief="flat")
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# Configuração frame_cima (login)
l_nome_login = Label(frame_cima, text="LOGIN", height=1, anchor=NE, font=('Ivy', 25), bg=co1, fg=co4)
l_nome_login.place(x=5, y=5)

l_linha_login = Label(frame_cima, width=275, text="", height=1, anchor=NW, font=('Ivy', 1), bg=co2)
l_linha_login.place(x=10, y=45)

credenciais = ['lais', '2310l']

def iniciar_jogo_namoro():
    # Criar a nova janela para o jogo
    janela_jogo = Toplevel(janela)
    janela_jogo.title("QUER NAMORAR COMIGO?")
    janela_jogo.geometry("400x200")
    janela_jogo.resizable(False, False)
    janela_jogo.configure(bg="#F0F0F0")

    def move_Button(event):
        x = random.randint(50, 350)
        y = random.randint(50, 150)

        # Evitar colisão com o botão SIM
        if (x < sim_button.winfo_x() - 50 or x > sim_button.winfo_x() + 50) or \
           (y < sim_button.winfo_y() - 50 or y > sim_button.winfo_y() + 50):
            nao_button.place(x=x, y=y)

    def show_response(response):
        if response == "sim":
            label_response.config(text="VOCÊ DISSE SIM!", fg="#32CD32")
            sim_button.config(state=DISABLED) # Desabilita o botão SIM
            nao_button.config(state=DISABLED) # Desabilita o botão NÃO
        elif response == "nao":
            label_response.config(text="VOCÊ DISSE NÃO!", fg="#FF6347")
            sim_button.config(state=DISABLED) # Desabilita o botão SIM
            nao_button.config(state=DISABLED) # Desabilita o botão NÃO


    sim_button = Button(janela_jogo, text="SIM", width=10, command=lambda: show_response("sim"))
    nao_button = Button(janela_jogo, text="NÃO", width=10, command=lambda: show_response("nao"))

    sim_button.configure(bg='#32CD32', fg='#ffffff', font=('Helvetica', 12))
    nao_button.configure(bg='#FF6347', fg='#ffffff', font=('Helvetica', 12))

    label_question = Label(janela_jogo, text="QUER NAMORAR COMIGO?", font=('Helvetica', 14), bg=("#f0f0f0"))
    label_response = Label(janela_jogo, text="", font=('Helvetica', 14), bg=("#f0f0f0"))

    sim_button.place(x=100, y=75)
    nao_button.place(x=250, y=75)
    label_question.place(x=50, y=20)
    label_response.place(x=120, y=130)

    nao_button.bind("<Motion>", move_Button)


def verificar_senha():
    nome = e_nome.get()
    senha = str(e_pass.get())

    if nome == 'admin' and senha == 'admin':
        messagebox.showinfo('Login', 'Seja bem vindo Admin!!!')
        nova_janela(nome)
    elif credenciais[0] == nome and credenciais[1] == senha:
        messagebox.showinfo('Login', 'Seja bem vindo de volta ' + credenciais[0])

        # Limpar a janela de login para exibir a nova interface
        for widget in janela.winfo_children():
            widget.destroy()

        nova_janela(nome)
    else:
        messagebox.showwarning('Error', 'Verifique o nome de usuario ou a palavra passe')

def nova_janela(usuario):
    # Recria os frames na janela principal para a nova interface
    global frame_cima, frame_baixo
    frame_cima = Frame(janela, width=310, height=50, bg=co1, relief="flat")
    frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)
    frame_baixo = Frame(janela, width=310, height=300, bg=co1, relief="flat")
    frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

    l_nome_saudacao = Label(frame_cima, text="Usuario: " + usuario, height=1, anchor=NE, font=('Ivy', 20), bg=co1, fg=co4)
    l_nome_saudacao.place(x=5, y=5)

    l_linha_saudacao = Label(frame_cima, width=275, text="", height=1, anchor=NW, font=("Ivy", 1), bg=co2)
    l_linha_saudacao.place(x=10, y=45)

    l_bem_vindo = Label(frame_baixo, text="Seja bem vindo, " + usuario, height=1, anchor=NE, font=('Ivy', 20), bg=co1, fg=co4)
    l_bem_vindo.place(x=5, y=10)

    # Botão para iniciar o jogo "Quer namorar comigo?"
    botao_iniciar_jogo = Button(frame_baixo, text="Iniciar Jogo", width=20, height=2, bg=co2, fg=co1, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=iniciar_jogo_namoro)
    botao_iniciar_jogo.place(x=60, y=100)


# Elementos da interface de login
l_nome_entrada = Label(frame_baixo, text="Nome *", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_nome_entrada.place(x=10, y=20)
e_nome = Entry(frame_baixo, width=25, justify='left', font=("", 15), highlightbackground=co1, relief="solid")
e_nome.place(x=14, y=50)

l_pass_entrada = Label(frame_baixo, text="Senha *", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_pass_entrada.place(x=10, y=90)
e_pass = Entry(frame_baixo, show='*', width=25, justify='left', font=("", 15), highlightbackground=co1, relief="solid")
e_pass.place(x=14, y=120)

botao_confirmar = Button(frame_baixo, text="Entrar", width=39, height=2, bg=co2, fg=co1, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE, command=verificar_senha)
botao_confirmar.place(x=15, y=180)

janela.mainloop()