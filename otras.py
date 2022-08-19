from tkinter import *
from tkinter import ttk
import math
def moduloOtros():
    ventanaOtros = Toplevel()       
    ventanaOtros.geometry('600x410')
    ventanaOtros.resizable(0,0)
    ventanaOtros.title("Otros cálculos")
    labelVentana=Label(ventanaOtros,text="Otras aplicaciones",fg="LightSkyBlue4",font=("Consolas",25)).pack()

    separator = ttk.Separator(ventanaOtros, orient='horizontal')
    separator.place(relx=0.10, rely=0.10, relwidth=0.8, relheight=8) #Barra separadora.
    #Menú para seleccionar la aplicacion.
    varOpcion = StringVar()
    varOpcion.set('Slecciona el cálculo...')
    desplegable = ttk.Combobox(ventanaOtros, textvariable=varOpcion)
    desplegable.state(["readonly"]) #Permite leer
    desplegable.pack()
    opciones=["Coeficiente de atenuación",
              "Ruido térmico","Relación C/N",
              "Propagación de ondas"]
    desplegable['values'] = opciones
    desplegable.place(x=100, y=50,width=190)


    def cerrar():
        ventanaOtros.destroy()

    def irSeleccion():
        if varOpcion.get() == opciones[0]:
            calculoCoeficiente()
        elif varOpcion.get() == opciones[1]:
            calculoRuido()
        elif varOpcion.get() == opciones[2]:
            relacionCN()
        elif varOpcion.get() == opciones[3]:
            propagacionOndas()
        

    botonSelecionar = Button(ventanaOtros,
                             text="Seleccionar",cursor="hand2",
                             command=lambda:irSeleccion(),font=("Arial",9,"bold"),
                             bg="CadetBlue4",fg="white").place(x=300, y=50)

    botonSalir = Button(ventanaOtros,
                        text="\u2B70Salir",cursor="hand2",command=lambda:cerrar(),font=("Arial",10),
                        bg="gray85",fg="black").place(x=15, y=360)

    def calculoCoeficiente():
        frame1= Frame(ventanaOtros)
        frame1.place(x=10,y=80,width=580,height=270)
        frameAppCoeficiente=LabelFrame(frame1,text="Coeficiente de atenuacion")
        frameAppCoeficiente.config(foreground="black")
        frameAppCoeficiente.place(x=10,y=5,width=550,height=120)        
        labelEntrada=Label(frameAppCoeficiente, text="Potencia de entrada (dBm): ",
                              font=("Arial",12),
                              foreground="black").grid(row=0,column=0,sticky="e")
        labelSalida=Label(frameAppCoeficiente, text="Potencia de salida (dBm): ",
                           font=("Arial",12),
                           foreground="black").grid(row=1,column=0,sticky="e")
        labelSeccion=Label(frameAppCoeficiente, text="Distancia (Km):",
                           font=("Arial",12),
                           foreground="black").grid(row=2,column=0,sticky="e")
        labelResultadoCoeficiente=Label(frameAppCoeficiente,text=" ")
        labelResultadoCoeficiente.config(font=("Arial",12),foreground="blue")
        labelResultadoCoeficiente.grid(row=0,column=2)
                
        var_entrada=StringVar()
        var_salida=StringVar()
        var_distancia=StringVar()
        entrada_db=Entry(frameAppCoeficiente,textvariable=var_entrada).grid(row=0,column=1)
        salida_db=Entry(frameAppCoeficiente,textvariable=var_salida).grid(row=1,column=1)
        distancia_km=Entry(frameAppCoeficiente,textvariable=var_distancia).grid(row=2,column=1) 
        def calcularCoeficiente():
            try: 
                entrada= float(var_entrada.get())
                salida=float(var_salida.get())
                distancia=float(var_distancia.get())
                resultadoCoeficiente = str(float((float(entrada - salida)) / (distancia)))
                labelResultadoCoeficiente.config(text=resultadoCoeficiente +str(" dB/Km"),
                                              bitmap ="",foreground="blue")
            except ValueError:
                labelResultadoCoeficiente.config(compound = "left", bitmap ="error",
                                              foreground="red",
                                              text=" Datos introducidos incorrectos!")
            except ZeroDivisionError:
                labelResultadoCoeficiente.config(compound = "left", bitmap ="error",
                                              foreground="red",
                                              text=" Datos introducidos incorrectos!")
                
        botonCalcularCoeficiente=Button(frameAppCoeficiente,text="Calcular",
                                     font=("Arial",9),cursor="hand2",bg="SteelBlue4",fg="white",
                                     command=lambda:calcularCoeficiente()).grid(row=3,column=1,sticky="e")
                
                    
    # App: Calculo de resistencia conductor.
    def calculoRuido():
        frame2= LabelFrame(ventanaOtros, text = 'Ruido térmico')
        frame2.config(foreground="black")
        frame2.place(x=10,y=80,width=580,height=270)
        
        var_frecuencia=StringVar()
        K=float((1.3803) *(10**-23))
        var_temperatura=StringVar()
        var_frecuencia=StringVar()
        entradaFrecuencia=Entry(frame2,textvariable=var_frecuencia).grid(row=1,column=1)
        entradaTemperatura=Entry(frame2,textvariable=var_temperatura).grid(row=0,column=1)
        entradaTemperatura=Entry(frame2,textvariable=var_temperatura).grid(row=0,column=1)

        
        labelTemperatura=Label(frame2, text="Temperatura: ",font=("Arial",12),foreground="black").grid(row=0,column=0,sticky="e")
        labelFrecuencia=Label(frame2, text="Ancho de banda (Hz)",
                           font=("Arial",12),foreground="black").grid(row=1,column=0)
                
        labelResultadoR= Label(frame2,text=" ")
        labelResultadoR.grid(row=1,column=2,columnspan=2)
        labelResultadoR.config(font=("Arial",12),foreground="blue")
        def calcularRuido():
            if opcionesTemperatura.get()==1:
                try:
                    temperatura = (float(var_temperatura.get())+273.15)
                    frecuencia=float(var_frecuencia.get())
                    resultadoA = float(K*temperatura*frecuencia)
                    resultadoR= str(float(10) * float(math.log(resultadoA,10)))
                    resultadoR= str(temperatura)

                    labelResultadoR.config(text=resultadoR +str(" dBW"), bitmap ="",foreground="blue")
                except ValueError:
                    labelResultadoR.config(compound = "left", bitmap ="error",foreground="red",text=" Datos introducidos incorrectos!")
                except ZeroDivisionError:
                    labelResultadoR.config(compound = "left", bitmap ="error",foreground="red",text=" Datos introducidos incorrectos!")
          
            if opcionesTemperatura.get()==2:
                try:
                    temperatura = float(var_temperatura.get())
                    frecuencia=float(var_frecuencia.get())
                    resultadoA = float(K*temperatura*frecuencia)
                    resultadoR= str(float(10) * float(math.log(resultadoA,10)))
                    labelResultadoR.config(text=resultadoR +str(" dBW"), bitmap ="",foreground="blue")
                except ValueError:
                    labelResultadoR.config(compound = "left", bitmap ="error",foreground="red",text=" Datos introducidos incorrectos!")
                except ZeroDivisionError:
                    labelResultadoR.config(compound = "left", bitmap ="error",foreground="red",text=" Datos introducidos incorrectos!")
        

                                
        opcionesTemperatura=IntVar()
        opcionCentigrados=Radiobutton(frame2,text="º C",value=1,variable=opcionesTemperatura,indicatoron=0,command=lambda:calcularRuido(),width=20).grid(row=0,column=2,sticky="snew")
        
        opcionKelvin=Radiobutton(frame2,text=" º K",value=2,variable=opcionesTemperatura,indicatoron=0,command=lambda:calcularRuido(),width=20).grid(row=0,column=3,sticky="snew")        
        

    def relacionCN():
        frame3= Frame(ventanaOtros)
        frame3.place(x=10,y=80,width=580,height=270)
        frameAppCN=LabelFrame(frame3,text="Relación Portadora/Ruido (C/N)")
        frameAppCN.config(foreground="black")
        frameAppCN.place(x=10,y=5,width=550,height=110)        
        var_sen=StringVar()
        var_ruido=StringVar()
        entradaSeñal=Entry(frameAppCN,textvariable=var_sen).grid(row=1,column=1)
        entradaRuido=Entry(frameAppCN,textvariable=var_ruido).grid(row=0,column=1)        
        labelSeñal=Label(frameAppCN, text="Señal util (dB\u00b5V):",font=("Arial",12),foreground="black").grid(row=0,column=0,sticky="e")
        labelRuido=Label(frameAppCN, text="Potencia ruido (dB\u00b5V)",
                           font=("Arial",12),foreground="black").grid(row=1,column=0)
        labelResultadoCN= Label(frameAppCN,text=" ")
        labelResultadoCN.grid(row=0,column=2,columnspan=2)
        labelResultadoCN.config(font=("Arial",12),foreground="blue")

        def relacionCN():
            try:
                señal = float(var_sen.get())
                ruido=float(var_ruido.get())
                resultado_cn= str(float(señal-ruido))
                labelResultadoCN.config(text=resultado_cn +str(" dB"), bitmap ="",foreground="blue")
            except ValueError:
                labelResultadoCN.config(compound = "left", bitmap ="error",foreground="red",text=" Datos introducidos incorrectos!")
            except ZeroDivisionError:
                labelResultadoR.config(compound = "left", bitmap ="error",foreground="red",text=" Datos introducidos incorrectos!")
            
        botonCalcularCN=Button(frameAppCN,text="Calcular",
                                     font=("Arial",9),cursor="hand2",bg="SteelBlue4",fg="white",
                                     command=lambda:relacionCN()).grid(row=3,column=1,sticky="e")

    def propagacionOndas():
        frame4= LabelFrame(ventanaOtros, text = 'Longitud onda y velocidad')
        frame4.config(foreground="black")
        frame4.place(x=10,y=80,width=580,height=270)
        
        frameLambda= LabelFrame(frame4, text = 'Longitud de onda ()')
        frameLambda.config(foreground="black")
        frameLambda.place(x=10,y=5,width=550,height=110)
        
        var_frecuencia=StringVar()
        var_otroValor=StringVar()
        entradaFrecuencia=Entry(frameLambda,textvariable=var_frecuencia).grid(row=0,column=1)
        entradaVelocidad=Entry(frameLambda,textvariable=var_otroValor,disabledforeground="gray")
        entradaVelocidad.config(state="disabled",width=6)
        entradaVelocidad.grid(row=1,column=5)
                
        labelFrecuencia=Label(frameLambda, text="Frecuencia (Hz)",
                            font=("Arial",12),
                            foreground="black").grid(row=0,column=0,sticky="e")
        labelVelocidad=Label(frameLambda, text="Velocidad:",
                            font=("Arial",12)).grid(row=1,column=0,sticky="e")
        labelIntroducirVelocidad=Label(frameLambda, text="Metros/segundos",
                               font=("Arial",8)).grid(row=1,column=6,sticky="w")
                
        labelResultadoLambda= Label(frameLambda,text=" ")
        labelResultadoLambda.grid(row=0,column=2,columnspan=10)
        labelResultadoLambda.config(font=("Arial",12),foreground="blue")
                
        def seleccionandoOpcion():
            if var_opcion.get()==1:
                var_otroValor.set(300000000)
                var_otroValor.get()
                entradaVelocidad.config(state="disabled")
            elif var_opcion.get()==2:
                var_otroValor.set(343)
                var_otroValor.get()
                entradaVelocidad.config(state="disabled")
            elif var_opcion.get()==3:
                entradaVelocidad.configure(state="normal",foreground="blue")
                var_otroValor.set(0)
                var_otroValor.get()
        def calcularLambda():
            try:
                frecuencia = float(var_frecuencia.get())
                velocidad=float(var_otroValor.get())
                resultadoLambda= str(float(velocidad / frecuencia))
                labelResultadoLambda.config(text=resultadoLambda +str(" metros"), bitmap ="",foreground="blue")
            except ValueError:
                labelResultadoLambda.config(compound = "left", bitmap ="error",foreground="red",text=" Datos introducidos incorrectos!")
            except ZeroDivisionError:
                labelResultadoLambda.config(compound = "left", bitmap ="error",foreground="red",text=" Datos introducidos incorrectos!")
                
                
        var_opcion=IntVar()
        opcionLuz=Radiobutton(frameLambda,text="Velocidad Luz",value=1,
                                variable=var_opcion,
                                command=lambda:seleccionandoOpcion()).grid(row=1,column=1,
                                                                           sticky="w")
            
        opcionSonido=Radiobutton(frameLambda,text="Velocidad Sonido",value=2,
                                    variable=var_opcion,
                                    command=lambda:seleccionandoOpcion()).grid(row=2,column=1,sticky="w")
            
        opcionOtro=Radiobutton(frameLambda,text="Otra velocidad:",value=3,
                                 variable=var_opcion,
                                 command=lambda:seleccionandoOpcion()).grid(row=1,column=4,sticky="e")
                
        botonCalculoLambda= Button(frameLambda,text="Calcular",
                              font=("Arial",9),cursor="hand2",
                              bg="SteelBlue4",fg="white",
                              command=lambda:calcularLambda()).grid(row=1,column=3,sticky="e")

        frameVelocidad = LabelFrame(frame4, text = 'Velocidad de propagación')
        frameVelocidad.config(foreground="black")
        frameVelocidad.place(x=10,y=120,width=550,height=110)
        
        var_frecuencia_dos=StringVar()
        var_lambda=StringVar()
        entradaFrecuencia=Entry(frameVelocidad,textvariable=var_frecuencia_dos).grid(row=0,column=1)
        entradaLambda=Entry(frameVelocidad,textvariable=var_lambda).grid(row=1,column=1)
                
        labelFrecuencia=Label(frameVelocidad, text="Frecuencia (Hz): ",
                            font=("Arial",12),
                            foreground="black").grid(row=0,column=0,sticky="e")
        labelLambda=Label(frameVelocidad, text="Longitud Onda (, metros): ",
                            font=("Arial",12)).grid(row=1,column=0,sticky="e")
        
                
        labelResultadoVelocidad= Label(frameVelocidad,text=" ")
        labelResultadoVelocidad.grid(row=0,column=2,columnspan=10)
        labelResultadoVelocidad.config(font=("Arial",12),foreground="blue")
        
        def calcularVelocidad():
            try: 
                frecuencia = float(var_frecuencia_dos.get())
                longitud_onda=float(var_lambda.get())
                resultadoVelocidad = str((float(longitud_onda)*float(frecuencia)))
                labelResultadoVelocidad.config(text=resultadoVelocidad+str(" m/s"),
                                              bitmap ="",foreground="blue")
            except ValueError:
                labelResultadoVelocidad.config(compound = "left", bitmap ="error",
                                              foreground="red",
                                              text=" Datos introducidos incorrectos!")
            except ZeroDivisionError:
                labelResultadoVelocidad.config(compound = "left", bitmap ="error",
                                              foreground="red",
                                              text=" Datos introducidos incorrectos!")
        
        botonCalculoVelocidad= Button(frameVelocidad,text="Calcular",
                              font=("Arial",9),cursor="hand2",
                              bg="SteelBlue4",fg="white",
                              command=lambda:calcularVelocidad()).grid(row=2,column=1,sticky="e")
        
    
    ventanaOtros.mainloop()
# moduloOtros()