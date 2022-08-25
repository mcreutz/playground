class Whatever():

    attr = 0

    def __init__(self) -> None:
        pass


if __name__ == "__main__":
    we1 = Whatever()
    we2 = Whatever()

    print(Whatever.attr)
    print(we1.attr)
    print(we2.attr)
    print("-----------")

    Whatever.attr = 100
    print(Whatever.attr)
    print(we1.attr)
    print(we2.attr)
    print("-----------")

    we1.attr = 200
    print(Whatever.attr)
    print(we1.attr)
    print(we2.attr)

    # 0
    # 0
    # 0
    # -----------
    # 100
    # 100
    # 100
    # -----------
    # 100
    # 200
    # 100
