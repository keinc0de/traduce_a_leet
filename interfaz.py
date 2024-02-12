import tkinter as tk
from tkinter import ttk


class Interfaz(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('430x220')

        fo = ('Consolas', 10, 'bold')
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
        self.salida = tk.Text(self, bg=fondo, fg=color, bd=0)
        self.salida.grid(row=2, column=0)
        self.config(bg='#262C2C', bd=0)

        self.columnconfigure(0, weight=1)

        



if __name__=="__main__":
    app = Interfaz()
    # app.dark()
    app.mainloop()