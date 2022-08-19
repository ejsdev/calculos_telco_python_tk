from tkinter import *
from tkinter import ttk
import math
def moduloSonido():
# Declaracion de la ventana de sonido y su configuración
    ventanaSonido = Toplevel()       
    ventanaSonido.geometry('600x410')
    ventanaSonido.resizable(0,0)
    ventanaSonido.title("Sonido")
    labelVentana=Label(ventanaSonido,text="Sonido",fg="LightSkyBlue4",font=("Consolas",25)).pack()
    
    # Widget separador, separa el titulo principal del menú desplegable
    separator = ttk.Separator(ventanaSonido, orient='horizontal')
    separator.place(relx=0.10, rely=0.10, relwidth=0.8, relheight=8) #Barra separadora.
    
 
    varOpcion = StringVar() 
    varOpcion.set('Slecciona la aplicacion...')
    desplegable = ttk.Combobox(ventanaSonido, textvariable=varOpcion)
    desplegable.state(["readonly"]) #Permite leer y no introducir texto en el combobox
    desplegable.pack()
    opciones=["Intensidad sonora",
              "Tiempo de reberveración(Sabine)","SPL (Nivel Presion Sonora)",
              "Perdida de transmisión de un material (PT)"]
    desplegable['values'] = opciones
    desplegable.place(x=100, y=50,width=250)
    
    def cerrar():
        ventanaSonido.destroy()
    
    def irSeleccion():
        if varOpcion.get() == opciones[0]:
            IntensidadSonora()
        elif varOpcion.get() == opciones[1]:
            TiempoReverberacion()
        elif varOpcion.get() == opciones[2]:
            PresionSonora()
        elif varOpcion.get() == opciones[3]:
            perdidaTransmision()
        elif varOpcion.get() == opciones[4]:
            pass
             
    botonSelecionar = Button(ventanaSonido,
                             text="Seleccionar",cursor="hand2",font=("Arial",9,"bold"),command=lambda:irSeleccion(),
                             bg="CadetBlue4",fg="white").place(x=355, y=50)    

    botonSalir = Button(ventanaSonido,
                        text="\u2B70Salir",cursor="hand2",command=lambda:cerrar(),font=("Arial",10),
                        bg="gray85",fg="black").place(x=15, y=378)

    def IntensidadSonora():
        
        frame1= LabelFrame(ventanaSonido, text = 'Intensidad Sonora')
        frame1.config(foreground="black")
        frame1.place(x=10,y=80,width=580,height=295)
                
        labelPotencia=Label(frame1, text="Potencia acustica (vatios):",font=("Arial",12),
                            foreground="black").grid(row=0,column=0,sticky="e")
        labelEsfera=Label(frame1, text="Radio esfera (metros):",font=("Arial",12),
                          foreground="black").grid(row=1,column=0,sticky="e")
        
        labelResultadoIntensidad=Label(frame1,text=" ")
        labelResultadoIntensidad.config(font=("Arial",12),foreground="blue")
        labelResultadoIntensidad.grid(row=0,column=2)
                
        var_potencia=StringVar()
        var_radio=StringVar()
        entradaPotencia=Entry(frame1,textvariable=var_potencia).grid(row=0,column=1)
        entradaRadio=Entry(frame1,textvariable=var_radio).grid(row=1,column=1)
                
        def calcularIntensidadSonora():
            try:
                potencia = float(var_potencia.get())
                radio=float(var_radio.get())
                resultadoIntensidad = str(potencia / (float(4*3.14*pow(radio, 2))))
                labelResultadoIntensidad.config(text=resultadoIntensidad+str("  W/m\u00B2"), bitmap ="",
                                                foreground="blue")
            except ValueError:
                labelResultadoIntensidad.config(compound = "left", bitmap ="error",
                                                foreground="red",text=" Datos introducidos incorrectos!")
            except ZeroDivisionError:
                labelResultadoIntensidad.config(compound = "left", bitmap ="error",
                                                foreground="red",text=" Datos introducidos incorrectos!")
                        
        botonCalcularIntensidad=Button(frame1,text="Calcular",font=("Arial",9),cursor="hand2",bg="SteelBlue4",fg="white",command=lambda:calcularIntensidadSonora()).grid(row=3,column=1,sticky="e")


    def TiempoReverberacion():
        frame2= LabelFrame(ventanaSonido, text = 'Tiempo reverberación de Sabine')
        frame2.config(foreground="black")
        frame2.place(x=10,y=80,width=580,height=295)    
        labelVolumen=Label(frame2, text="Volumen del recinto(m\u00B3):",font=("Arial",12),
                           foreground="black").grid(row=0,column=0,sticky="e")
        labelArea=Label(frame2, text="Area de absorcion (m\u00B2):",font=("Arial",12),
                        foreground="black").grid(row=1,column=0,sticky="e")
        labelResultadoTiempo=Label(frame2,text=" ")
        labelResultadoTiempo.config(font=("Arial",12),foreground="blue")
        labelResultadoTiempo.grid(row=0,column=2)
                
        var_volumen=StringVar()
        var_area=StringVar()
        entradaVolumen=Entry(frame2,textvariable=var_volumen).grid(row=0,column=1)
        entradaArea=Entry(frame2,textvariable=var_area).grid(row=1,column=1)
                
        def calcularTiempo():
            try:
                volumen = float(var_volumen.get())
                area = float(var_area.get())
                resultadoTiempo = str((0.16*volumen) / area)
                labelResultadoTiempo.config(text=resultadoTiempo+str("  segundos"), bitmap ="",
                                            foreground="blue")
            except ValueError:
                labelResultadoTiempo.config(compound = "left", bitmap ="error",
                                            foreground="red",text=" Datos introducidos incorrectos!")
            except ZeroDivisionError:
                labelResultadoTiempo.config(compound = "left", bitmap ="error",
                                            foreground="red",text=" Datos introducidos incorrectos!")
                 
        botonCalcularTiempo=Button(frame2,text="Calcular",font=("Arial",9),
                                   cursor="hand2",bg="SteelBlue4",fg="white",
                                   command=lambda:calcularTiempo()).grid(row=3,column=1,sticky="e")
    
    def PresionSonora():
        frame3= LabelFrame(ventanaSonido, text = 'SPL (Nivel de Presion Sonora)')
        frame3.config(foreground="black")
        frame3.place(x=10,y=80,width=580,height=80)        
        
        labelPascales=Label(frame3, text="Presion sonora (Pascales):",font=("Arial",12),
                            foreground="black").grid(row=0,column=0,sticky="e")
        
        labelResultado_db=Label(frame3,text=" ")
        labelResultado_db.config(font=("Arial",12),foreground="blue")
        labelResultado_db.grid(row=0,column=2)       
        
        var_pascales=StringVar()
        entradaPresion=Entry(frame3,textvariable=var_pascales).grid(row=0,column=1)
                
        def calcularPresion():
            try:
                presion = float(var_pascales.get())
                resultado_db = str(float(20) * (float(math.log((presion / 0.00002),10))))
                labelResultado_db.config(text=resultado_db +str("  dB"), bitmap ="",foreground="blue")
            except ValueError:
                labelResultado_db.config(compound = "left", bitmap ="error",foreground="red",
                                         text=" Datos introducidos incorrectos!")
            except ZeroDivisionError:
                 labelResultado_db.config(compound = "left", bitmap ="error",foreground="red",
                                          text=" Datos introducidos incorrectos!")
        botonCalcularPresion=Button(frame3,text="Calcular",font=("Arial",9),
                                    cursor="hand2",bg="SteelBlue4",fg="white",
                                    command=lambda:calcularPresion()).grid(row=3,column=1,sticky="e")
        
        frame4= LabelFrame(ventanaSonido, text = 'Atenuación SPL')
        frame4.config(foreground="black")
        frame4.place(x=10,y=160,width=580,height=120)       
        
        labelSPL=Label(frame4, text="SPL de referenccia del altavoz (dB): ",font=("Arial",9),
                       foreground="black").grid(row=0,column=0,sticky="e")   
        labelSPL=Label(frame4, text="Distancia (metros) ",font=("Arial",9),
                       foreground="black").grid(row=1,column=0,sticky="e")   

        var_valorSPL=StringVar()
        var_distancia=StringVar()
        entradaSPL=Entry(frame4,textvariable=var_valorSPL).grid(row=0,column=1)
        entradaDistancia=Entry(frame4,textvariable=var_distancia).grid(row=1,column=1)
        
        labelValor_at=Label(frame4,text=" ")
        labelValor_at.config(font=("Arial",8),foreground="blue")
        labelValor_at.grid(row=2,column=1,columnspan=3)       
        
        labelResultado_at=Label(frame4,text=" ")
        labelResultado_at.config(font=("Arial",8),foreground="blue")
        labelResultado_at.grid(row=3,column=1,columnspan=3)
        
        def seleccionandoOpcion():
            if var_opcion.get()==1:
                try:
                    distancia = float(var_distancia.get())
                    spl = float(var_valorSPL.get())
                    valor_at = str(float((20) *  float(math.log(distancia,10))))
                    labelValor_at.config(text=str("Atenuación de:  ") + valor_at +str("  dB"), bitmap ="",
                                         foreground="blue")
                    resultado= str(float(spl - float(valor_at)))
                    labelResultado_at.config(text=str("SPL: ") + resultado +str("  dB"), bitmap ="",
                                             foreground="blue")      
                except ValueError:
                    labelResultado_at.config(compound = "left", bitmap ="error",
                                             foreground="red",text=" Datos introducidos incorrectos!")
                    labelValor_at.config(compound = "left", bitmap ="error",
                                         foreground="red",text=" Datos introducidos incorrectos!")
                
            elif var_opcion.get()==2:
                try:
                    distancia = float(var_distancia.get())
                    spl = float(var_valorSPL.get())
                    valor_at =str(float((10) *  float(math.log(distancia,10))))
                    labelValor_at.config(text=str("Atenuación de:  ") +  valor_at +str("  dB"), bitmap ="",
                                         foreground="blue")
                    resultado=str(float(spl - float(valor_at)))
                    labelResultado_at.config(text=str("SPL: ") + resultado +str("  dB"), bitmap ="",
                                             foreground="blue")
                except ValueError:
                    labelResultado_at.config(compound = "left", bitmap ="error",
                                             foreground="red",text=" Datos introducidos incorrectos!")
                    labelValor_at.config(compound = "left", bitmap ="error",
                                         foreground="red",text=" Datos introducidos incorrectos!")
            
                      
        var_opcion=IntVar()
        opcionPuntual=Radiobutton(frame4,text="Fuente puntual",value=1,variable=var_opcion,indicatoron=0,
                                  width=15,command=lambda:seleccionandoOpcion()).grid(row=0,column=2,columnspan=1)
        opcionLineal=Radiobutton(frame4,text="Fuente Lineal",value=2,variable=var_opcion,indicatoron=0,
                                 width=15,command=lambda:seleccionandoOpcion()).grid(row=0,column=3,columnspan=1)

  
        frame5= LabelFrame(ventanaSonido, text = 'Aumento SPL')
        frame5.config(foreground="black")
        frame5.place(x=10,y=280,width=580,height=95)       
        
        labelSPL=Label(frame5, text="SPL referenccia del altavoz (dB): ",font=("Arial",12),
                       foreground="black").grid(row=0,column=0,sticky="e")   
        labelPotencia=Label(frame5, text="Potencia aplicada (W): ",font=("Arial",12),
                            foreground="black").grid(row=1,column=0,sticky="e") 
        
        labelValor_aspl=Label(frame5,text=" ")
        labelValor_aspl.config(font=("Arial",8),foreground="blue")
        labelValor_aspl.grid(row=0,column=2)
        
        labelResultado_spl=Label(frame5,text=" ")
        labelResultado_spl.config(font=("Arial",8),foreground="blue")
        labelResultado_spl.grid(row=1,column=2) 
        
        var_spl=StringVar()
        var_potencia=StringVar()
        entradaSPL=Entry(frame5,textvariable=var_spl).grid(row=0,column=1)
        entradaPotencia=Entry(frame5,textvariable=var_potencia).grid(row=1,column=1)
        def aspl():   
            try:
                potencia = float(var_potencia.get())
                spl = float(var_spl.get())
                valor_aspl = str(float((10) *  float(math.log(potencia,10))))
                labelValor_aspl.config(text=str("Aumento (SPL):  ") + valor_aspl +str("  dB"), bitmap ="",
                                       foreground="blue")
                resultado_spl= str(float(spl + float(valor_aspl)))
                labelResultado_spl.config(text=str("SPL: ") + resultado_spl +str("  dB"), bitmap ="",
                                          foreground="blue")      
            except ValueError:
                labelValor_aspl.config(compound = "left", bitmap ="error",
                                       foreground="red",text=" Datos introducidos incorrectos!")
                labelResultado_spl.config(compound = "left", bitmap ="error",
                                          foreground="red",text=" Datos introducidos incorrectos!")
        botonCalcularPerdida=Button(frame5,text="Calcular",font=("Arial",9),
                                    cursor="hand2",bg="SteelBlue4",fg="white",
                                    command=lambda:aspl()).grid(row=3,column=1,sticky="e")

     
    def perdidaTransmision():
        frame6= LabelFrame(ventanaSonido, text = 'Perdida de transmision de un material (PT)')
        frame6.config(foreground="black")
        frame6.place(x=10,y=80,width=580,height=295)      
        
        labelPresionIncidente=Label(frame6, text="Presion sonora incidente (Pascales):",font=("Arial",12),
                                    foreground="black").grid(row=0,column=0,sticky="e")
        labelPresionSaliente=Label(frame6, text="Presion sonora transmitida (Pascales):",font=("Arial",12),
                                   foreground="black").grid(row=1,column=0,sticky="e")

        labelResultado_pt=Label(frame6,text=" ")
        labelResultado_pt.config(font=("Arial",12),foreground="blue")
        labelResultado_pt.grid(row=0,column=2)       
        
        var_incidente=StringVar()
        entradaPresionIncidente=Entry(frame6,textvariable=var_incidente).grid(row=0,column=1)
        var_saliente=StringVar()
        entradaPresionSaliente=Entry(frame6,textvariable=var_saliente).grid(row=1,column=1)
        
        def calcularPerdidaT():
            try:
                incidente = float(var_incidente.get())
                saliente = float(var_saliente.get())
                resultado_pt = str(float(incidente - saliente))
                labelResultado_pt.config(text=resultado_pt +str("  dB"), bitmap ="",foreground="blue")
            except ValueError:
                labelResultado_db.config(compound = "left", bitmap ="error",
                                         foreground="red",text=" Datos introducidos incorrectos!")
            except ZeroDivisionError:
                 labelResultado_db.config(compound = "left", bitmap ="error",
                                          foreground="red",text=" Datos introducidos incorrectos!")      
        botonCalcularPerdida=Button(frame6,text="Calcular",font=("Arial",9),
                                    cursor="hand2",bg="SteelBlue4",fg="white",
                                    command=lambda:calcularPerdidaT()).grid(row=3,column=1,sticky="e")

    ventanaSonido.mainloop()

# moduloSonido()