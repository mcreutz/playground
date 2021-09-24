class MyClass_A():
    """The pythonic way to do it."""

    def __init__(self) -> None:
        self.my_prop = None

    @property
    def my_prop(self):
        print("Setter")
        return self._my_prop

    @my_prop.setter
    def my_prop(self, value):
        print("Getter")
        self._my_prop = value


class MyClass_B():
    """An alternative and less pythonic way to do it."""

    def __init__(self) -> None:
        self.my_prop = None

    def get_my_prop(self):
        print("Setter")
        return self._my_prop

    def set_my_prop(self, value):
        print("Getter")
        self._my_prop = value

    my_prop = property(get_my_prop, set_my_prop)


class MyClass_C():
    """An alternative and less pythonic way to do it."""

    def __init__(self) -> None:
        self.my_prop = None

    def get_my_prop(self):
        print("Setter")
        return self._my_prop

    def set_my_prop(self, value):
        print("Getter")
        self._my_prop = value

    my_prop = property()
    my_prop = my_prop.getter(get_my_prop)
    my_prop = my_prop.setter(set_my_prop)


if __name__ == "__main__":
    my_obj_a = MyClass_A()
    my_obj_a.my_prop = "Content"
    print(my_obj_a.my_prop)
