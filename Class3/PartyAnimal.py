class PartyAnimal:
    x = 0
    name = ''

    def __init__(self, name):
        self.name = name
        print(self.name, ' contructed')

    def party(self):
        self.x = self.x + 1
        print(self.name, 'party count ', self.x)