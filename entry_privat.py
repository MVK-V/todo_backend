import os
import json


def print_with_indent(value, indent=0):
    print('\t' * indent + str(value))
    '''  печать Value(входящих данных) с отступом '''


class Entry:
    def __init__(self, title, entries=None, parent=None):
        if entries is None:
            self.entries = []
        '''   список    '''
        self.title = title
        '''  название книги '''
        self.parent = parent
        ''' инициализация родителя'''

    def __str__(self):
        return self.title

    '''  если отдать Entry в консоль ---     title  '''

    def add_entry(self, entry):
        self.entries.append(entry)
        entry.parent = self
        ''' добавляем entry(запись) в entries(лист записей)
            инициализируем себя как родителя ???'''

    def print_entries(self, indent=0):
        print_with_indent(self.title, indent)  # функция по печати с отступом
        for entry in self.entries:
            entry.print_entries(indent + 1)
            ''' рекурсия по листу записей : 
                    - печатаем каждый уровень с новым отступом
                    '''

    def json(self):
        res = {
            'title': self.title,

            'entries': [entry.json() for entry in self.entries]
        }

        return res

    ''' рекурсия по листу записей : 
            - res - словарь со вложенными названиями всех записей из листа 

            мы создали обычный словарь, который можно конвертировать(сереализация) в json 
            - нельзя вытащить объект из Entry напрямую, потому что каждый объект записи - тоже объект класса Entry 
            здесь мы просто делаем строки рекурсией.

            just dict  
            '''

    @classmethod  # метод classmethod привязывает метод к классу - может быть вызван не имея представителя класса для его создания
    def from_json(cls, value: dict):

        new_entry = cls(value['title'])  # создаем представителя класса напрямую ( даем только название - title)

        for sub_entry in value.get('entries', []):  # Мы заглядываем внутрь словаря и ищем там ключ 'entries'
            new_entry.add_entry(cls.from_json(sub_entry))
            ''' new_entry.add_entry()  -  добавляем к объекту класса Entry (new_entry) 
                cls.from_json(sub_entry)  -  для каждого entries в нашем объекте мы создаем объект класса Entry с помощью рекурсии 

                таким образом из обычного словаря мы создали объект класса Entry со всеми уровнями вложений 
                и получили доступ ко всем методам класса'''

        return new_entry

    def save(self, path):  # path - путь к папке (например: /tpt/)

        filename = f'{self.title}.json'  # например: Продукты.json

        full_path = os.path.join(path, filename)  # склеили путь к папке - получили адрес файла на компьютере

        with open(full_path, 'w', encoding='utf-8') as f:
            data = self.json()

            json.dump(data, f, ensure_ascii=False, indent=4)
            ''' data = self.json()  -  Берем данные из твоего метода json() - делаем обычный словарь
                json.dump(data, f, ensure_ascii=False, indent=4)  - 
                    - Теперь json.dump знает, ЧТО записывать (data) и КУДА (f)
                       мы записываем наш словарь data в файл (память компьютера) '''

    @classmethod
    def load(cls, filename):

        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)

        return cls.from_json(data)

    ''' data = json.load(f) - перенесли данные из файла в код      str -> dict
        return cls.from_json(data) - вернули из полученного словаря объект класса Entry 

        dict  ->  cls(EntryManager) '''


new_entry = Entry('Продукты')
new_entry2 = Entry('Рабочие дела')
print(new_entry)