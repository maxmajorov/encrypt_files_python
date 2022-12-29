import pyAesCrypt
import os

def encryption(file, password):

    """Задаем размер буфера"""
    buffer_size = 512 * 1024

    """Вызываем метод шифрования"""
    pyAesCrypt.encryptFile(
        str(file),
        str(file) + '.crp',
        password,
        buffer_size
    )

    """Выводим результат операции"""
    print("[File '"+ str(os.path.splitext(file)[0]) + "'  encrypted]")

    """Удаляем исходный файл"""
    os.remove(file)

def walking_by_dirs(dir, password):
    """Функция сканирования директорий"""  

    #Перебираем все поддериктории в вабранной директории

    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        #Если находим файл, то шифруем его 
        if os.path.isfile(path):
            try:
                encryption(path, password)
            except Exception as _ex:
                print(_ex)
        #Если находим директорию, то повторяем цикл в поиске файлов
        else: 
            walking_by_dirs(path, password)    

password = input('Please, input password for encrypt:')  
# Передаем директорию с файлами для шифромания
walking_by_dirs('../encrypt/x_files', password)

       


