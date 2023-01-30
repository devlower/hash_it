# imports project setup

from os import listdir
from os.path import isfile, join
from tkinter import *
from tkinter import ttk
import hashlib
from datetime import datetime

# initializing variables

hash = hashlib.md5()
now = datetime.now().strftime('(%d/%m/%Y %H:%M:%S)')
time = datetime.now().strftime('(%d-%m-%Y %H-%M-%S)')
hashList = []
fileContent = []
outputContent = []

# function scope to generate HASH criptography


def PrintHash(*args):
    index = 0
    fileContent = []
    outputContent = []
    hashList = []

    try:
        path = pathInput.get()
        for char in path:
            if(char == '/'):
                char = '\\'
        files = [f for f in listdir(path) if isfile(join(path, f))]
        for file in files:
            hash = hashlib.md5()
            file = path + '\\' + file
            hash.update(open(file, 'rb').read())
            hashList.append(hash.hexdigest())

            txtFormat = file + '; ' + hashList[index] + ' ' + now + '\n'
            windowFormat = file + '; ' + hashList[index] + ' ' + now
            fileContent.append(txtFormat)
            outputContent.append(windowFormat)
            index += 1
        print(fileContent)
        fileOutput = open(f"Hash-Generator{time}.txt", "w")
        fileOutput.writelines(fileContent)
        print(hashList)

    except ValueError:
        pass

    information = Label(
        window, text=f'Um arquivo Hash-Generator{time}.txt foi criado no mesmo diretório do arquivo hash-generator.py, contendo as HASHs do diretório inserido')
    information.grid(column=0, row=3, padx=10, pady=10)

    outputvar = StringVar(value=outputContent)
    lbox = Listbox(window, listvariable=outputvar,  width=130, height=20)
    lbox.grid(column=0, row=4, padx=10, pady=10)

# graphic user interface using tk


window = Tk()
window.title('Gerador de Hash')

text = Label(window, text='Escolha um diretório para que seja gerado os HASHs de seus arquivos')
text.grid(column=0, row=0, padx=10, pady=10)

pathInput = StringVar()
path_entry = ttk.Entry(window, width=55, textvariable=pathInput)
path_entry.grid(column=0, row=1, padx=10, pady=10)

botao = Button(window, text="Hash it!", command=PrintHash)
botao.grid(column=0, row=2, padx=10, pady=10)


window.mainloop()
