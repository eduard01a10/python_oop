from person import Person

class Dishwasher(Person):

    def __init__(self, name, age, gender):
        super(Dishwasher, self).__init__(name, age, gender)

    def wash(self):
        return "The dishwasher can wash the dishes"