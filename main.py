from tkinter import *

#iniciar tkinter
operador = ''
precios_comida = [1500, 2400, 1300, 1250, 750, 2500, 1750, 400]
precios_bebida = [400, 700, 750, 1500, 900, 1100, 500, 600]
precios_postres = [2100, 700, 1500, 1250, 750, 400, 1100, 600]

def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0,END)
    visor_calculadora.insert(END, operador)

def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0,END)

def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0,END)
    visor_calculadora.insert(0,resultado)
    operador = ''

def revisar_check():
    x = 0
    for i in cuadros_comida:
        if variables_comidas[x].get() == 1:
            cuadros_comida[x].config(state=NORMAL)
            if cuadros_comida[x].get() == '0':
                cuadros_comida[x].delete(0,END)
            cuadros_comida[x].focus()
        else:
            cuadros_comida[x].config(state=DISABLED)
            texto_comida[x].set('0')
        x += 1

    x = 0
    for i in cuadros_bebida:
        if variables_bebidas[x].get() == 1:
            cuadros_bebida[x].config(state=NORMAL)
            if cuadros_bebida[x].get() == '0':
                cuadros_bebida[x].delete(0,END)
            cuadros_bebida[x].focus()
        else:
            cuadros_bebida[x].config(state=DISABLED)
            texto_bebida[x].set('0')
        x += 1

    x = 0
    for i in cuadros_postres:
        if variables_postres[x].get() == 1:
            cuadros_postres[x].config(state=NORMAL)
            if cuadros_postres[x].get() == '0':
                cuadros_postres[x].delete(0,END)
            cuadros_postres[x].focus()
        else:
            cuadros_postres[x].config(state=DISABLED)
            texto_postres[x].set('0')
        x += 1


def total():
    sub_total_comida = 0
    p = 0
    for cantidad in texto_comida:
        sub_total_comida = sub_total_comida + (int(cantidad.get()) * precios_comida[p])
        p += 1


    sub_total_bebida = 0
    p = 0
    for cantidad in texto_comida:
        sub_total_bebida = sub_total_bebida + (int(cantidad.get()) * precios_bebida[p])
        p += 1


    sub_total_postres = 0
    p = 0
    for cantidad in texto_postres:
        sub_total_postres = sub_total_postres + (int(cantidad.get()) * precios_postres[p])
        p += 1

    sub_total = sub_total_comida + sub_total_bebida + sub_total_postres
    impuestos = sub_total * 0.07
    total = sub_total + impuestos

    var_costo_comida.set(f'$ {round(sub_total_comida,2)}')
    var_costo_bebida.set(f'$ {round(sub_total_bebida,2)}')
    var_costo_postres.set(f'$ {round(sub_total_postres,2)}')
    var_subtotal.set(f'$ {round(sub_total,2)}')
    var_impuestos.set(f'${round(impuestos,2)}')
    var_total.set(f'${round(total,2)}')




aplicacion = Tk()


#tamaño de la ventana
aplicacion.geometry('1280x630+0+0')


#evitar maximizar
aplicacion.resizable(False, False)

#Titulo ventana
aplicacion.title('Mi Restaurante - Sistema de Facturación')

#color de fondo de la ventana

aplicacion.config(bg='aquamarine')

#panel superior
panel_superior = Frame(aplicacion, bd=1, relief=FLAT )
panel_superior.pack(side=TOP)

#etiqueta titulo

etiqueta_titulo = Label(panel_superior, text='Sistema de Facturación', fg='azure4',
                        font=('Dosis', 48), bg='aquamarine', width=27)

#panel izquierdo

panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

#panel costos
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT, bg='azure4', padx=50)
panel_costos.pack(side=BOTTOM)


