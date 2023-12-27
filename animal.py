class Animal:
    def __init__(self, name, type_animal, birthday, command):
        self._name = name
        self._type_animal = type_animal
        self._birthday = birthday
        self._command = command

    def set_name(self, name):
        self._name = name

    def set_type_animal(self, type_animal):
        self._type_animal = type_animal

    def set_birthday(self, birthday):
        self._birthday = birthday

    def set_command(self, command):
        self._command = command

    def get_name(self):
        return self._name

    def get_type_animal(self):
        return self._type_animal

    def get_birthday(self):
        return self._birthday

    def get_command(self):
        return self._command
