class MyClass():

    static_attr: int

    def __init__(self) -> None:
        MyClass.static_attr = 12

    @classmethod
    def read(cls):
        print(cls.static_attr)
        cls.static_attr = 13
        print(cls.static_attr)

        print(id(cls))
        print(id(MyClass))  # same


my_object = MyClass()
my_object.read()
