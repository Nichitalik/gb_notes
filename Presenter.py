# 1) получение списка заметок
# 2) создание новой заметки
# 3) сохранение заметки
# 4) обновление существующей заметки
# 5) удаление заметки
# 6) удаление всех заметок

from Operation import Operation
from View import View

class Presenter(object):
    
    def __init__(self, view, operation):
        self.view = view
        self.operation = operation
    
    def show_notes_list(self):
        self.view.print_notes_list(self.operation.get_notes_list())
        
    def create_new_note(self, note):
        self.operation.create_notes(note)
        
    def update_note(self, search_id, note):
        self.operation.update_note(search_id, note)
        
    def remove_note(self, search_id):
        self.operation.remove_note(search_id)
        
    def remove_all_notes(self):
        self.operation.remove_all_notes()