from person import Person

class Manager(Person):

    def __init__(self, name, age, gender):
        super(Manager, self).__init__(name, age, gender)

    def management(self):
        return "The manager can see if everything is working properly"