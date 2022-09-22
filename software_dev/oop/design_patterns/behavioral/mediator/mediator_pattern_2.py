from abc import ABC

"""
Components get reference of the mediator on creation. Mediator then gets 
references of all components.

'Notify' method of the mediator is called to communicate to mediator. Mediator 
then calls 'receive' method of all other components. Each component then 
decides, if to react on this call. If a component reacts on a call from the 
mediator, it can itself call the 'receive' method of the mediator to pass the 
result back to the calling component.

Advantages of this implementation:

The functional code stays in the component classes. So the 'mediator' class 
does not become a "god-class".

Also, the mediator does not directy call any funtional methods from the 
components. So the component's methods that are not meant to be called from 
outside can be declared as private.

Disadvantages:

Arbitrary messages, prone to induce errors, that are hard to find and to track.

Within the constructors of the components, no methods of other components can 
or should be be called, as yo cannot be sure, what other components are already
created.
"""


class Mediator():
    """
    Mediator class to pass calls and data between components. Does not hold any 
    functional code.
    """

    def __init__(self):
        self._components = set()

    def add(self, component):
        """Add component reference to mediator"""
        self._components.add(component)

    def notify(self, originator, message, data):
        """Call all components except for the originator component"""

        for component in self._components:
            if component != originator:
                result = component.receive(message, data)
                # Return the value, as soon as one component has returned a result
                if result != None:
                    return result


class IComponent(ABC):
    """Components base class"""

    def __init__(self, mediator, name):
        self._mediator = mediator
        self._name = name

    def receive(self):
        """Abstract method"""
        raise NotImplementedError


class Component_1(IComponent):
    """
    Concrete component class. Holds the functional code. Calls other component's 
    methods via the mediator.
    """

    def method_1(self):
        """Public functional method to be called from a client"""
        result = self._mediator.notify(
            originator=self, message="method_two", data="data")
        print(result)

    def receive(self, message, data):
        """
        Gets called from mediator for each call from other components. Decides 
        on the reaction based on 'message'.
        """
        pass


class Component_2(IComponent):
    """
    Concrete component class. Holds the functional code. Calls other component's 
    methods via the mediator.
    """

    def __method_2(self, data):
        """
        Private functional method. Not visible to the client, but can be called 
        from other components through the mediator.
        """
        return str.upper(data)

    def receive(self, message, data):
        """
        Gets called from mediator for each call from other components. Decides 
        on the reaction based on 'message'.
        """

        if message == "method_two":
            result = self.__method_2(data)
            return result
        elif message == "another_message_to_act_on":
            return "something"


if __name__ == "__main__":
    """This is the client, calling the components' public methods."""

    m = Mediator()
    c1 = Component_1(m, "c1")
    c2 = Component_2(m, "c2")
    m.add(c1)
    m.add(c2)

    c1.method_1()
