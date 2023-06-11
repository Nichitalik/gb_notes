import datetime

from Presenter import Presenter
from View import View
from Operation import Operation
from Note import Note

def run():
    while True:
        p = Presenter(View,Operation('notesData.json'))
        View.show_operation()
        choice = int(input("Введите номер операции: "))
        if choice == 6:
            break
        if choice == 1:                 # 1) получение списка заметок
            p.show_notes_list()
        if choice == 2:               # 2) создание новой заметки
            p.create_new_note(Note(0, set_date(), set_title(), set_text()))
        if choice == 3:                 # 3) обновление существующей заметки
            id = id_request()
            p.update_note(id, Note(id, set_date(), set_title(), set_text()))
        if choice == 4:                 # 4) удаление заметки
            p.remove_note(id_request())
            View.masage_delete()
        if choice == 5:                    # 5) удаление всех заметок
            p.remove_all_notes()
            
            
        
def set_date():
    return datetime.datetime.now()

def set_title():
    View.title_request()
    return input()

def set_text():
    View.text_request()
    return input()

def id_request():
    return int(input("Введите id заметки: "))