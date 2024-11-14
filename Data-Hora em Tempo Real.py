import tkinter as tk
from tkinter import ttk
from datetime import datetime

def atualizar_hora():
    # Obtém a data e hora atual
    agora = datetime.now()
    # Formata a string da data e hora
    data_hora = agora.strftime('%d/%m/%Y %H:%M:%S')
    # Atualiza o rótulo com a nova data e hora
    rotulo.config(text=data_hora)
    # Chama a função novamente após 1000 ms (1 segundo)
    root.after(1000, atualizar_hora)

# Cria a janela principal
root = tk.Tk()
root.title("Relógio em Tempo Real")
root.configure(bg="#ADD8E6")  # Cor de fundo azul-claro

# Cria um rótulo para exibir a data e hora
rotulo = ttk.Label(root, font=('Arial', 30), background="#ADD8E6")
rotulo.pack(pady=20)

# Chama a função para atualizar a hora pela primeira vez
atualizar_hora()

# Inicia o loop da interface gráfica
root.mainloop()
