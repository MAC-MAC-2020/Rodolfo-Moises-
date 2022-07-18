#-------------------------------------------------------------------------------------------LIBRARIES

import os 
import shutil 
from tkinter import filedialog, font
from tkinter import *
import sys

#-------------------------------------------------------------------------------------------WINDOW PARAMETERS

window = Tk()
window.geometry('200x250')
window.config(bg='white')
window.title('OF')
window.resizable(width=False, height=False)
window.iconbitmap('logo.ico')

#-------------------------------------------------------------------------------------------LABLES

estado_select_file = Label(window, bg='white', font=('Times New Roman', 12))
estado_select_file.place(x=38,y=200)
name_videos = Label(window, text='Video name', bg='white',font=('Times New Roman', 10)).place(x=60,y=20) 
name_videos = Label(window, text='Created by Rodolfo A.C.', bg='white',font=('Times New Roman', 7)).place(x=98,y=228) 
#-------------------------------------------------------------------------------------------ENTRIES
name_entry = StringVar()
name_videos_entry = Entry(window,textvariable=name_entry,  bg = 'white',bd= 1, font=('Times New Roman', 10), fg= 'black')
name_videos_entry.place(x=35,y=40)

#-------------------------------------------------------------------------------------------FUNCTION

def selectFile():
    root = Tk()
    root.withdraw()
    sesiones_carpeta = filedialog.askdirectory()
    carpeta_sesiones_listarchivos = os.listdir(sesiones_carpeta)
    for i, carpeta1 in enumerate(carpeta_sesiones_listarchivos):
        carpeta_raton = sesiones_carpeta+ f'/{carpeta_sesiones_listarchivos[i]}'
        carpeta_raton_listaarchivos = os.listdir(carpeta_raton)
        for j, carpeta2 in enumerate(carpeta_raton_listaarchivos):
            carpeta_video = carpeta_raton + f'/{carpeta_raton_listaarchivos[j]}'
            nombre_video = os.rename(carpeta_video + '/behavCam1.avi', carpeta_raton + f'/{j+1}_{name_entry.get()}.avi')

    estado_select_file.config(text='COMPLETADO...')

def cancelar():
    sys.exit()
    

#-------------------------------------------------------------------------------------------BUTTONS

select_file_button = Button(window, text='SELECT FILE', command=selectFile)
select_file_button.config(bg='white', width=20)
select_file_button.place(x=25,y=100)

change_file_button = Button(window, text='CHANGE FILE', command=selectFile)
change_file_button.config(bg='white', width=20)
change_file_button.place(x=25,y=130)

cancelar_button = Button(window, text='CANCELAR', command=cancelar)
cancelar_button.config(bg='white', width=20)
cancelar_button.place(x=25,y=160)

window.mainloop()

