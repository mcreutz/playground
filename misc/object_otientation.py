"""
Reference for object oriented programming in Python
Todo:
- super()
- Interfaces
- @property
- abc
- composition

"""

global_variable = 12


def global_function(par1='standardValue'):
    return par1


class MyClass1:
    # Static attributes / variables
    static_public_attribute = 1        # public, because no underscores. External acces possible.
    _static_protected_attribute = 2    # protected, because one underscore. External access only possible from subclasses.
    __static_private_attribute = 3     # private, because two underscores. External access NOT possible


    # Constructor / destructor
    def __init__(self, par1='standardValue'):       # constructor
        self.object_attribute = par1
        MyClass1.static_public_attribute += 1

    def __del__(self):                              # destructor
        print("Object is being deleted")
        MyClass1.static_public_attribute -= 1


    # Class method  / static method                 # https://www.geeksforgeeks.org/class-method-vs-static-method-python/
    @classmethod
    def class_method(cls, par1):                    # can access class status
        return par1

    @staticmethod
    def static_method(par1):                        # can not access class status
        return par1


    # Object methods
    def method1(self, parameter1="standard"):       # public, because no underscores. External rw possible.
        return parameter1

    def _method2(self, parameter2="standard"):      # protected, because one underscore. External rw possible,
                                                    # but not suggested.
        return parameter2

    def __method3(self, parameter3="standard"):     # private, because two underscores. External rw NOT possible,
                                                    # invisible
        return parameter3


class MyInterface():
    def another_method_1():
        raise NotImplementedError


class MyClass2(MyClass1, MyInterface):      # Inherits from MyClass1, MyInterface
    another_static_public_attribute = 1

    def another_method_1(self, parameter1="standard"):
        return parameter1


if __name__ == '__main__':
    my_object_1 = MyClass1()
    my_object_2 = MyClass1('nonStandard')

    my_result_1 = my_object_1.method1("nonStandard")

    my_result_2 = my_object_1.class_method("loremipsum")
    my_result_2 = MyClass1.class_method("loremipsum")   # Same as above

    my_class_value = my_object_1.static_public_attribute
    my_object_1_value = my_object_1.object_attribute