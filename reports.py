class cell:
    def __init__(self, text):
        self._text = text
    
    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        self._text = text

    def __str__(self):
        return self._text

class float_cell(cell):
    def __init__(self, text, prec):
        super().__init__(text)
        self._prec = prec

    def __str__(self):
        length = self._prec - len(self.text)        
        if length < 0:
            length = 0
        return ' '*length + self.text

class align:
    def __ge

fc = float_cell('text', 15)

print(fc)
