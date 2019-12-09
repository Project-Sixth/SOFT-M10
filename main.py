import zipfile
import os
import sys
import subprocess
import shutil

pathTo7Zip = "C:\\Program Files\\7-Zip\\7z.exe"

def rearchive(file):
    print("Переархивирую %s" % file)

    # Создать темп-папку
    ospath = os.path.split(file)
    tempFolderName = ospath[0] + "\\tmp"
    os.mkdir(tempFolderName)

    # Разархивировать из ZIP в временную папку
    zippedFile = zipfile.ZipFile(file, mode="r")
    zippedFile.extractall(tempFolderName)
    zippedFile.close()

    # Заархивировать в 7Z
    command = '"' + pathTo7Zip + '" a -t7z -r -mx9 "' + os.path.join(ospath[0], ospath[1].replace(".zip", ".7z")) + '" "' + tempFolderName + "\\*"
    # print("Calling %s" % command, file=os.devnull)
    subprocess.call(command)

    # Удалить папку TMP
    # os.remove(tempFolderName)
    shutil.rmtree(tempFolderName)

    # Удалить прошлый файл
    os.remove(file)
    print("Удалил прошлый файл.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Give me file (one or more)!")
        input()
    else:
        for singleFile in sys.argv[1:]:
            rearchive(singleFile)