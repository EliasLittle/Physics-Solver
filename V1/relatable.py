"""
Objects of this class are part of a relationship
Properties and operators are children
"""

class Relatable:

    def __init__(self, tag, value=None):
        self.tag = tag
        self.name = self.getName(tag)
        self.value = value

    @staticmethod
    def getName(tag):
        # TODO: Create dictionary that retrieves name from tag
        return tag

    def toString(self):
        s = ""
        for r in self.relations:
            s += r.toString() + " | "
        return "Relatable [ {} ] tagged [ {} ] and value [ {} ]".format(self.name, self.tag, self.value)
