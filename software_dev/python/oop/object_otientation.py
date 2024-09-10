"""
Reference for object oriented programming in Python
Todo:
- super()
- Interfaces
- @property
- abc
- composition
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass


global_variable = 12


def global_function(par_1="default_value"):
    return par_1


class MyClass1:

    # Static attributes / variables
    # public, because no underscores. External acces possible.
    static_public_attribute = 1
    # protected, because one underscore. External access only possible from
    # subclasses.
    _static_protected_attribute = 2
    # private, because two underscores. External access NOT possible
    __static_private_attribute = 3

    def __init__(self, par_1="default_value"):
        """constructor"""
        self.object_attribute = par_1
        MyClass1.static_public_attribute += 1

    def __del__(self):
        """destructor"""
        print("Object is being deleted")
        MyClass1.static_public_attribute -= 1

    @classmethod
    def class_method(cls, par_1):
        """
        can access class status
        compulsory argument 'cls' as first parameter is mandatory
        """
        return par_1

    @staticmethod
    def static_method(par_1):
        """
        can not access class properties
        (although it could, by accessing 'MyClass.my_attribute')
        """
        return par_1

    # Object methods
    def method1(self, parameter_1="default_value"):
        """public, because no underscores. External access possible."""
        return parameter_1

    def _method2(self, parameter_2="default_value"):
        """
        protected, because one underscore. External acces possible only from
        inheriting classes
        """
        return parameter_2

    def __method3(self, parameter_3="default_value"):
        """
        private, because two underscores. External acces NOT possible,
        invisible
        """
        return parameter_3


class MyAbstractBaseClass(ABC):

    @abstractmethod
    def another_method_1():
        raise NotImplementedError


class MyClass2(MyClass1, MyAbstractBaseClass):
    """Inherits from MyClass1, MyInterface"""

    another_static_public_attribute = 1

    def another_method_1(self, parameter_1="default_value"):
        return parameter_1


@dataclass
class MyDataClass:
    """Dataclass"""

    data_attribute_1: int
    data_attribute_2: str


if __name__ == "__main__":
    my_object_1 = MyClass1()
    my_object_2 = MyClass1("concrete_value")

    my_result_1 = my_object_1.method1("concrete_value")

    my_result_2 = my_object_1.class_method("loremipsum")
    my_result_2 = MyClass1.class_method("loremipsum")  # Same as above

    my_class_value = my_object_1.static_public_attribute
    my_object_1_value = my_object_1.object_attribute

    my_dataclass_object = MyDataClass(1, "string")
    my_dataclass_result = my_dataclass_object.data_attribute_1
