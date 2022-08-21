from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from electricidad import *
from otras import *
from sonido import *
from conversor_decimal import *
from conversor_potencia import *
class Aplicacion():
    def __init__(self):                       
        self.raiz = Tk()       
        self.raiz.geometry('800x600')
        self.raiz.resizable(0,0)
        self.raiz.title("Aplicación") 
        self.raiz.config(bg="#465461")  
        menubar = Menu(self.raiz)
        self.raiz.config(menu=menubar)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Info",command=lambda:info())
        
        filemenu.add_separator()
        filemenu.add_command(label="Salir")

        menubar.add_cascade(label="Informacion", menu=filemenu)
        
        framePrincipal=Frame(self.raiz,bg="black")
        framePrincipal.place(x=75,y=80,width=600,height=191)
        def info():
            messagebox.showinfo(message='''\u2B91Programa para cálculos de electricidad/electrónica
y telecomunicaciones.
Desarrollado por: E. José Fresnedoso.\n
Sistemas de Telecomunicaciones e Informáticos''', title="Info")
        #Llamada a las aplicaciones.
        def abrir_electricidad():
            moduloElectricidad()
        
        def abrir_conversor():
            moduloConversor()         
        
        def abrir_potencias():
            moduloPotencias()
            
        def abrir_sonido():
            moduloSonido()
        
        def abrir_otros():
            moduloOtros()
            
        
        Label(self.raiz, text="Cálculos para Electricidad, Electrónica y Telecomunicaciones",
              foreground="#ECF3F4",bg="#465461",font=("Arial",18)).pack()
        
        #separator = ttk.Separator(self.raiz, orient='horizontal')
        #separator.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.01) #Barra separadora.
        
        boton = Button(framePrincipal, text='Cálculos eléctricos',font=("Arial",16),background="#ECF3F4",
                       foreground="#465461",borderwidth=2,relief=RAISED,activeforeground="white",activebackground="#465461",anchor="center",
                       overrelief="flat",cursor="hand2",command=lambda:abrir_electricidad())    
        boton.pack(fill='x')
        boton = Button(framePrincipal, text='Conversor decimal/binario',font=("Arial",12),background="gray85",
                       foreground="gray15",borderwidth=2,relief=RAISED,activeforeground="white",activebackground="green",anchor="center",
                       overrelief="raised",cursor="hand2",command=lambda:abrir_conversor())
        boton.pack(fill='x')
        
        
        
        boton = Button(framePrincipal, text='Sonido',font=("Arial",12),background="gray85",
                       foreground="gray15",borderwidth=2,relief=RAISED,activeforeground="white",activebackground="green",anchor="center",
                       overrelief="raised",cursor="hand2",command=lambda:abrir_sonido())
        boton.pack(fill='x')
        
        
        boton = Button(framePrincipal, text='Conversor W/dB',font=("Arial",12),background="gray85",
                       foreground="gray15",borderwidth=2,relief=RAISED,activeforeground="white",activebackground="green",anchor="center",
                       overrelief="raised",cursor="hand2",command=lambda:abrir_potencias())
        boton.pack(fill='x')
        
        
        boton = Button(framePrincipal, text='Otras aplicaciones',font=("Arial",12),background="gray85",
                       foreground="gray15",borderwidth=2,relief=RAISED,activeforeground="white",activebackground="green",anchor="center",
                       overrelief="raised",cursor="hand2",command=lambda:abrir_otros())
        boton.pack(fill='x')
         
                 
              
        self.raiz.mainloop()

def main():
    mi_app = Aplicacion()
    return(0)

if __name__ == '__main__':
    main()

    