from tkinter import *
from tkinter import ttk

# cores

cor1 = '#3b3b3b' # preto
cor2 = '#feffff' # branco
cor3 = '#38576b' # azul carregando
cor4 = '#ECEFF1' # cinza
cor5 = '#FFAB40' # laranja

#criando janela

janela = Tk()
janela.title('Calculadora')
janela.geometry('235x360')
janela.config(bg=cor2)

# criando frames

frame_tela =  Frame(janela, width=235, height=80, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo =  Frame(janela, width=235, height=280, bg=cor1)
frame_corpo.grid(row=1, column=0)


#variável todo valores
todos_valores = ''

valor_texto = StringVar()

#criando função
def entrar_valores(event):
    global todos_valores
    todos_valores = todos_valores + str(event)

    #passando valor para tela
    valor_texto.set(todos_valores)

#função para calcular 
def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    
    valor_texto.set(str(resultado))

#função para limpar tela
def limpar_tela():
        global todos_valores
        todos_valores = ''
        valor_texto.set('')




#criando label
app_label = Label(frame_tela, textvariable=valor_texto, width=15, height=4, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font= 'Ivy 18 ', bg=cor3, fg=cor2 )
app_label.place(x=0, y=0)

# criando botões

# primeira fileira
b_1 =Button(frame_corpo, command=limpar_tela, text='C', width=7, height=2, bg= cor4, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 =Button(frame_corpo,command=lambda:entrar_valores('%'), text='%', width=3, height=2, bg= cor4, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_2.place(x=110, y=0)
b_3 =Button(frame_corpo,command=lambda:entrar_valores('/'), text='/', width=3, height=2, bg= cor5, fg=cor2, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_3.place(x=172, y=0)

# segunda fileira
b_4 =Button(frame_corpo,command=lambda:entrar_valores('7'), text='7', width=3, height=2, bg= cor4, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_4.place(x=0, y=56)
b_5 =Button(frame_corpo,command=lambda:entrar_valores('8'), text='8', width=3, height=2, bg= cor4, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_5.place(x=55, y=56)
b_6 =Button(frame_corpo,command=lambda:entrar_valores('9'), text='9', width=3, height=2, bg= cor4, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_6.place(x=110, y=56)
b_7 =Button(frame_corpo,command=lambda:entrar_valores('*'), text='*', width=3, height=2, bg= cor5, fg=cor2, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_7.place(x=172, y=56)

# terceira fileira
b_8 =Button(frame_corpo,command=lambda:entrar_valores('4'), text='4', width=3, height=2, bg= cor4, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_8.place(x=0, y=112)
b_9 =Button(frame_corpo,command=lambda:entrar_valores('5'), text='5', width=3, height=2, bg= cor4, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_9.place(x=55, y=112)
b_10 =Button(frame_corpo,command=lambda:entrar_valores('6'), text='6', width=3, height=2, bg= cor4, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_10.place(x=110, y=112)
b_11 =Button(frame_corpo,command=lambda:entrar_valores('-'), text='-', width=3, height=2, bg= cor5, fg=cor2, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_11.place(x=172, y=112)

# quarta fileira
b_12 =Button(frame_corpo,command=lambda:entrar_valores('1'), text='1', width=3, height=2, bg= cor4, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_12.place(x=0, y=168)
b_13 =Button(frame_corpo,command=lambda:entrar_valores('2'), text='2', width=3, height=2, bg= cor4, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_13.place(x=55, y=168)
b_14 =Button(frame_corpo,command=lambda:entrar_valores('3'), text='3', width=3, height=2, bg= cor4, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_14.place(x=110, y=168)
b_15 =Button(frame_corpo,command=lambda:entrar_valores('+'), text='+', width=3, height=2, bg= cor5, fg=cor2, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_15.place(x=172, y=168)

# quinta fileira
b_16 =Button(frame_corpo,command=lambda:entrar_valores('0'), text='0', width=7, height=2, bg= cor4, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_16.place(x=0, y=224)
b_17 =Button(frame_corpo,command=lambda:entrar_valores('.'), text='.', width=3, height=2, bg= cor4, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_17.place(x=110, y=224)
b_18 =Button(frame_corpo,command=calcular, text='=', width=3, height=2, bg= cor5, fg=cor2, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_18.place(x=172, y=224)



janela.mainloop()
