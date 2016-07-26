"""
Example of operator overloading.
You can use / operator to appent to Path
"""

import os.path


class Path(object):

    def __init__(self, dirs):
        self.dirs = [dirs] if isinstance(dirs, str) else list(dirs)


    def __str__(self):
        return os.path.join(*self.dirs)


    def exists(self):
        return os.path.exists(str(self))


    def __truediv__(self, divider):
        return Path(self.dirs + [divider])


    def __rtruediv__(self, divider):
        return Path([divider] + self.dirs)


if __name__ == "__main__":
    path = Path('test')
    path2 = path / 'abc'
    path3 = 'abc' / path
    print(path)
    print(path2)
    print(path3)