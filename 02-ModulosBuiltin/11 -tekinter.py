# Dando um apelido pa o tkinter
import tkinter as tk

# Criando janela 
window = tk.Tk()
window.geometry("600x300")
window.title("Gerador de Frases")

# Adicionando um frame
frame = tk.Frame(window)
frame.pack(padx=10, pady=10, fill='x',expand=True)

# Adicionando label
label = tk.Label(frame,text= "Hello World")
label.pack(fill='x',expand=True)

# Adicionando Frase para o input
label_lab = tk.Label(frame, text= "Frase")
label_lab.pack(fill='x',expand=True)

# Adicionando input 
frase_inp = tk.Entry(frame)
frase_inp.pack(fill='x',expand=True)

# Alterando Frase da label
def cli():
   label.config(text=frase_inp.get())

# Adicionando button
button = tk.Button(frame, text='Enviar', command=cli)
button.pack()



window.mainloop()

