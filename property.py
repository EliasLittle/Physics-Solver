from relatable import *

"""
Objects of this class are nodes in the graph
A property
e.g. Force, mass, or time
"""

class Property (Relatable):

    relations = set() #Storage type TBD

    def __init__(self, tag, value=None, unit=None):
        self.tag = tag
        self.name = super().getName(tag)
        self.value = value
        self.unit = unit

    def addRelation(self,R):
        self.relations.add(R)

    def getName(self):
        return self.name

    def toString(self):
        s = ""
        for r in self.relations:
            s += r.toString() + " | "
        return "Property [ {} ] tagged [ {} ] with relations [ {} ] with value [ {} ] in [ {} ]".format(self.name, self.tag, s[:-3], self.value, self.unit)


if __name__ == '__main__':
    F1 = Property("Force",5,"meters")
    print(F1.toString())
