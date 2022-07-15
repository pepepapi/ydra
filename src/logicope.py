from constants import *
class LogiCope:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def _and(a, b):
        return a and b

    def _or(a, b):
        return a or b

    def _not(a):
        return bool(~a + 2)

    def _nand(a, b):
        x = a and b
        return bool(~x + 2)

    def _nor(a, b):
        x = a or b
        return bool(~x + 2)