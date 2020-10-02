from tkinter import ttk
from tkinter import *

lista = [
    {
        "nombre" : 'Celular',
        "precio" : 700000
    },
    {
        "nombre" : 'PC',
        "precio" : 1500000 
    }
]

class Product:

    def __init__(self, window):
        self.wind = window
        self.wind.title('Productos')
    
        #crear contenedor (frame similar a un panel)
        frame = LabelFrame(self.wind, text = 'Registrar nuevo producto')
        #pad(pading) agrega un margen 
        #columnsapn cantidad de columnas que ocupara el elemento
        frame.grid(row = 0, column = 0, columnspan = 4, pady = 20, padx = 5)

        #label
        Label(frame, text = 'Nombre: ').grid(row = 1, column = 0)
        #input
        self.name = Entry(frame)
        self.name.grid(row = 1, column = 1)

        Label(frame, text = 'Precio: ').grid(row = 2, column = 0)
        self.price = Entry(frame)
        self.price.grid(row = 2, column = 1)

        #boton
        #sticky 
        ttk.Button(frame, text = 'Guardar').grid(row = 3, columnspan = 2, sticky = W + E)

        #tabla
        self.tree = ttk.Treeview(height = 10, column = 2)
        self.tree.grid(row = 4, column = 0, columnspan = 2)
        #agregar cabecera
        self.tree.heading('#0', text = 'nombre', anchor = CENTER)
        self.tree.heading('#1', text = 'precio', anchor = CENTER)

        self.getProducto()

    def getProducto(self):
        #limpiando ando
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        for fila in lista:
            self.tree.insert('', 0, text = fila['nombre'], values = fila['precio'])

if __name__ == '__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()