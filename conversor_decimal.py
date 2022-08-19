from tkinter import *
import math
def moduloConversor():
    ventanaConversor = Toplevel()       
    ventanaConversor.geometry('600x410')
    ventanaConversor.resizable(0,0)
    ventanaConversor.title("Conversor ")
    #Frame de la ventana de la aplicacion.
    frame=LabelFrame(ventanaConversor, text = "Decimal-Binario")
    frame.config(foreground="black")
    frame.place(x=50,y=60,width=520,height=170)
    
    def cerrar():
        ventanaConversor.destroy()
    
    labelTituloApp=Label(ventanaConversor,text="Conversor Decimal/Binario",fg="LightSkyBlue4",
                         font=("Consolas",25)).pack()
    botonSalir = Button(ventanaConversor, text="\u2B70Salir",cursor="hand2",
                        command=lambda:cerrar(),font=("Arial",10),
                        bg="gray85",fg="black").place(x=15, y=370)
    
    labelValor = Label(frame, text="Convertir: ",font=("Arial",12))
    labelValor.grid(row=0,column=0) 
    
    labelResultado_bin= Label(frame, text="",font=("Arial",12))
    labelResultado_bin.grid(row=0,column=2,columnspan=2,sticky="w")

    labelResultado_dec= Label(frame, text="",font=("Arial",12))
    labelResultado_dec.grid(row=1,column=2,columnspan=2,sticky="w")

    labelResultado_hex= Label(frame, text="",font=("Arial",10))
    labelResultado_hex.grid(row=3,column=2,columnspan=2,sticky="w")

    

    var_valor=StringVar() #Variable que almacena el valor introducido.

    def convertirNumero():        
        try:
            valor = str(int(var_valor.get()))
            resultado_bin= str(bin(int(valor))[2:])
            labelResultado_bin.config(text=str("Binario: ") + resultado_bin,foreground="blue")
            resultado_dec=str(int(str(int(valor)), 2))
            labelResultado_dec.config(text=str("Decimal: ") + resultado_dec,foreground="blue")
        except ValueError:
            labelResultado_bin.config(foreground="red",text="[El valor introducido no se puede convertir]")
            labelResultado_dec.config(foreground="red",text=str(""))
        finally:
            valor = str(var_valor.get())
            resultado_bin= str(bin(int(valor))[2:])
            labelResultado_bin.config(text=str("Binario: ") + resultado_bin,foreground="blue")

          
    entrada_Valor=Entry(frame, textvariable=var_valor).grid(row=0,column=1,columnspan=1)
    
    botonBorrar=Button(frame, text="Convertir",font=("Arial",11),
                       cursor="hand2",bg="SteelBlue4",fg="white",
                       command=lambda:convertirNumero()).grid(row=1,column=1,columnspan=1)

    ventanaConversor.mainloop()

# moduloConversor()


