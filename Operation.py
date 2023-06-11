# В этом классе представленны основные оерации которые можно выполнять с блокнотом
# 1) получение списка заметок
# 2) создание новой заметки
# 3) сохранение заметки
# 4) обновление существующей заметки
# 5) удаление заметки
# 7) удаление всех заметок

import json

from Note import Note

class Operation(object):
    
    def __init__(self, file):
        self.file = file
        self.notes = list()
        
    def seter_notes(self):
        self.notes = self.get_notes_list()
        
    def get_notes_list(self):
        notes_list = list()
        try:
            with open(self.file, 'r', encoding= 'utf-8') as f:
                data = json.loads(f.read())
            data.sort(key=lambda x: x['date'])
            for item in data:
                notes_list.append(Note(item['id'], item['date'], item['title'], item['text']))
            return notes_list
        except ValueError:
            return self.notes
        
    def create_notes(self, note):
        self.notes = self.get_notes_list()
        max_id = 0
        for item in self.notes:
            if item.id > max_id:
                max_id = item.id
        note.id = max_id + 1
        
        self.notes.append(note)
        self.save_notes(self.notes)
        
    def save_notes(self, notes):
        json_string = list()
        for note in notes:
            json_string.append({'id': note.id, 'date': note.date, 'title': note.title, 'text': note.text})
        notes_json = json.dumps(json_string, indent=4, ensure_ascii=False, sort_keys=False, default=str)
        with open(self.file, 'w', encoding= 'utf-8') as f:
            f.write(notes_json)
            
    def update_note(self, search_id, note):
        for item in self.notes:
            if item.id == search_id:
                item.date = note.date
                item.title = note.title
                item.text = note.text
                
        self.save_notes(self.notes)
    
    def remove_note(self, search_id):
        self.notes = self.get_notes_list()
        for key, value in enumerate(self.notes):
            if value.id == search_id:
                del self.notes[key]
                
        self.save_notes(self.notes)
        
    def remove_all_notes(self):
        self.notes = self.get_notes_list()
        self.notes.clear()
        self.save_notes(self.notes)