"""
Example how fixmath module changed math.pi but didn't affect any other function
"""

import fixmath
import math


if __name__ == "__main__":
    print(math.floor(3.2))
    for i in range(100):
        print(math.pi)
