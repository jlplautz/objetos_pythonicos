from tkinter import Frame, Label, Button


class Timer(Frame):
    def __init__(self):
        super().__init__()
        self.inicio = self.agora = 15
        self.pendente = None  # alarme pedente
        self.grid()
        self.mostrador = Label(
            self, width=2, anchor='e', font='Helvetica 40 bold'
        )
        self.mostrador.grid(column=0, row=0, sticky='nswe')
        self.bt_start = Button(self, text='Start', command=self.start)
        self.bt_start.grid(column=0, row=1, sticky='we')
        self.atualizar_mostrador()

    def atualizar_mostrador(self):
        self.mostrador['text'] = str(self.agora)

    def start(self):
        if self.pendente:
            self.after_cancel(self.pendente)
        self.agora = self.inicio
        self.atualizar_mostrador()
        self.pendente = self.after(100, self.tictac)

    def tictac(self):
        self.agora -= 1
        self.atualizar_mostrador()
        if self.agora > 0:
            self.pendente = self.after(100, self.tictac)


if __name__ == '__main__':
    timer = Timer()
    timer.mainloop()
