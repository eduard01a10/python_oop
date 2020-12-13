from person import Person

class Client(Person):

    def __init__(self, gender):
        self.gender = gender

    def order(self):
        return "The client can order the food it likes"

