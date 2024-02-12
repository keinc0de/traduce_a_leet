import tkinter as tk
from tkinter import ttk
from leet import Diccionario


class Interfaz(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('430x220')

        fo = ('Consolas', 10, 'bold')
        fo2 = ('Consolas', 14, 'bold')
        fondo = '#0E0515'
        color = '#C7FF1E'
        dark = ttk.Style(self)
        dark.theme_use('alt')
        dark.configure(
            'TButton',
            background=fondo,
            foreground='white',
            font=fo,
            border=0
        )
        dark.map(
            'TButton',
            foreground=[('pressed', color), ('active', 'yellow')],
            background=[('pressed', 'black'), ('!active', fondo)]
        )


        self.entrada = tk.Text(
            self, bg='#262C2C', fg='#EDE7D3', height=4, bd=0,
            insertbackground='#EDE7D3', font=fo, padx=5,
            selectbackground='#151817', selectforeground='yellow'
        )
        self.entrada.grid(row=0, column=0, sticky='wens')
        self.fm1 = tk.Frame(relief='flat', bd=0, bg='#262C2C')
        self.fm1.grid(row=1, column=0, sticky='e')
        self.bte = ttk.Button(self.fm1, text='EJEMPLOS', padding=0, takefocus=False)
        self.bte.grid(row=0, column=0, sticky='e')
        self.btt = ttk.Button(
            self.fm1, text='TRADUCE',padding=0
        )
        self.btt.grid(row=0, column=1, sticky='e')
        self.cx = tk.BooleanVar()
        self.cbx = tk.Checkbutton(
            self.fm1, text='CON ESPACIOS', font=fo,
            foreground='#C7FF1E', background='#262C2C',
            selectcolor=fondo,
            activebackground='#262C2C',
            activeforeground='yellow',
            variable=self.cx
        )
        self.cbx.grid(row=0, column=2, sticky='e')

        self.salida = tk.Text(self, bg=fondo, fg=color, bd=0, font=fo2)
        self.salida.grid(row=2, column=0, sticky='wens')
        self.config(bg='#262C2C', bd=0)

        self.columnconfigure(0, weight=1)

    def escribe_a_entrada(self, texto):
        self._escribe(self.entrada, texto)

    def escribe_a_salida(self, texto):
        self._escribe(self.salida, texto)

    def _escribe(self, wtexto, texto):
        wtexto.delete('0.1', 'end')
        wtexto.insert('end', texto)
        wtexto.see('end')

        
class Leet(Interfaz):
    def __init__(self):
        super().__init__()
        self.dc = Diccionario()
        self.bte.config(command=self.obten_ejemplo)
        self.btt.config(command=self.muestra_traduccion)
    
    def obten_ejemplo(self):
        frase = self.dc.obten_frase()
        self.escribe_a_entrada(frase)

    def muestra_traduccion(self):
        frase = self.entrada.get('0.1', 'end').strip()
        texto_traducido = self.dc.encode(frase, con_espacio=self.cx.get())
        self.escribe_a_salida(texto_traducido)




if __name__=="__main__":
    app = Leet()
    app.mainloop()