class Mother():
    def whoareyou(self):
        print("I am mother.")


class Daughter(Mother):
    def whoareyou(self):
        # overridden method
        print("I am daughter.")


mother = Mother()
daughter = Daughter()

# Call overridden method
daughter.whoareyou()  # --> I am daughter.


class Household():
    def __init__(self, mother: Mother) -> None:
        self.mother = mother

    def identify(self):
        self.mother.whoareyou()


# injecting an instance of the baseclass
old_household = Household(mother=mother)
old_household.identify()  # --> I am mother.

# injecting an instance of a subclass
new_household = Household(mother=daughter)  # -> accepted by static typechecker

# call overridden method
new_household.identify()  # --> I am daughter.
