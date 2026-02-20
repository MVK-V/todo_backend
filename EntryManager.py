import os
from entry import Entry


class EntryManager:
    def __init__(self, data_path):
        self.data_path = data_path
        self.entries = []

    def save(self):
        for entry in self.entries:
            entry.save(self.data_path)




    def load(self):

        files = os.listdir(self.data_path)

        for filename in files:

            if filename.endswith('.json'):
                full_path = os.path.join(self.data_path, filename)

                entry = Entry.load(full_path)

                self.entries.append(entry)




    def add_entry(self, title: str):

        new_entry = Entry(title)

        self.entries.append(new_entry)
