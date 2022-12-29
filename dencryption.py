import pyAesCrypt
import os

def dencryption(file, password):

    """Задаем размер буфера"""
    buffer_size = 512 * 1024

    """Вызываем метод расшифрования"""
    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
        password,
        buffer_size
    )

    """Выводим результат операции"""
    print("[File '"+ str(os.path.splitext(file)[0]) + "'  dencrypted]")

    """Удаляем исходный файл"""
    os.remove(file)

def walking_by_dirs(dir, password):
    """Функция сканирования директорий"""  

    #Перебираем все поддериктории в вабранной директории

    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        #Если находим файл, то дешифруем его 
        if os.path.isfile(path):
            try:
                dencryption(path, password)
            except Exception as _ex:
                print(_ex)
        #Если находим директорию, то повторяем цикл в поиске файлов
        else: 
            walking_by_dirs(path, password)    

password = input('Please, input password for dencrypt:')  
walking_by_dirs('../encrypt/x_files', password)

       


