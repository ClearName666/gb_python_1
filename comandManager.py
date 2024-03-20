from fileManager import *
import re
def comandRead(comand):
    patternPrint = r"print num (\d+)"
    patternEdit = r"edit num (\d+)"
    patternDel = r"del num (\d+)"
    matchPrint = re.search(patternPrint, comand)
    matchEdit = re.search(patternEdit, comand)
    matchDel = re.search(patternDel, comand)
    if comand == "add":
        print("Введите заметку")
        note = input()
        writeFile(note)
        print("ваша заметка сохранена")
    elif comand == "print":
        print(readAllFile())
    elif matchPrint:
        number = int(matchPrint.group(1))
        s = readFile(number-1)
        if s != "":
            print(s)
        else:
            print("Не найдена запись")
    elif matchEdit:
        number = int(matchEdit.group(1))
        s = readFile(number-1)
        if s != "":
            print(s)
            print("Напишите новую заметку для этой записи")
            newNote = input()
            print(editFile(number, newNote))
        else:
            print("Не найдена запись")
    elif matchDel:
        number = int(matchDel.group(1))
        s = readFile(number-1)
        if s != "":
            print(delLineFile(number-1))
        else:
            print("Не найдена запись")

    else:
        print("Нету такой команды")




