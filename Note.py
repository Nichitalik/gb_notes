class Note(object):
    def __init__(self, id, title, text, dateTime):
        self.id = id
        self.title = title
        self.text = text
        self.dateTime = dateTime
        
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
