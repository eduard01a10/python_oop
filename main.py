##This is a basic OOP project with python
from person import Person
from chef import Chef
from manager import Manager
from waiter import Waiter
from dishwasher import Dishwasher
from client import Client

if __name__ == "__main__":
    
    c = Chef("Jesus", 45, "Male")
    m = Manager("Beto", 72, "Male")
    w = Waiter("Eduardo", 25, "Male")
    d = Dishwasher("Sarah", 33, "Female")
    cl = Client("Female")

    print(f"{c.name} is the chef name, is {c.age} years old, and is {c.gender}. {c.cook()}")
    print(f"{m.name} is the manager name, is {m.age} years old, and is {m.gender}. {m.management()}")
    print(f"{w.name} is the waiter name, is {w.age} years old, and is {w.gender}. {w.serve()}")
    print(f"{d.name} is the dishwasher name, is {d.age} years old, and is {d.gender}. {d.wash()}")
    print(f"The client is a {cl.gender} and {cl.order()}")