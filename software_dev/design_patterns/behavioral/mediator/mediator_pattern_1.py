"""
Components are created with their reference to the mediator set to 'None'.
Mediator gets references of component classes on its creation.
Metiator then sets itself as mediator within the components.

Client calls a component's method. Component then notifies mediator about the 
task. Mediator holds the functional code to handle the calling of other 
components' methods including the passing and receiving of data.

Advantages of this implementation:

Disadvantages:

Components' properties and methods, that are ment to be called only from the 
mediator and not from a client, cannot be declared as private, as the mediator 
needs to be able to call them.

The mediator class(es) contain(s) functional code. Actually the collaboration 
code could be placed in the components OR in the mediator.

Arbitrary messages, prone to induce errors, that are hard to find and to track.

Within the constructors of the components, no methods of other components can 
be called, as the connection to the mediator is established only after the 
initialization of all components.
"""

from __future__ import annotations
from abc import ABC


class Mediator(ABC):
    def notify(self) -> None:
        raise NotImplementedError


class ConcreteMediator(Mediator):
    def __init__(self, c1: Component1, c2: Component2) -> None:
        self.c1 = c1
        self.c1.mediator = self
        self.c2 = c2
        self.c2.mediator = self

    def notify(self, sender: BaseComponent, action: str, parameters: dict) -> str:
        if action == "21":
            result = self.c2.action_21(param_1=parameters['param_1'])
            return result


class BaseComponent(ABC):
    def __init__(self, mediator: Mediator = None) -> None:
        self.mediator = mediator


class Component1(BaseComponent):
    def action_11(self, param_1: str) -> str:
        print("Doing action 11")
        print("Requesting action 21")
        parameters = {'param_1': "Value 11"}
        result = self.mediator.notify(self, "21", parameters)
        print(result)
        return "Result of action 11"


class Component2(BaseComponent):
    def action_21(self, param_1: str) -> str:
        print("Doing action 21")
        return "Result of action 21"


if __name__ == "__main__":
    c1 = Component1()
    c2 = Component2()
    m = ConcreteMediator(c1, c2)

    print("Requesting action 11")
    result = c1.action_11("Value 11")
    print(result)
