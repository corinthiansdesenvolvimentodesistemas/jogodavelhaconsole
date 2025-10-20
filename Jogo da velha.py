import tkinter as tk
from tkinter import messagebox

jogador = "X"
placar_x = 0
placar_o = 0

def limpar_tabuleiro():
    global jogador
    jogador = "X"
    for i in range(3):
        for j in range(3):
            botoes[i][j].config(text="", state="normal")

def verificar_vencedor():
    for i in range(3):
        if botoes[i][0]["text"] == botoes[i][1]["text"] == botoes[i][2]["text"] != "":
            destacar(botoes[i][0], botoes[i][1], botoes[i][2])
            return botoes[i][0]["text"]
        if botoes[0][i]["text"] == botoes[1][i]["text"] == botoes[2][i]["text"] != "":
            destacar(botoes[0][i], botoes[1][i], botoes[2][i])
            return botoes[0][i]["text"]
    if botoes[0][0]["text"] == botoes[1][1]["text"] == botoes[2][2]["text"] != "":
        destacar(botoes[0][0], botoes[1][1], botoes[2][2])
        return botoes[0][0]["text"]
    if botoes[0][2]["text"] == botoes[1][1]["text"] == botoes[2][0]["text"] != "":
        destacar(botoes[0][2], botoes[1][1], botoes[2][0])
        return botoes[0][2]["text"]
    for i in range(3):
        for j in range(3):
            if botoes[i][j]["text"] == "":
                return None
    return "Empate"

def destacar(a, b, c):
    a.config(bg="lightgreen")
    b.config(bg="lightgreen")
    c.config(bg="lightgreen")

def clique_botao(i, j):
    global jogador, placar_x, placar_o
    if botoes[i][j]["text"] == "" and botoes[i][j]["state"] == "normal":
        botoes[i][j].config(text=jogador)
        vencedor = verificar_vencedor()
        if vencedor:
            if vencedor == "Empate":
                messagebox.showinfo("Empate", "Deu empate!")
            else:
                messagebox.showinfo("Vitória!", f"Jogador {vencedor} venceu!")
                if vencedor == "X":
                    placar_x += 1
                else:
                    placar_o += 1
            atualizar_placar()
            desativar_todos()
            return
        jogador = "O" if jogador == "X" else "X"
        status_label.config(text=f"Vez do jogador {jogador}")

def desativar_todos():
    for i in range(3):
        for j in range(3):
            botoes[i][j].config(state="disabled")

def atualizar_placar():
    placar_label.config(text=f"Placar — X: {placar_x} O: {placar_o}")

def reiniciar_jogo():
    for i in range(3):
        for j in range(3):
            botoes[i][j].config(text="", state="normal", bg="SystemButtonFace")
    global jogador
    jogador = "X"
    status_label.config(text="Vez do jogador X")

def zerar_placar():
    global placar_x, placar_o
    placar_x = 0
    placar_o = 0
    atualizar_placar()
    reiniciar_jogo()

def mostrar_creditos():
    messagebox.showinfo(
        "Créditos",
        "Jogo da Velha 🕹️\n\nDesenvolvido por Mirella Maria\nUsando Python + Tkinter\\nDivirta-se!",
    )

janela = tk.Tk()
janela.title("Jogo da Velha")
janela.resizable(False, False)

placar_label = tk.Label(janela, text="Placar — X: 0 O: 0", font=("Arial", 12))
placar_label.grid(row=0, column=0, columnspan=3, pady=5)

status_label = tk.Label(janela, text="Vez do jogador X", font=("Arial", 11), fg="blue")
status_label.grid(row=1, column=0, columnspan=3)

botoes = [[None for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        botoes[i][j] = tk.Button(
            janela,
            text="",
            width=6,
            height=3,
            font=("Arial", 20),
            command=lambda i=i, j=j: clique_botao(i, j),
        )
        botoes[i][j].grid(row=i + 2, column=j, padx=5, pady=5)

frame_botoes = tk.Frame(janela)
frame_botoes.grid(row=5, column=0, columnspan=3, pady=10)

tk.Button(frame_botoes, text="Reiniciar", width=12, command=reiniciar_jogo).grid(
    row=0, column=0, padx=5
)
tk.Button(frame_botoes, text="Zerar Placar", width=12, command=zerar_placar).grid(
    row=0, column=1, padx=5
)
tk.Button(frame_botoes, text="Créditos", width=12, command=mostrar_creditos).grid(
    row=0, column=2, padx=5
)

janela.mainloop()
