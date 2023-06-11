# 1) получение списка заметок
# 2) создание новой заметки
# 3) сохранение заметки
# 4) обновление существующей заметки
# 5) удаление заметки
# 6) удаление всех заметок

from Operation import Operation as Operation

class View(object):
    
    def show_operation():
        print(
            "\
            1 - получение списка заметок\n\
            2 - создание новой заметки\n\
            3 - обновление существующей заметки\n\
            4 - удаление заметки\n\
            5 - удаление всех заметок\n\
            6 - Выход")
    
    def masage_save():
        print("Заметка сохранена")
        
    def masage_delete():
        print("Заметка удалена")
    
    def print_notes_list(notes):
        print("Список существующих заметок:\n")
        for note in notes:
            print(note, "\n")
        print('Конец\n')

    def title_request():
        print('Введите заголовок заметки\n')
        
    def text_request():
        print('Введите текст заметки\n')
    
    
        