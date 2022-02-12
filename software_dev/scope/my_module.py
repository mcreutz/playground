module_var = 12


def module_function():
    print(module_var)
    # module_var = 13
    # print(module_var)


class MyClass():
    def method(self):
        print(module_var)
        # module_var = 13
        # print(module_var)


"""
-> As long as access to a module variable is only reading, it can be accessed 
just fine. But if access is writing within the function, the variable is 
considered local. If you want writing-access to a module variable, you need 
to declare it as 'global' within the function.
"""
