public_attribute = 12
__private_attribute = 34


def public_method():
    __private_method()


def __private_method():
    print(__private_attribute)
