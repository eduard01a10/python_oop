from person import Person

class Waiter(Person):

    def __init__(self, name, age, gender):
        super(Waiter, self).__init__(name, age, gender)

    def serve(self):
        return "The waiter can serve the food"