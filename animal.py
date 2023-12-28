class Animal:
    count = -1

    def __init__(self, id_animal=None, name=None, type_animal=None, command=None):
        self.name = name
        self.type_animal = type_animal
        self.command = command
        if id_animal == None:
            Animal.count += 1
            self.id_animal = str(Animal.count)
        else:
            self.id_animal = id_animal

    def set_name(self, name):
        self.name = name

    def set_type_animal(self, type_animal):
        self.type_animal = type_animal

    def get_id_animal(self):
         return self.id_animal

    def get_name(self):
        return self.name

    def get_type_animal(self):
        return self.type_animal

