import pyautogui
import time
import mysql.connector
from tkinter import *
# ------Armazenamento de histórico de pesquisa--------#
#conexao = mysql.connector.connect(
#            host="",
#            user="",
#            password="",
#            database=""
#        )
#cursor = conexao.cursor()
temas = []

def pesquisa(k):
    pyautogui.press("win")
    time.sleep(8)
    pyautogui.write("opera")
    pyautogui.press("enter")
    time.sleep(8)
    pyautogui.write("youtube.com")
    pyautogui.press("enter")
    time.sleep(15)
    pyautogui.press("tab", presses=4)
    pyautogui.write(k)
    time.sleep(3)
    pyautogui.press("enter")
    time.sleep(30)
def get_tema():
    tema = input.get()
    temas.append(tema)
def exec():
    for tema in temas:
        pesquisa(tema)
    #for assunto in temas:
        #data = time.localtime()
        #datahora = data.tm_hour
        #comando = f'INSERT INTO hist(assunto, datahora) VALUES("{assunto}", "{datahora}");'
        #cursor.execute(comando)
        #conexao.commit()


#------interface gráfica -------
janela = Tk()
janela.configure(background="#dde")
janela.geometry("500x500")
janela.title("Pesquisa para estudos")
barra_pesquisa = Entry(janela)

botao = Button(janela, text="executar pesquisa", command=exec).place(x=170, y=300, width=125, height=50)

botao2 = Button(janela, text="adicionar", command=get_tema, foreground="#009")
botao2.place(x=170, y=370, width=120, height=50)
texto = Label(janela, text="Pesquise seus assuntos de estudo!", font="comicSans", background="#dde")
texto.place(x=50, y=40, width=400, height=25)
input = Entry(janela)
input.place(x=130, y=120 , width=200, height=25)
texto_de_pesquisa = Label(janela, text="assunto(s)", background="#dde").place(x=170, y="90", width=100, height="25")
janela.mainloop()
#cursor.close()
#conexao.close()

