from tkinter import *
from tkinter import ttk
def moduloElectricidad():
    ventanaElectricidad = Toplevel()       
    ventanaElectricidad.geometry('600x410')
    ventanaElectricidad.resizable(0,0)
    ventanaElectricidad.title("Electricidad")
    labelVentana=Label(ventanaElectricidad,text="Cálculos eléctricos",fg="LightSkyBlue4",font=("Consolas",25)).pack()

    separator = ttk.Separator(ventanaElectricidad, orient='horizontal')
    separator.place(relx=0.10, rely=0.10, relwidth=0.8, relheight=8) #Barra separadora.
    #Menú para seleccionar la aplicacion.
    
    varOpcion = StringVar()
    varOpcion.set('Slecciona el cálculo...')
    desplegable = ttk.Combobox(ventanaElectricidad, textvariable=varOpcion)
    desplegable.state(["readonly"]) 
    desplegable.pack()
    opciones=["Densidad e Intensidad de corriente",
              "Resistencia de conductor","Ley de Ohm",
              "Consumo Electrico","Potencia Eléctrica"]
    desplegable['values'] = opciones
    desplegable.place(x=100, y=50,width=190)


    def cerrar():
        ventanaElectricidad.destroy()

    def irSeleccion():
        if varOpcion.get() == opciones[0]:
            calculoDensidadIntensidad()
        elif varOpcion.get() == opciones[1]:
            calculoResistencia()
        elif varOpcion.get() == opciones[2]:
            leyOhm()
        elif varOpcion.get() == opciones[3]:
            costeConsumo()
        elif varOpcion.get() == opciones[4]:
            potenciaElectrica()

    botonSelecionar = Button(ventanaElectricidad,
                             text="Seleccionar",cursor="hand2",command=lambda:irSeleccion(),font=("Arial",9,"bold"),
                             bg="CadetBlue4",fg="white").place(x=300, y=50)

    botonSalir = Button(ventanaElectricidad,
                        text="\u2B70Salir",cursor="hand2",command=lambda:cerrar(),font=("Arial",10),
                        bg="gray85",fg="black").place(x=11, y=360)

    # App: Calculo de densidad e intensidad de corriente.
    def calculoDensidadIntensidad():
        # App: Calculo densidad de corriente. 
        frame1= LabelFrame(ventanaElectricidad, text = 'Densidad de corriente')
        frame1.config(foreground="black")
        frame1.place(x=10,y=80,width=580,height=120)
                
        labelIntensidad=Label(frame1, text="Intensidad (amperios):",
                              font=("Arial",12),
                              foreground="black").grid(row=0,column=0,sticky="e")
        labelSeccion=Label(frame1, text="Sección (mm\u00B2):",
                           font=("Arial",12),
                           foreground="black").grid(row=1,column=0,sticky="e")
        labelResultadoDensidad=Label(frame1,text=" ")
        labelResultadoDensidad.config(font=("Arial",12),foreground="blue")
        labelResultadoDensidad.grid(row=0,column=2)
                
        var_intensidad=StringVar()
        var_seccion=StringVar()
        entradaIntensidad=Entry(frame1,textvariable=var_intensidad).grid(row=0,column=1)
        entradaSeccion=Entry(frame1,textvariable=var_seccion).grid(row=1,column=1)
              
        def calcularDensidad():
            try: 
                intensidad = float(var_intensidad.get())
                seccion=float(var_seccion.get())
                resultadoCulombios = str((float(intensidad)/float(seccion)))
                labelResultadoDensidad.config(text=resultadoCulombios+str(" Culombios"),
                                              bitmap ="",foreground="blue")
            except ValueError:
                labelResultadoDensidad.config(compound = "left", bitmap ="error",
                                              foreground="red",
                                              text=" Datos introducidos incorrectos!")
            except ZeroDivisionError:
                labelResultadoDensidad.config(compound = "left", bitmap ="error",
                                              foreground="red",
                                              text=" Datos introducidos incorrectos!")
                 
        botonCalcularDensidad=Button(frame1,text="Calcular",
                                     font=("Arial",9),cursor="hand2",bg="SteelBlue4",fg="white",
                                     command=lambda:calcularDensidad()).grid(row=3,column=1,sticky="e")
                
        # App: Calculo intensidad de corriente.
        frame2= LabelFrame(ventanaElectricidad, text = 'Intensidad de corriente')
        frame2.config(foreground="black")
        frame2.place(x=10,y=200,width=580,height=150)
                
        labelCulombios=Label(frame2, text="Culombios (Q):",font=("Arial",12),
                             foreground="black").grid(row=0,column=0,sticky="e")
        labelTiempo=Label(frame2, text="Tiempo (segundos):",font=("Arial",12),
                          foreground="black").grid(row=1,column=0,sticky="e")
        
        labelResultadoIntensidad=Label(frame2,text=" ")
        labelResultadoIntensidad.config(font=("Arial",12),
                                        foreground="blue")
        labelResultadoIntensidad.grid(row=0,column=2)
                
        var_culombios=StringVar()
        var_tiempo=StringVar()
        entradaCulombios=Entry(frame2,textvariable=var_culombios).grid(row=0,column=1)
        entradaTiempo=Entry(frame2,textvariable=var_tiempo).grid(row=1,column=1)
        
        def calcularIntensidad():
            try: 
                culombios = float(var_culombios.get())
                tiempo=float(var_tiempo.get())
                resultadoIntensidad = str(float(culombios)/float(tiempo))
                labelResultadoIntensidad.config(text=resultadoIntensidad+str(" A"),
                                                bitmap ="",foreground="blue")
            except ValueError:
                labelResultadoIntensidad.config(compound = "left",
                                                bitmap ="error",foreground="red",
                                                text=" Datos introducidos incorrectos!")
            except ZeroDivisionError:
                labelResultadoIntensidad.config(compound = "left",
                                                bitmap ="error",foreground="red",
                                                text=" Datos introducidos incorrectos!")
                
        botonCalcularIntensidad=Button(frame2,text="Calcular",
                                       font=("Arial",9),cursor="hand2",
                                       bg="SteelBlue4",fg="white",
                                       command=lambda:calcularIntensidad()).grid(row=3,column=1,sticky="e")
            
    # App: Calculo de resistencia conductor.
    def calculoResistencia():
        frame3= LabelFrame(ventanaElectricidad, text = 'Resistencia Conductor')
        frame3.config(foreground="black")
        frame3.place(x=10,y=80,width=580,height=270)
                
        var_long=StringVar()
        var_secc=StringVar()
        var_otra=StringVar()
        var_otroValor=StringVar()
        var_ValorFinal=DoubleVar()
        entradaLongitud=Entry(frame3,textvariable=var_long).grid(row=0,column=1)
        entradaSeccion=Entry(frame3,textvariable=var_secc).grid(row=1,column=1)
        entradaResistividad=Entry(frame3,textvariable=var_otroValor,disabledforeground="gray")
        entradaResistividad.config(state="disabled",width=6)
        entradaResistividad.grid(row=1,column=5)
                
        labelLongitud=Label(frame3, text="Longitud (metros):",
                            font=("Arial",12),
                            foreground="black").grid(row=0,column=0,sticky="e")
        labelSeccion=Label(frame3, text="Sección conductor (mm\u00B2):",
                           font=("Arial",12),foreground="black").grid(row=1,column=0)
        labelMaterial=Label(frame3, text="Conductor:",
                            font=("Arial",12)).grid(row=2,column=0)
        labelIntroducirR=Label(frame3, text="Resistividad:",
                               font=("Arial",12)).grid(row=1,column=4,sticky="w")
                
        labelResultadoR= Label(frame3,text=" ")
        labelResultadoR.grid(row=0,column=2,columnspan=10)
        labelResultadoR.config(font=("Arial",12),foreground="blue")
                
        def seleccionandoOpcion():
            if var_opcion.get()==1:
                var_otroValor.set(0.0172)
                var_otroValor.get()
                entradaResistividad.config(state="disabled")
            elif var_opcion.get()==2:
                var_otroValor.set(0.028)
                var_otroValor.get()
                entradaResistividad.config(state="disabled")
            elif var_opcion.get()==3:
                var_otroValor.set(0.016)
                var_otroValor.get()
                entradaResistividad.config(state="disabled")
            elif var_opcion.get()==4:
                var_otroValor.set(0.13)
                var_otroValor.get()
                entradaResistividad.config(state="disabled")
            elif var_opcion.get()==5:
                var_otroValor.set(0.95)
                var_otroValor.get()
                entradaResistividad.config(state="disabled")
            elif var_opcion.get()==6:
                var_otroValor.set(0.12)
                var_otroValor.get()
                entradaResistividad.config(state="disabled")
            elif var_opcion.get()==7:
                var_otroValor.set(0.055)
                var_otroValor.get()
                entradaResistividad.config(state="disabled")
            elif var_opcion.get()==8:
                var_otroValor.set(1.09)
                var_otroValor.get()
                entradaResistividad.config(state="disabled")
            elif var_opcion.get()==9:
                entradaResistividad.configure(state="normal",foreground="blue")
                var_otroValor.set(0)
                var_otroValor.get()
        
        def calcularResistencia():
            try:
                valorLong = float(var_long.get())
                valorSecc=float(var_secc.get())
                valorCond=float(var_otroValor.get())
                resultadoR = str(((valorLong)/(valorSecc))*(valorCond))
                labelResultadoR.config(text=resultadoR +str(" \u2126"), bitmap ="",foreground="blue")
            except ValueError:
                labelResultadoR.config(compound = "left", bitmap ="error",foreground="red",
                                       text=" Datos introducidos incorrectos!")
            except ZeroDivisionError:
                labelResultadoR.config(compound = "left", bitmap ="error",foreground="red",
                                       text=" Datos introducidos incorrectos!")
                
        var_opcion=IntVar()
        opcionCobre=Radiobutton(frame3,text="Cobre",value=1,
                                variable=var_opcion,
                                command=lambda:seleccionandoOpcion()).grid(row=2,column=1,
                                                                           sticky="w")
            
        opcionAluminio=Radiobutton(frame3,text="Aluminio",value=2,
                                    variable=var_opcion,
                                    command=lambda:seleccionandoOpcion()).grid(row=3,column=1,sticky="w")
            
        opcionPlata=Radiobutton(frame3,text="Plata",value=3,
                                variable=var_opcion,
                                command=lambda:seleccionandoOpcion()).grid(row=4,column=1,sticky="w")
            
        opcionEstaño=Radiobutton(frame3,text="Estaño",value=4,
                                variable=var_opcion,
                                command=lambda:seleccionandoOpcion()).grid(row=5,column=1,sticky="w")
            
        opcionMercurio=Radiobutton(frame3,text="Mercurio",value=5,
                                   variable=var_opcion,
                                   command=lambda:seleccionandoOpcion()).grid(row=6,column=1,sticky="w")
            
        opcionHierro=Radiobutton(frame3,text="Hierro",value=6,
                                 variable=var_opcion,
                                 command=lambda:seleccionandoOpcion()).grid(row=7,column=1,sticky="w")
            
        opcionTungsteno=Radiobutton(frame3,text="Tungsteno",value=7,
                                    variable=var_opcion,
                                    command=lambda:seleccionandoOpcion()).grid(row=8,column=1,sticky="w")
            
        opcionNicrom=Radiobutton(frame3,text="Nicrom",value=8,
                                 variable=var_opcion,
                                 command=lambda:seleccionandoOpcion()).grid(row=9,column=1,sticky="w")
            
        opcionNicrom=Radiobutton(frame3,text="Otro",value=9,
                                 variable=var_opcion,
                                 command=lambda:seleccionandoOpcion()).grid(row=1,column=6,sticky="w")
                
        botonCalculo3= Button(frame3,text="Calcular",
                              font=("Arial",9),cursor="hand2",
                              bg="SteelBlue4",fg="white",
                              command=lambda:calcularResistencia()).grid(row=1,column=3,sticky="e")
        
            
    # App: Calculo ley de Ohm.
    def leyOhm():
        frame4= LabelFrame(ventanaElectricidad, text = 'Ley de Ohm')
        frame4.config(foreground="black")
        frame4.place(x=10,y=80,width=580,height=270)
                
        var_intensidad=StringVar()
        var_tension=StringVar()
        var_resistencia=StringVar()
        var_resultadoOhm=StringVar()
                
        def seleccionandoOhm():
                    
            if var_opcionesOhm.get()==1:
                frameOhm=LabelFrame(ventanaElectricidad, text = "Obtener Intensidad")
                frameOhm.config(foreground="black")
                frameOhm.place(x=50,y=150,width=500,height=150)
                labelTension=Label(frameOhm, text="Tension (Voltios):",
                                   font=("Arial",12),foreground="black").grid(row=0,column=0,sticky="e")
                labelResistencia=Label(frameOhm, text="Resistencia"+ " (\u2126):",
                                       font=("Arial",12),foreground="black").grid(row=1,column=0,sticky="e")
                        
                labelResultadoI=Label(frameOhm,text=" ")
                labelResultadoI.config(font=("Arial",10),foreground="blue")
                labelResultadoI.grid(row=0,column=2)
                       
                entradaTension=Entry(frameOhm,textvariable=var_tension).grid(row=0,column=1)
                entradaResistencia=Entry(frameOhm,textvariable=var_resistencia).grid(row=1,column=1)
                        
                def calcularI():
                    try:
                        tension=float(var_tension.get())
                        resistencia=float(var_resistencia.get())
                        resultadoI=str((tension)/(resistencia))
                        labelResultadoI.config(text=resultadoI +str(" A"), bitmap ="",
                                               foreground="blue")
                    except ValueError: 
                        labelResultadoI.config(compound = "left", bitmap ="error",
                                               foreground="red",text=" Datos introducidos incorrectos!")
                    except ZeroDivisionError:
                        labelResultadoI.config(compound = "left", bitmap ="error",
                                               foreground="red",text=" Datos introducidos incorrectos!")
                        return (0)
                botonCalcularI=Button(frameOhm,text="Calcular",
                                      font=("Arial",9),cursor="hand2",
                                      bg="SteelBlue4",fg="white",command=lambda:calcularI())
                botonCalcularI.grid(row=3,column=1)
                    
            elif var_opcionesOhm.get()==2:
                frameOhm=LabelFrame(ventanaElectricidad, text = "Obtener Tension")
                frameOhm.config(foreground="black")
                frameOhm.place(x=50,y=150,width=500,height=150)
               
                labelResistencia=Label(frameOhm, text="Resistencia"+ " (\u2126):",font=("Arial",12),foreground="black").grid(row=0,column=0,sticky="e")
                labelIntensidad=Label(frameOhm, text="Intensidad (Amperios):",font=("Arial",12),foreground="black").grid(row=1,column=0,sticky="e")
                        
                labelResultadoT=Label(frameOhm,text=" ")
                labelResultadoT.config(font=("Arial",10),foreground="blue")
                labelResultadoT.grid(row=0,column=3)
                        
                        
                entradaIntensidad=Entry(frameOhm,textvariable=var_intensidad).grid(row=0,column=1)
                entradaResistencia=Entry(frameOhm,textvariable=var_resistencia).grid(row=1,column=1)
                        
                def calcularT():
                    try:
                        resistencia=float(var_resistencia.get())
                        intensidad=float(var_intensidad.get())
                        resultadoT=str((resistencia)*(intensidad))
                        labelResultadoT.config(text=resultadoT +str(" V"), bitmap ="",
                                               foreground="blue")
                    except ValueError: 
                        labelResultadoT.config(compound = "left", bitmap ="error",
                                               foreground="red",text=" Datos introducidos incorrectos")
                botonCalcularT=Button(frameOhm,text="Calcular",
                                      font=("Arial",9),cursor="hand2",
                                      bg="SteelBlue4",fg="white",
                                      command=lambda:calcularT()).grid(row=3,column=1)
                 
                    
            elif var_opcionesOhm.get()==3:
                frameOhm=LabelFrame(ventanaElectricidad, text = "Obtener Resistencia")
                frameOhm.config(foreground="black")
                frameOhm.place(x=50,y=150,width=500,height=150)
                
                labelTension=Label(frameOhm, text="Tension (Voltios):",
                                   font=("Arial",12),foreground="black").grid(row=0,column=0,sticky="e")
                labelIntensidad=Label(frameOhm, text="Intensidad (Amperios):",
                                      font=("Arial",12),foreground="black").grid(row=1,column=0,sticky="e")
                        
                labelResultadoR=Label(frameOhm,text=" ")
                labelResultadoR.config(font=("Arial",10),foreground="blue")
                labelResultadoR.grid(row=0,column=3)
                        
                entradaTension=Entry(frameOhm,textvariable=var_tension).grid(row=0,column=1)
                entradaIntensidad=Entry(frameOhm,textvariable=var_intensidad).grid(row=1,column=1)
                def calcularR():
                    try:
                        tension=float(var_tension.get())
                        intensidad=float(var_intensidad.get())
                        resultadoR=str((tension)/(intensidad))
                        labelResultadoR.config(text=resultadoR +" \u2126", bitmap ="",foreground="blue")
                    except ValueError:
                        labelResultadoR.config(compound = "left", bitmap ="error",foreground="red",
                                               text="Datos introducidos incorrectos")
                    except ZeroDivisionError:
                        labelResultadoR.config(compound = "left", bitmap ="error",foreground="red",
                                               text="Datos introducidos incorrectos")
                botonCalcular=Button(frameOhm,text="Calcular",
                                     font=("Arial",9),cursor="hand2",
                                     bg="SteelBlue4",fg="white",
                                     command=lambda:calcularR()).grid(row=3,column=1)
                      
                
        var_opcionesOhm=IntVar()
        opcionIntensidad=Radiobutton(frame4,text="Obtener Intensidad",
                                     value=1,variable=var_opcionesOhm,width=25,
                                     indicatoron=0,command=lambda:seleccionandoOhm()).grid(row=0,column=0,sticky="w")
        opcionTension=Radiobutton(frame4,text="Obtener tensiónn",
                                  value=2,variable=var_opcionesOhm,width=25,indicatoron=0,
                                  command=lambda:seleccionandoOhm()).grid(row=0,column=1,sticky="w")
        opcionResistencia=Radiobutton(frame4,text="Obtener Resistencia",
                                      value=3,variable=var_opcionesOhm,width=25,indicatoron=0,
                                      command=lambda:seleccionandoOhm()).grid(row=0,column=2,sticky="w")

    # App: Calculo de consumo y coste electrico.
    def costeConsumo():
        frame5= LabelFrame(ventanaElectricidad, text="Coste y consumo electrico")
        frame5.config(foreground="black")
        frame5.place(x=10,y=80,width=580,height=270)
        var_dias=StringVar()
        var_horas=StringVar()
        var_vatios=StringVar()
        var_coste=StringVar()
        energia_consumida=StringVar()
        def seleccionandoAppEnenergia():
            if opcionesEnergiaConsumo.get()==1:            
                frameEnergia=LabelFrame(frame5, text = "Obtener Resistencia")
                frameEnergia.config(foreground="black")
                frameEnergia.place(x=40,y=50,width=500,height=150)

                labelDias=Label(frameEnergia,text="Días de utilización:",
                                font=("Arial",12)).grid(row=0,column=0,sticky="e")
                labelHoras=Label(frameEnergia,text="Horas/día:",
                                 font=("Arial",12)).grid(row=1,column=0,sticky="e")
                labelVatios=Label(frameEnergia,text="Consumo (kWh):",
                                  font=("Arial",12)).grid(row=2,column=0,sticky="e")
                
                labelConsumo=Label(frameEnergia,text="Consumo:",font=("Arial",12)).grid(row=0,column=3)
                labelResultadoConsumo=Label(frameEnergia,text=" ")
                labelResultadoConsumo.config(font=("Arial",10),foreground="blue")
                labelResultadoConsumo.grid(row=0,column=4)
            
                #Entrada de datos
                entradaDias=Entry(frameEnergia,textvariable=var_dias).grid(row=0,column=1)
                entadaHoras=Entry(frameEnergia,textvariable=var_horas).grid(row=1,column=1)
                entradaVatios=Entry(frameEnergia,textvariable=var_vatios).grid(row=2,column=1)
                def calcularEnergia():
                    try:
                        dias=float(var_dias.get())
                        horas=float(var_horas.get())
                        vatios=float(var_vatios.get())
                        resultadoEnergia=str(vatios*(dias*horas))
                        labelResultadoConsumo.config(text=resultadoEnergia+str(" kWh"),
                                                     bitmap ="",foreground="blue")
                    except ValueError:
                        labelResultadoConsumo.config(compound = "left",
                                                     bitmap ="error",foreground="red",
                                                     text=" Datos incorrectos")
                        return (0)
                botonCalcular=Button(frameEnergia, text="Calcular",
                                     font=("Arial",9),cursor="hand2",
                                     bg="SteelBlue4",fg="white",
                                     command=lambda:calcularEnergia()).grid(row=4,column=1)

            elif opcionesEnergiaConsumo.get()==2:     
                frameCoste=LabelFrame(frame5, text = "Coste")
                frameCoste.config(foreground="black")
                frameCoste.place(x=40,y=50,width=500,height=150)
            
                labelDias=Label(frameCoste,text="Energía consumida (kWh):",
                                font=("Arial",12)).grid(row=0,column=0,sticky="e")
                labelHoras=Label(frameCoste,text="Precio unitario (€):",
                                 font=("Arial",12)).grid(row=1,column=0,sticky="e")
                labelCoste=Label(frameCoste, text="Coste:",
                                 font=("Arial",8)).grid(row=0,column=2)
            
                labelResultadoCoste=Label(frameCoste,text=" ")
                labelResultadoCoste.config(font=("Arial",11),foreground="blue")
                labelResultadoCoste.grid(row=0,column=3)
            
                entradaEnergia=Entry(frameCoste, textvariable=energia_consumida).grid(row=0,column=1)
                entradaCoste=Entry(frameCoste, textvariable=var_coste).grid(row=1,column=1)
                def calcularCoste():
                    try:
                        energia=float(energia_consumida.get())
                        precio=float(var_coste.get())
                        resultado=str(energia*precio)
                        labelResultadoCoste.config(text=resultado+ " €",
                                                   bitmap ="",foreground="blue")
                    
                    except ValueError:
                        labelResultadoCoste.config(compound = "left",
                                                   bitmap ="error",foreground="red",
                                                   text=" Datos incorrectos")
                        
                    
                botonCalcularCoste=Button(frameCoste, text="Calcular",
                                          font=("Arial",9),cursor="hand2",
                                          bg="SteelBlue4",fg="white",
                                          command=lambda:calcularCoste()).grid(row=4,column=1)
        opcionesEnergiaConsumo=IntVar()
        opcionConsumo=Radiobutton(frame5,text="Consumo",width=20,
                                  value=1,variable=opcionesEnergiaConsumo,indicatoron=0,
                                  command=lambda:seleccionandoAppEnenergia()).grid(row=0,column=0,sticky="w")
        opcionCosten=Radiobutton(frame5,text="Coste",width=20,
                                 value=2,variable=opcionesEnergiaConsumo,indicatoron=0,
                                 command=lambda:seleccionandoAppEnenergia()).grid(row=0,column=1,sticky="w")
    def potenciaElectrica():
        frame6= LabelFrame(ventanaElectricidad, text="Potencia Eléctrica")
        frame6.config(foreground="black")
        frame6.place(x=10,y=80,width=580,height=270)
        
        frame_a=LabelFrame(frame6, text = "Tensión (U) y resistencia (R)")
        frame_a.config(foreground="black")
        frame_a.place(x=10,y=5,width=500,height=100)

        labelTension=Label(frame_a,text="Tensión (U, voltios):",font=("Arial",12)).grid(row=0,column=0,sticky="e")
        labelResistencia=Label(frame_a,text="Resistencia (R, \u2126):",font=("Arial",12)).grid(row=1,column=0,sticky="e")
        labelResultadoPA=Label(frame_a,text=" ")
        labelResultadoPA.config(font=("Arial",15),foreground="blue")
        labelResultadoPA.grid(row=0,column=4)
            
        #Entrada de datos
        var_tension=StringVar()
        var_resistencia=StringVar()
        var_intensidad=StringVar()
        entradaTension=Entry(frame_a,textvariable=var_tension).grid(row=0,column=1)
        entadaResistencia=Entry(frame_a,textvariable=var_resistencia).grid(row=1,column=1)
        def calcularPA():
            try:
                tension=float(var_tension.get())
                resistencia=float(var_resistencia.get())
                resultado=str(float(tension**2 /resistencia))
                labelResultadoPA.config(text=resultado + " W",bitmap ="",foreground="blue")
            except ValueError:
                labelResultadoPA.config(compound = "left",bitmap ="error",
                                        foreground="red",text=" Datos incorrectos")
        
        botonCalcularPA=Button(frame_a, text="Calcular",font=("Arial",9),
                               cursor="hand2",bg="SteelBlue4",fg="white",
                                          command=lambda:calcularPA()).grid(row=4,column=0)
            
        
        
        frame_b=LabelFrame(frame6, text = "Tensión (U) y resistencia (R)")
        frame_b.config(foreground="black")
        frame_b.place(x=10,y=115,width=500,height=105)

        labelResistenciaB=Label(frame_b,text="Resistencia (R, \u2126):",
                                font=("Arial",12)).grid(row=0,column=0,sticky="e")
        labelIntensidadB=Label(frame_b,text="Intensidad (amperios):",
                               font=("Arial",12)).grid(row=1,column=0,sticky="e")
        labelResultadoPB=Label(frame_b,text=" ")
        labelResultadoPB.config(font=("Arial",15),foreground="blue")
        labelResultadoPB.grid(row=0,column=4)
            
        #Entrada de datos
        var_resistenciaB=StringVar()
        var_intensidad=StringVar()
        entradaResistenciaB=Entry(frame_b,textvariable=var_resistenciaB).grid(row=0,column=1)
        entadaIntensidad=Entry(frame_b,textvariable=var_intensidad).grid(row=1,column=1)
        def calcularPB():
            try:
                intensidad=float(var_intensidad.get())
                resistencia=float(var_resistenciaB.get())
                resultadoB=str(float((intensidad**2)*(resistencia)))
                labelResultadoPB.config(text=resultadoB + " W",bitmap ="",foreground="blue")
            except ValueError:
                labelResultadoPB.config(compound = "left",bitmap ="error",
                                        foreground="red",text=" Datos incorrectos")
        
        botonCalcularPB=Button(frame_b, text="Calcular",
                               font=("Arial",9),cursor="hand2",bg="SteelBlue4",fg="white",
                                          command=lambda:calcularPB()).grid(row=4,column=0)
    ventanaElectricidad.mainloop()
# moduloElectricidad()