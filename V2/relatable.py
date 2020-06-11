from propsDict import propsDict
"""
Objects of this class are part of a relationship
Properties and operators are children
"""

class Relatable:

    def __init__(self, tag, value=None):
        self.tag = tag
        self.name = self.getName(tag)
        self.value = value
        self.status = 1
        self.color = self.setColor()


    @staticmethod
    def getName(tag):
        return propsDict[tag]

    def setColor(self):
        color_options = {
        3 : 'Green',
        2 : 'Blue',
        1 : 'Grey',
        0 : 'Red'
        }
        self.color = color_options[self.status]

    def toString(self):
        s = ""
        for r in self.relations:
            s += r.toString() + " | "
        return "Relatable [ {} ] tagged [ {} ] and value [ {} ]".format(self.name, self.tag, self.value)