#panel comida
panel_comidas = LabelFrame(panel_izquierdo, text='Comida', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')

panel_comidas.pack(side=LEFT)


#panel bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text='Bebidas', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_bebidas.pack(side=LEFT)

#postres
panel_postres = LabelFrame(panel_izquierdo, text='Postres', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')

panel_postres.pack(side=LEFT)

#panel derecha
panel_derecha = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecha.pack(side=RIGHT)

#panel calculadora
panel_calculadora = Frame(panel_derecha, bd=1, relief=FLAT, bg='aquamarine')
panel_calculadora.pack()

#panel recibo
panel_recibo = Frame(panel_derecha, bd=1, relief=FLAT, bg='aquamarine')
panel_recibo.pack()

#panel botones
panel_botones = Frame(panel_derecha, bd=1, relief=FLAT, bg='aquamarine')
panel_botones.pack()

#lista de productos

lista_comidas = ['pollo', 'cordero', 'parrillada', 'pescado', 'pizza', 'albondiga', 'hamburguesa', 'milanesa']
lista_bebidas = ['agua', 'soda', 'jugo', 'cola', 'vino', 'gancia', 'cerveza', 'exprimido']
lista_postres = ['helado', 'fruta', 'brownies', 'flan', 'mousse', 'pastel', 'borracho', 'bolcan']


#generar items comida
variables_comidas = []
cuadros_comida = []
texto_comida = []
contador = 0
for comida in lista_comidas:

    #crear checkbutton
    variables_comidas.append('')
    variables_comidas[contador] = IntVar()
    comida = Checkbutton(panel_comidas, text=comida.title(), font=('Dosis', 19, 'bold'),
                         onvalue=1, offvalue=0, variable=variables_comidas[contador],command=revisar_check)
    comida.grid(row=contador, column=0, sticky=W)


    #crear los cuadros de entrada

    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(panel_comidas,
                                     font=('Dosis', 18, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_comida[contador])
    cuadros_comida[contador].grid(row=contador,
                                  column=1)

    contador += 1


#generar items bebida
variables_bebidas = []
cuadros_bebida = []
texto_bebida = []
contador = 0
for bebida in lista_bebidas:


    #crear chekbutton
    variables_bebidas.append('')
    variables_bebidas[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas, text=bebida.title(), font=('Dosis', 19, 'bold'),
                         onvalue=1, offvalue=0, variable=variables_bebidas[contador],command=revisar_check)
    bebida.grid(row=contador, column=0, sticky=W)

    #crear cuadro de entrada de bebida
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set('0')
    cuadros_bebida[contador] = Entry(panel_bebidas,
                                     font=('Dosis', 18, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_bebida[contador])
    cuadros_bebida[contador].grid(row=contador,
                                  column=1)


    contador += 1


#generar items postre
variables_postres = []
cuadros_postres = []
texto_postres = []
contador = 0
for postres in lista_postres:

    #creando el chekbutton
    variables_postres.append('')
    variables_postres[contador] = IntVar()
    postres = Checkbutton(panel_postres, text=postres.title(), font=('Dosis', 19, 'bold'),
                         onvalue=1, offvalue=0, variable=variables_postres[contador],command=revisar_check)
    postres.grid(row=contador, column=0, sticky=W)



    #creando cuadro de entrada de postre
    cuadros_postres.append('')
    texto_postres.append('')
    texto_postres[contador] = StringVar()
    texto_postres[contador].set('0')
    cuadros_postres[contador] = Entry(panel_postres,
                                     font=('Dosis', 18, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_postres[contador])
    cuadros_postres[contador].grid(row=contador,
                                  column=1)





    contador += 1


#variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postres = StringVar()
var_subtotal = StringVar()
var_impuestos = StringVar()
var_total = StringVar()

#etiquetas de costos y costos de entrada
etiqueta_costo_comida = Label(panel_costos,
                              text='Costo Comida',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_comida.grid(row=0, column=0)

texto_costo_comida = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_comida)
texto_costo_comida.grid(row=0,column=1)



#etiquetas de costos y costos de entrada
etiqueta_costo_bebida = Label(panel_costos,
                              text='Costo Bebida',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_bebida.grid(row=1, column=0)

texto_costo_bebida = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1,column=1, padx=41)


#etiquetas de costos y costos de entrada
etiqueta_costo_postres = Label(panel_costos,
                              text='Costo Postres',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_postres.grid(row=2, column=0, padx=41)

texto_costo_postres = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_postres)
texto_costo_postres.grid(row=2,column=1, padx=41)


#etiquetas de costos y costos de entrada
etiqueta_subtotal = Label(panel_costos,
                              text='Subtotal',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_subtotal.grid(row=0, column=2, padx=41)

texto_subtotal = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_subtotal)
texto_subtotal.grid(row=0,column=3, padx=41)


#etiquetas de costos y costos de entrada
etiqueta_impuesto = Label(panel_costos,
                              text='Impuestos',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_impuesto.grid(row=1, column=2, padx=41)

texto_impuesto = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_impuestos)
texto_impuesto.grid(row=1,column=3, padx=41)


#etiquetas de costos y costos de entrada
etiqueta_total = Label(panel_costos,
                              text='Total',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_total.grid(row=2, column=2, padx=41)

texto_total = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_total)
texto_total.grid(row=2,column=3, padx=41)


#botones
botones = ['total', 'recibo', 'guardar', 'resetear']
botones_creados = []
columnas = 0
for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=('Dosis', 14, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=9)
    botones_creados.append(boton)
    boton.grid(row=0,
               column=columnas)
    columnas += 1
botones_creados[0].config(command=total)


#area de recibo
texto_recibo = Text(panel_recibo,
                    font=('Dosis', 12, 'bold'),
                    bd=1,
                    width=50,
                    height=10)
texto_recibo.grid(row=0,
                  column=0)


#calculadora
visor_calculadora = Entry(panel_calculadora,
                          font=('Dosis', 16, 'bold'),
                          width=37,
                          bd=1)
visor_calculadora.grid(row=0,
                       column=0,
                       columnspan=4)

#botones de calculadora
botones_calculadora = ['7','8','9','+','4','5','6', '-', '1',
                       '2', '3', 'x', 'R', 'B','0','/']
botones_guardados = []
fila = 1
columna = 0

for boton in botones_calculadora:
    boton = Button(panel_calculadora,
                   text=boton.title(),
                   font=('Dosis',16,'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=8)
    botones_guardados.append(boton)
    boton.grid(row=fila,
               column=columna)
    if columna == 3:
        fila += 1
    columna +=1
    if columna == 4:
        columna = 0



botones_guardados[0].config(command=lambda: click_boton('7'))
botones_guardados[1].config(command=lambda: click_boton('8'))
botones_guardados[2].config(command=lambda: click_boton('9'))
botones_guardados[3].config(command=lambda: click_boton('+'))
botones_guardados[4].config(command=lambda: click_boton('4'))
botones_guardados[5].config(command=lambda: click_boton('5'))
botones_guardados[6].config(command=lambda: click_boton('6'))
botones_guardados[7].config(command=lambda: click_boton('-'))
botones_guardados[8].config(command=lambda: click_boton('1'))
botones_guardados[9].config(command=lambda: click_boton('2'))
botones_guardados[10].config(command=lambda: click_boton('3'))
botones_guardados[11].config(command=lambda: click_boton('*'))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda: click_boton('0'))
botones_guardados[15].config(command=lambda: click_boton('/'))




etiqueta_titulo.grid(row=0,column=0)



#evitar que la pantalla se cierre
aplicacion.mainloop()