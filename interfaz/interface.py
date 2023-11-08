from interfaz.hoverButton import HoverButton
from tkinter import Button, Label, Tk, Frame, Entry,END
from movimientos import Movimientos

class Interfaz():
    def __init__(self):
        self.jugador = "X"
        self.tablero = [[None, None, None], [None, None, None], [None, None, None]]
        
        ventana = Tk()
        ventana.geometry('300x300')
        ventana.config(bg="white")
        ventana.iconbitmap('semana_11\\triqui\\interfaz\\iconos\\triqui.ico')
        ventana.resizable(0,0)
        ventana.title("Calculadora")
        
        frame = Frame(ventana, bg="#AE90BE", relief="raised")
        frame.grid(column=0, row=0, padx=6, pady=3)
        
        ventana.grid_rowconfigure(0, weight=1)
        ventana.grid_columnconfigure(0, weight=1)
        
        self.etiquetaEvaluacion = Label(ventana, text="", font=('Comic sens MC', 14, 'bold'))
        self.etiquetaEvaluacion.grid(column=0, row=1, padx=3, pady=3)
        
        self.puntuacion = Label(ventana, text="", font=('Comic sens MC', 14, 'bold'))
        self.puntuacion.grid(column=0, row=2, padx=3, pady=3)

        # fila 1
        
        Button1 = HoverButton(frame, text="", borderwidth=2, height=3, width=6, font=('Comic sens MC', 12, 'bold'), relief="raised", activebackground="aqua", bg="#DDF2B3", anchor="center", command=lambda: self.clickButton(Button1, 0, 0))
        Button1.grid(column=0, row=1, padx=3, pady=3)

        Button2 = HoverButton(frame, text="", borderwidth=2, height=3, width=6, font=('Comic sens MC', 12, 'bold'), relief="raised", activebackground="aqua", bg="#DDF2B3", anchor="center", command=lambda: self.clickButton(Button2, 0, 1))
        Button2.grid(column=1, row=1, padx=3, pady=3)

        Button3 = HoverButton(frame, text="", borderwidth=2, height=3, width=6, font=('Comic sens MC', 12, 'bold'), relief="raised", activebackground="aqua", bg="#DDF2B3", anchor="center", command=lambda: self.clickButton(Button3, 0, 2))
        Button3.grid(column=2, row=1, padx=3, pady=3)

        # fila 2
        
        Button4 = HoverButton(frame, text="", borderwidth=2, height=3, width=6, font=('Comic sens MC', 12, 'bold'), relief="raised", activebackground="aqua", bg="#DDF2B3", anchor="center", command=lambda: self.clickButton(Button4, 1, 0))
        Button4.grid(column=0, row=2, padx=3, pady=3)

        Button5 = HoverButton(frame, text="", borderwidth=2, height=3, width=6, font=('Comic sens MC', 12, 'bold'), relief="raised", activebackground="aqua", bg="#DDF2B3", anchor="center", command=lambda: self.clickButton(Button5, 1, 1))
        Button5.grid(column=1, row=2, padx=3, pady=3)

        Button6 = HoverButton(frame, text="", borderwidth=2, height=3, width=6, font=('Comic sens MC', 12, 'bold'), relief="raised", activebackground="aqua", bg="#DDF2B3", anchor="center", command=lambda: self.clickButton(Button6, 1, 2))
        Button6.grid(column=2, row=2, padx=3, pady=3)

        # fila 3

        Button7 = HoverButton(frame, text="", borderwidth=2, height=3, width=6, font=('Comic sens MC', 12, 'bold'), relief="raised", activebackground="aqua", bg="#DDF2B3", anchor="center", command=lambda: self.clickButton(Button7, 2, 0))
        Button7.grid(column=0, row=3, padx=3, pady=3)

        Button8 = HoverButton(frame, text="", borderwidth=2, height=3, width=6, font=('Comic sens MC', 12, 'bold'), relief="raised", activebackground="aqua", bg="#DDF2B3", anchor="center", command=lambda: self.clickButton(Button8, 2, 1))
        Button8.grid(column=1, row=3, padx=3, pady=3)

        Button9 = HoverButton(frame, text="", borderwidth=2, height=3, width=6, font=('Comic sens MC', 12, 'bold'), relief="raised", activebackground="aqua", bg="#DDF2B3", anchor="center", command=lambda: self.clickButton(Button9, 2, 2))
        Button9.grid(column=2, row=3, padx=3, pady=3)

        ventana.mainloop()
    
    def clickButton(self, button, posicionI, posicionJ):
        button.config(text=self.jugador)
        if self.jugador == "X":
            self.tablero[posicionI][posicionJ] = 1
            a = Movimientos(self.tablero, 1)
            self.jugador = "O"
        elif self.jugador == "O":
            self.tablero[posicionI][posicionJ] = 0
            a = Movimientos(self.tablero, 0)
            self.jugador = "X"
        
        self.etiquetaEvaluacion.config(text="Evaluacion: " + str(a.getEvaluacion()))
        self.puntuacion.config(text="Puntuacion: " + str(a.getRootNode().root_node.puntuacion))
        