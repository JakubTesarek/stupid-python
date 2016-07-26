"""
List object to which you can append strings by accessing an attribute
"""


class BetterList(object):
    def __init__(self, initial_data=None):
        if initial_data is None:
            initial_data = []
        self._data = initial_data


    def __str__(self):
        return str(self._data)


    def __repr__(self):
        return str(self._data)


    def __getattr__(self, name):
        return BetterList(self._data + [name])


    def __iter__(self):
        return iter(self._data)


if __name__ == "__main__":
    bl = BetterList().a.name.more.words
    print(bl)
    for item in bl:
        print(item)
