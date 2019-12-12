class base:
    def get_name(self):
        raise NotImplementedError    

    def get_cost(self):
        raise NotImplementedError

class coffee(base):
    def get_name(self):
        return 'coffee'

    def get_cost(self):
        return 10

class tea(base):
    def get_name(self):
        return 'tea'

def add_milk_cost(obj):
    return obj.get_cost() + 1.5

def add_milk_name(obj):
    return f"{obj.get_name()}, milk"

m = coffee()

print(add_milk_cost(m))
print(add_milk_name(m))
