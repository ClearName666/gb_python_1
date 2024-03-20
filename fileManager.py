from settings import nameFileNotes

def writeFile(info):
    try:
        with open(nameFileNotes, "a", encoding="utf-8") as file:
            file.write(info + '\n')
    except Exception as e:
        print(f"При работе призошла ошибка", e)

def readAllFile():
    try:
        with open(nameFileNotes, "r", encoding="utf-8") as file:
            return str(file.readlines())
    except Exception as e:
        print(f"При работе призошла ошибка", e)
        return ""

def readFile(num):
    try:
        with open(nameFileNotes, "r", encoding="utf-8") as file:
            lines = file.readlines()
            return str(lines[num])
    except Exception as e:
        print(f"При работе призошла ошибка", e)
        return ""


def editFile(num, info):
    try:
        with open(nameFileNotes, "r", encoding="utf-8") as file:
            lines = file.readlines()
        if 0 <= num < len(lines):
            lines[num] = info + '\n'
        else:
            return "Строка с таким номером не существует."

        with open(nameFileNotes, "w", encoding="utf-8") as file:
            file.writelines(lines)

        return "Файл успешно отредактирован."
    except Exception as e:
        print(f"При работе призошла ошибка", e)
        return ""

def delLineFile(num):
    try:
        with open(nameFileNotes, "r", encoding="utf-8") as file:
            lines = file.readlines()
        if 0 <= num < len(lines):
            lines[num] = ""
        else:
            return "Строка с таким номером не существует"

        with open(nameFileNotes, "w", encoding="utf-8") as file:
            file.writelines(lines)

        return "Запись успешно удалена"
    except Exception as e:
        print(f"При работе призошла ошибка", e)
        return ""
