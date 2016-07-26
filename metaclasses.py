"""
Example how to use metaclasses to change order of method load in inheritance tree
"""


class Library(type):
    """
    Classes with Library metaclass will search in inheritance tree ordered
    alphebitacaly
    """

    def mro(cls):
        return sorted(
            super().mro(),
            key=lambda cls: cls.__name__
        )


class AClass(metaclass=Library):
    def hello(self):
        print('hello', 'A')


class BClass(AClass):
    def hello(self):
        print('hello', 'B')


class CClass(BClass):
    def hello(self):
        print('hello', 'C')


if __name__ == "__main__":
    print(CClass.mro())
    CClass().hello()
