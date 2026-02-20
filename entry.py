import os
import json


def print_with_indent(value, indent=0):
    print('\t' * indent + str(value))


class Entry:
    def __init__(self, title, entries=None, parent=None):
        if entries is None:
            self.entries = []
        self.title = title
        self.parent = parent


    def __str__(self):
        return self.title


    def add_entry(self, entry):
        self.entries.append(entry)
        entry.parent = self


    def print_entries(self, indent=0):
        print_with_indent(self.title, indent)  # функция по печати с отступом
        for entry in self.entries:
            entry.print_entries(indent + 1)


    def json(self):
        res = {
            'title': self.title,

            'entries': [entry.json() for entry in self.entries]
        }

        return res



    @classmethod
    def from_json(cls, value: dict):

        new_entry = cls(value['title'])

        for sub_entry in value.get('entries', []):
            new_entry.add_entry(cls.from_json(sub_entry))


        return new_entry

    def save(self, path):

        filename = f'{self.title}.json'

        full_path = os.path.join(path, filename)

        with open(full_path, 'w', encoding='utf-8') as f:
            data = self.json()

            json.dump(data, f, ensure_ascii=False, indent=4)


    @classmethod
    def load(cls, filename):

        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)

        return cls.from_json(data)


