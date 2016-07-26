"""
This module replaces math.pi with it's own implementation that return slightly
wrong number every time. It leaves all other methods and constants intact.

To apply this 'fix', just import this module anywhere in code.
"""

import math as good_math
import random
import sys

class BadMath(object):
    @property
    def pi(self):
        return good_math.pi + (random.random() - 0.5) * 0.00001 
    
    def __getattr__(self, name):
        return getattr(good_math, name)

sys.modules['math']  = BadMath()