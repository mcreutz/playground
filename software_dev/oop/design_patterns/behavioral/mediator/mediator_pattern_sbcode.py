
from abc import ABCMeta, abstractmethod


class Mediator():
    "A Subject whose notify method is mediated"

    def __init__(self):
        self._components = set()

    def add(self, component):
        "Add components"
        self._components.add(component)

    def notify(self, message, originator):
        "Add components except for the originator component"
        for component in self._components:
            if component != originator:
                component.receive(message)


class IComponent(metaclass=ABCMeta):
    "An interface that each component will implement"

    @staticmethod
    @abstractmethod
    def notify(message):
        "The required notify method"

    @staticmethod
    @abstractmethod
    def receive(message):
        "The required receive method"


class Component(IComponent):
    "Each component stays synchronized through a mediator"

    def __init__(self, mediator, name):
        self._mediator = mediator
        self._name = name

    def notify(self, message):
        print(self._name + ": >>> Out >>> : " + message)
        self._mediator.notify(message, self)

    def receive(self, message):
        print(self._name + ": <<< In <<< : " + message)


if __name__ == "__main__":
    "The Mediator Use Case Example"

    MEDIATOR = Mediator()
    COMPONENT1 = Component(MEDIATOR, "Component1")
    COMPONENT2 = Component(MEDIATOR, "Component2")
    COMPONENT3 = Component(MEDIATOR, "Component3")
    MEDIATOR.add(COMPONENT1)
    MEDIATOR.add(COMPONENT2)
    MEDIATOR.add(COMPONENT3)

    COMPONENT1.notify("data A")
    COMPONENT2.notify("data B")
    COMPONENT3.notify("data C")
