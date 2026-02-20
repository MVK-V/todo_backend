import os
from entry import Entry


class EntryManager:
    def __init__(self, data_path):
        self.data_path = data_path  # путь данных - адрес к файлу
        self.entries = []

    def save(self):
        for entry in self.entries:
            entry.save(self.data_path)
        ''' перебираем список (объекты класса Entry) 
                применяем метод save из Entry(потому что entry - объект класса Entry)
            save - конвертируем словарь из объектов(класса Entry) в json 
                            dict  ->  json   '''



    def load(self):

        files = os.listdir(self.data_path)  # выдает списком содержимое data_path

        for filename in files:  # идем по полученному списку объектов

            if filename.endswith('.json'):
                full_path = os.path.join(self.data_path, filename)  # склеиваем адрес (например: '/tmp/toro.json')

                entry = Entry.load(full_path)   # создали объект класса Entry   str -> dict

                self.entries.append(entry)
                ''' по факту мы просто нашли все файлы '.json'
                    десериализировали их в объекты класса Entry
                    положили в список EntryManager '''



    def add_entry(self, title: str):

        new_entry = Entry(title)

        # 2. Добавляем этот новый объект в наш список self.entries
        self.entries.append(new_entry)
        ''' добавляем в список класса объекты класса Entry'''