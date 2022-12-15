# Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.
# Фамилия_1|Имя_1|Телефон_1|Описание_1

# {
# фамилия: Бочков,
# имя: Марк,
# телефон: 564564,
# описание: с работы, знакомый
# }

# os.chdir(path) Смена текущей директории (аналог cd)
# os.getcwd() Текущая директория (аналог pwd)
# os.listdir(path=".") Список файлов в директории(аналог ls в linux или dir в windows)
# os.mkdir создаёт директорию. OSError, если директория существует
# os.remove Удаление пути файла 
# os.rename(src, dst) Переименовывает файл или директорию из src в dst
# os.path.exists True, если файл или директория существует
# os.path.join Соединяется два пути с учетом ОС
# os.path.normpath Нормализует путь, убирая лишние разделители 
# os.path.split Разделяет путь на список
# obj Что записывать (см.таблицу на 21 слайде)
# fp Файл, куда записывать
# skipkeys Значением по умолчанию - False. Если True,то ключи dict, которые не имеют базового 
# типа (str, int, float, bool, None), будут пропущены вместо вызова TypeError(не все типы данных 
# переводятся в JSON
# ensure_ascii По умолчанию True: берет за основу таблицу ASCII. Если False, то возьмет таблицу Unicode, 
# где есть русский язык
# check_circular Нужна ли проверка циклических ссылок
# allow_nan  Разрешает NaN, Infinity, -Infinity
# indent Отступ. Советую использовать 2 или 4, чтобы JSON приобрел свой канонический образ.
# separators Подается кортежем из двух элементов. По умолчанию: (', ', ': '). Первый - item_separator, 
# второй - разделитель ключа-значения.
# sort_keys По умолчанию False. Если True, то входные данные отсортируются по ключу.

# функция csv.reader
# функция csv.writer
# класс csv.Dictwriter
# класс csv.DictReader


import json

CONTACTS_STRUCTURE = {
    "id": None,
    "sec_name": None, 
    "first_name": None,
    "tel_number": None,
    "adress": None
}

# Создаём новый файл .json, если не найдет с указанным именем.
def file_init(list_1):
    list_0 = [list_1]
    with open("phone_file_1.json", "w") as write_file:
        json.dump(list_0, write_file, separators=',\n')

# Считываем записанный файл 
def read_file():
    with open("phone_file_1.json", "r", encoding = 'utf-8') as read_file:
        return json.load(read_file)

def file_edit(list_1):
    list_0 = [list_1]
    with open("phone_file_1.json", "a", encoding = 'utf-8') as write_ed_file:
        json.dump(list_0, write_ed_file, ensure_ascii=False, indent=4)


contact_1 = {
    "id": 1,
    "sec_name": 'jbnkj', 
    "first_name": 'ufviuc',
    "tel_number": '+123456789',
    "adress": 'lvjhvjhvljvh'
}

file_edit(contact_1)

print(read_file())