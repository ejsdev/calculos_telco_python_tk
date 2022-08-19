from tkinter import *
import math
def moduloPotencias():
    ventanaLogaritmos = Toplevel()       
    ventanaLogaritmos.geometry('600x410')
    ventanaLogaritmos.resizable(0,0)
    ventanaLogaritmos.title("Conversor ")
    #Frame de la ventana de la aplicacion.
    frame=LabelFrame(ventanaLogaritmos, text = "Conversor dB/W")
    frame.config(foreground="black")
    frame.place(x=10,y=50,width=580,height=150)
    
    def cerrar():
        ventanaLogaritmos.destroy()
    
    labelTituloApp=Label(ventanaLogaritmos,text="Conversor de potencia",fg="LightSkyBlue4",
                         font=("Consolas",25)).pack()
    botonSalir = Button(ventanaLogaritmos, text="\u2B70Salir",cursor="hand2",
                        command=lambda:cerrar(),font=("Arial",10),
                        bg="gray85",fg="black").place(x=15, y=370)
    
    labelValor = Label(frame, text="Convertir: ",font=("Arial",12))
    labelValor.grid(row=0,column=0) 

    #Etiquetas de texto para mostrar los resultados.
    labelConvertido=Label(frame,text="",font=("Arial",12)) #Etiqueta que muestra el valor a convertir.
    labelConvertido.grid(row=1,column=1) 

    labelResultado_dbm= Label(frame, text="",font=("Arial",12))
    labelResultado_dbm.grid(row=1,column=2,columnspan=6,sticky="w")

    labelResultado_w= Label(frame, text="",font=("Arial",12))
    labelResultado_w.grid(row=2,column=2,columnspan=6,sticky="w")

    labelResultado_dbw= Label(frame, text="",font=("Arial",12))
    labelResultado_dbw.grid(row=3,column=2,columnspan=6,sticky="w")

    labelResultado_mw= Label(frame, text="",font=("Arial",12))
    labelResultado_mw.grid(row=4,column=2,columnspan=6,sticky="w")

    var_valor=StringVar() #Variable que almacena el valor introducido.
    entrada_Valor=Entry(frame, textvariable=var_valor).grid(row=0,column=1,columnspan=1)

    def borrar(): #Funcion que borra los valores introducidos y resultados.
        var_valor.set("")
        opcionesConvertir.set(0)
        labelResultado_dbm.config(text="",foreground="blue")
        labelResultado_w.config(text="",foreground="blue")
        labelResultado_dbw.config(text="",foreground="blue")
        labelResultado_mw.config(text="",foreground="blue")
        labelConvertido.config(text="",foreground="blue")


    def convertir():
        if opcionesConvertir.get()==1:   #Convertir mW         
            try:  
                valor=float(var_valor.get())
                resultado_dbm=str(float(10) * float(math.log(valor,10)))
                resultado_w= str(valor / 1000)
                resultado_dbw= str(float(10) * float(math.log((valor/1000),10)))
                labelResultado_dbm.config(text=str(" · dBm >> ") + resultado_dbm,foreground="blue")
                labelResultado_w.config(text=str(" · W >>") + resultado_w,foreground="blue")
                labelResultado_dbw.config(text=str(" · dBw >> ") + resultado_dbw,foreground="blue")
                labelResultado_mw.config(text=str(" · mW >> ") + str(valor),foreground="blue")

                labelConvertido.config(text= str(valor) +str(" mW= "),foreground="blue")
                
            except ValueError:
                labelResultado_dbm.config(foreground="red",text="[No convertible a dBm]")
                labelResultado_w.config(foreground="red",text="[No convertible a W]")
                labelResultado_dbw.config(foreground="red",text="[No convertible a dBW]")
                labelResultado_mw.config(foreground="red",text="[No convertible a mW]")
            finally:
                valor=float(var_valor.get())
                resultado_w= str(float(valor / 1000))
                labelResultado_w.config(text=str(" · W >>") + resultado_w,foreground="blue")
                labelConvertido.config(text= str(valor) +str(" mW= "),foreground="blue")

        if opcionesConvertir.get()==2: #Convertir W
            try:
                valor=float(var_valor.get())
                resultado_dbw=str(float(10) * float(math.log(valor,10)))
                resultado_dbm= str(float(10) * float(math.log((valor*1000),10)))
                resultado_mw=str(float(valor*1000))
                labelResultado_dbw.config(text=str(" · dBW >> ") + resultado_dbw, foreground="blue")
                labelResultado_dbm.config(text=str(" · dBm >> ") + resultado_dbm,foreground="blue")
                labelResultado_mw.config(text=str(" · mW >> ") + resultado_mw,foreground="blue")
                labelResultado_w.config(text=str(" · W >>  ") + str(valor),foreground="blue")

            except ValueError:
                labelResultado_dbm.config(foreground="red",text="[No convertible a dBm]")
                labelResultado_dbw.config(foreground="red",text="[No convertible a dBW]")
                labelResultado_mw.config(foreground="red",text="[No convertible a mW]")
                labelResultado_w.config(foreground="red",text="[No convertible a W]")

            finally:
                valor=float(var_valor.get())
                labelResultado_w.config(text=str(" · W >>  ") + str(valor),foreground="blue")

                resultado_mw=str(float(valor*1000))
    #             
                labelResultado_mw.config(text=str(" · mW >>") + resultado_mw,foreground="blue")
                labelConvertido.config(text= str(valor) +str(" W= "),foreground="blue")


        if opcionesConvertir.get()==3:   #Convertir dBm        
            try:  
                valor=float(var_valor.get())
                resultado_mw= str(float(10**(float(valor/10))))
                resultado_w= str(((float(10**(float(valor/1000))))+30))
                
                resultado_dbw= str(float(valor-30))
                labelResultado_dbm.config(text=str(" · dBm >> ") + str(valor),foreground="blue")
                labelResultado_w.config(text=str(" · W >>") + resultado_w,foreground="blue")
                labelResultado_mw.config(text=str(" · mW >> ") + resultado_mw,foreground="blue")
                labelResultado_dbw.config(text=str(" · dBW >> ") + resultado_dbw,foreground="blue")
                labelConvertido.config(text= str(valor) +str(" dBm= "),foreground="blue")
                
            except ValueError:
                labelResultado_dbm.config(foreground="red",text="[No convertible a dBm]")
                labelResultado_w.config(foreground="red",text="[No convertible a W]")
                labelResultado_mw.config(foreground="red",text="[No convertible a mW]")
                labelResultado_dbw.config(foreground="red",text="[No convertible a dBW]")
            except OverflowError:
                labelResultado_mw.config(foreground="red",text="[No convertible a mW]")
            finally:
                valor=float(var_valor.get())
                resultado_mw= str(float(10**(float(valor/10))))
                resultado_w= str(((float(10**(float(valor/10))))/1000))
                resultado_dbw= str(float(valor-30))
                
                labelResultado_dbm.config(text=str(" · dBm >> ") + str(valor),foreground="blue")
                labelResultado_w.config(text=str(" · W >>") + resultado_w,foreground="blue")
                labelResultado_mw.config(text=str(" · mW >> ") + resultado_mw,foreground="blue")
                labelResultado_dbw.config(text=str(" · dBW >> ") + resultado_dbw,foreground="blue")

                labelConvertido.config(text= str(valor) +str(" dBm= "),foreground="blue")
            
        if opcionesConvertir.get()==4:   #Convertir dBm        
            try:  
                valor=float(var_valor.get())
                resultado_w= str(((float(10**(float(valor/10))))/1000))
                resultado_mw= str(float(1000*(float(resultado_w))))               
                resultado_dbm= str(float(valor)+30)
                resultado_dbw= str(float(valor-30))
                labelResultado_dbm.config(text=str(" · dBm >> ") + resultado_dbm,foreground="blue")
                labelResultado_w.config(text=str(" · W >>") + resultado_w,foreground="blue")
                labelResultado_mw.config(text=str(" · mW >> ") + resultado_mw,foreground="blue")
                labelResultado_dbw.config(text=str(" · dBW >> ") + str(valor),foreground="blue")
                labelConvertido.config(text= str(valor) +str(" dBm= "),foreground="blue")
                
            except ValueError:
                labelResultado_dbm.config(foreground="red",text="[No convertible a dBm]")
                labelResultado_w.config(foreground="red",text="[No convertible a W]")
                labelResultado_mw.config(foreground="red",text="[No convertible a mW]")
            except OverflowError:
                labelResultado_mw.config(foreground="red",text="[No convertible a mW]")
            finally:
                valor=float(var_valor.get())
                
                resultado_w= str(((float(10**(float(valor/10))))))
                resultado_mw= str(float(1000*(float(resultado_w))))
                resultado_dbm= str(float(valor)+30)
                labelResultado_dbm.config(text=str(" · dBm >> ") + resultado_dbm,foreground="blue")
                labelResultado_w.config(text=str(" · W >>") + resultado_w,foreground="blue")
                labelResultado_mw.config(text=str(" · mW >> ") + resultado_mw,foreground="blue")

                labelConvertido.config(text= str(valor) +str(" dBW= "),foreground="blue")

    #Radiobutton para seleccionar la unidad a convertir. 
    opcionesConvertir=IntVar()
    opcionmW=Radiobutton(frame,text=" mW ",value=1,
                              variable=opcionesConvertir,indicatoron=0,width=10,
                              command=lambda:convertir()).grid(row=0,column=2, columnspan=1)
    opcionW=Radiobutton(frame,text=" W ",value=2,
                             variable=opcionesConvertir,indicatoron=0,width=10,
                            command=lambda:convertir()).grid(row=0,column=3, columnspan=1)
    opciondBm=Radiobutton(frame,text="dBm ",value=3,
                              variable=opcionesConvertir,indicatoron=0,width=10,
                              command=lambda:convertir()).grid(row=0,column=4, columnspan=1)
    opciondBW=Radiobutton(frame,text=" dBW ",value=4,
                              variable=opcionesConvertir,indicatoron=0,width=10,
                              command=lambda:convertir()).grid(row=0,column=5, columnspan=1)
    #Boton que llama a la funcion "borrar" borrando los resultados.
    botonBorrar=Button(frame, text="Borrar",cursor="hand2",bg="gainsboro",fg="red",
                       command=lambda:borrar()).grid(row=0,column=6)
    
    
    

    ventanaLogaritmos.mainloop()

# moduloPotencias()


