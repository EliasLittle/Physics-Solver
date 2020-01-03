from relatable import *

"""
A wrapper class for operators
child of relatable
e.g. *,/,+,-,^, etc...
"""

class Operator (Relatable):

    def __init__(self, op):
        self.tag = op
        self.name = super().getName(op)
        self.value = op
        self.prec = self.getPrec(op)

    @staticmethod
    def getPrec(op): # Returns precedence of the given operator
        switcher = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '^': 3,
            '(': 4,
            ')': 4
        }
        s = switcher.get(op, "Precedence not defined")
        if s == "Precedence not defined":
            raise NotImplementedError
        else:
            return s

    def toString(self):
        return "Operator is [ {} ] with precedence [ {} ]".format(self.tag, self.value)


if __name__ == '__main__':
    a = Operator("*")
    print(a.toString())
