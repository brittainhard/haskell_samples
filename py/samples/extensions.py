class SuperInt(int):
    """
    Redefine the add method.
    """

    def __init__(self, digit):
        self.digit = digit

    def __add__(self, int):
        return self.digit + int + 1


def test_super_int():
    a = SuperInt(1)
    print(a + 1)


class SuperList(list):
    """
    Designed it so that we can pass stuff in as args and it will just list
    everything we pass in. No different than surrounding it with [] but its
    still kinda cool.
    """

    def __init__(self, *args):
        print(args)
        super().__init__(x for x in args)

    @classmethod
    def duplicate(cls, *args):
        print(args)
        return cls(args)


def test_super_list():
    b = SuperList(1, 2, 3, "potato")
    c = [1, 2, 3]

a = SuperList.duplicate(1, 2, 3)
b = SuperList(4, 5, 6)

