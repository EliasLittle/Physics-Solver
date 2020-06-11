from relatable import *

"""
Objects of this class are nodes in the graph
A property
e.g. Force, mass, or time
"""

class Property (Relatable):

    relations = set() #Storage type TBD

    def __init__(self, tag: str, value=None, unit=None):
        self.tag = tag
        self.name = super().getName(str(tag))
        self.value = value
        self.unit = unit
        self.status = 1
        self.color = 'Green' if (self.value != None) else 'Red'

    def addRelation(self,R):
        self.relations.add(R)

    def getName(self):
        return self.name

    def setValue(self,val):
        self.value = val

    def setStatus(self):
        test = (self.value != None)
        status_options = {
            True : 3, # 3 Solved
            False : 0 # 0 Not solved
        }

        self.status = status_options.get(test)
        self.setColor()

    def solve(self):
        for r in self.relations:
            if all(p.value != None for p in r.props if p != self):
                r.solve(self)
                break
        #TODO: What if none of them are currently totally solvable?

    def toString(self):
        s = ""
        for r in self.relations:
            s += r.toString() + " | "
        return "Property [ {} ] tagged [ {} ] with relations [ {} ] with value [ {} ] in [ {} ]".format(self.name, self.tag, s[:-3], self.value, self.unit)


if __name__ == '__main__':
    F1 = Property("Force",5,"meters")
    print(F1.toString())
