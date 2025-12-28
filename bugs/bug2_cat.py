import os
from src.logger import p_error, p_good

# Глобальный кэш для файлов
CACHE = {}

def read_file_with_cache(file_path, cache={}):  # изменяемое значение по умолчанию
    """
    Чтение файла с кэшированием
    """
    if file_path not in cache:
        with open(file_path, 'r', encoding='utf-8') as f:
            cache[file_path] = f.read()
    return cache[file_path]

def cat(file_path):
    """
    Вывод содержимого файла в консоль
    file_path: путь к файлу (относительный или абсолютный)
    """
    try:
        # Если путь не абсолютный, делаем его абсолютным
        if not os.path.isabs(file_path):
            file_path = os.path.join(os.getcwd(), file_path)

        # Проверка на существование
        if not os.path.exists(file_path):
            print(f"Ошибка: Файл '{file_path}' не существует")
            p_error(f"Файл '{file_path}' не существует")
            return False

        # Проверка на файл
        if os.path.isdir(file_path):
            print(f"Ошибка: '{file_path}' является каталогом, а не файлом")
            p_error(f"'{file_path}' является каталогом, а не файлом")
            return False

        # Вывод содержимого с кэшированием
        content = read_file_with_cache(file_path)
        print(content)

        # Логируем успешность
        p_good(f"cat {file_path}")
        return True

    except PermissionError:
        print(f"Ошибка: Нет прав доступа к файлу '{file_path}'")
        p_error(f"Нет прав доступа к файлу '{file_path}'")
        return False
    except UnicodeDecodeError:
        print(f"Ошибка: Файл '{file_path}' содержит бинарные данные или не поддерживаемую кодировку")
        p_error(f"Файл '{file_path}' содержит бинарные данные или не поддерживаемую кодировку")
        return False
    except Exception as e:
        print(f"Ошибка: Ошибка при чтении файла: {e}")
        p_error(f"Ошибка при чтении файла: {e}")
        return False