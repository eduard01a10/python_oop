from person import Person

class Chef(Person):

    def __init__(self, name, age, gender):
        super(Chef, self).__init__(name, age, gender)

    def cook(self):
        return "The chef can cook good dishes"