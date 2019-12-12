class tag:
    def __init__(self, value):
        self._value = value
    
    def value(self):
        return self._value

    def name(self):
        raise NotImplementedError

    def __str__(self):
        return f"<{self.name()}>{self.value()}</{self.name()}>"

#конкретные компоненты
class p_tag(tag):
    def name(self):
        return "p"
  
class td_tag(tag):
    def name(self):
        return "td"

#абстрактный декторатор

class tag_decorator(tag):
    def __init__(self, wrapped):
        super().__init__(wrapped.value())
        self._wrapped = wrapped

    def name(self):
        return self._wrapped.name()

    def __str__(self):
        raise NotImplementedError

#конкретные декораторы

class italic(tag_decorator):
    def __str__(self):
        return f"<{self._wrapped.name()}><i>{self._wrapped.value()}</i></{self._wrapped.name()}>"

class bold(tag_decorator):
    def __str__(self):
        return f"<{self._wrapped.name()}><b>{self._wrapped.value()}</b></{self._wrapped.name()}>"

t = p_tag("TDecorator")

t = bold(t)

t = italic(t)

print(t)