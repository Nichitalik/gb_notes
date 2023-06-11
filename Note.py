class Note(object):
    def __init__(self, id, date, title, text):
        self.id = id
        self.title = title
        self.text = text
        self.date = date
        
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id
        
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        self._title = title
        
    @property
    def text(self):
        return self._text
    
    @text.setter
    def text(self, text):
        self._text = text
        
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        self._date = date
        
    def __str__(self):
        return f'Заметка номер: {self._id}\nПоследние изменения: {self._date}\n{self._title}\n{self._text}'