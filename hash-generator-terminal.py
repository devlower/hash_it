# imports project setup

from os import listdir
from os.path import isfile, join
import hashlib
from datetime import datetime

# initializing variables

hash = hashlib.md5()
now = datetime.now().strftime('(%d/%m/%Y %H:%M:%S)')
time = datetime.now().strftime('(%d-%m-%Y %H-%M-%S)')
hashList = []
fileContent = []
index = 0
path = input(
    'Insira aqui um diretório para que seja gerada a hash de seus arquivos: ')

# formating path 

for char in path:
    if(char == '/'):
        char = '\\'

# list comprehension that loops in each file in folder path (returns only files)

files = [f for f in listdir(path) if isfile(join(path, f))]
print(files)

# generating HASH md5 for each file from folder path

for file in files:
    hash = hashlib.md5()

    file = path + '\\' + file

    hash.update(open(file, 'rb').read())
    hashList.append(hash.hexdigest())

    outputFormat = file + '; ' + hashList[index] + ' ' + now + '\n'
    fileContent.append(outputFormat)
    index += 1

# creating output .txt file with HASHs

fileOutput = open(f"C:\\Temp\\Hash-Generator{time}.txt", "w")
fileOutput.writelines(fileContent)
fileOutput.close()
print(hashList)


