import ExpressionTree as ET
from property import *
from Operator import *
from relatable import *
import re

"""
A relation between a set of properties
Takes multiple inputs to solve for the final output
A child of method
e.g. {F,m,a} takes two solves for the third
"""
class Relation:
    props = []
    formula = [] # QUESTION: Is this needed, can it be deleted?

    def __init__(self,expression,properties=[]):
        self.props = properties #A Collection of property objects
        if len(self.props) != 0:
            for p in self.props:
                p.addRelation(self)
        self.expression = expression #For giving a printable string
        self.dVar, self.vars = self.parseVars(expression) #Assigns the property placeholder tags that parseVars provides
        self.evaluable = ET.constructTree(self.parseExp(expression)) #Creates an ExpressionTree from the postfix that parseExp returns


    def getProps(self):
        return props


    def getName(self):
        return self.expression.replace('{','').replace('}','').replace('|','')


    def toString(self):
        return self.getName()


    # Parses the expression for the variables, both default and other properties
    def parseVars(self,s):
        s = s.split('=')
        s1 = s[0][1:-1]
        s2 = re.findall('\{(.*?)\}',s[1])

        return [s1,s2]


    def parseExp(self,s):
        inf = []
        # Takes the right side of the equation, and seperates all variables and operators, then splits all into a list
        s = s.split('=')[1].replace('{','|').replace('}','|')[1:-1].split('|')
        for i in s:
            if isOperator(i):
                inf.append(Operator(i))
            else:
                if len(self.props) != 0:
                    for prop in self.props:
                        if i == prop.tag:
                            inf.append(prop)
                            break
                newProp = Property(i)
                newProp.addRelation(self)
                self.props.append(newProp)
                inf.append(newProp)
        #print("--- Infix list created ---")

        return infToPostf(inf)


    # TODO: Use the assigned formula to solve for the given 'variable'
    def solve(self, varTag):
        # Take self.expression, and transform it to solve for the given 'variable'
        # Evaluate the new expression tree and return the answer
        for prop in self.props:
            if prop.value == None:
                print("Missing Values")
                return
        if varTag == self.dVar:
            return self.evaluable.solve()
        else:
            print("Not yet implemented")

##-------------------------------------#

# A helper function to check if 'c' is an operator
def isOperator(c):
    if (c in ('+','-','*','/','^','(',')')):
        return True
    else:
        return False


def infToPostf(infix):
    postfix = []
    stack = []

    paren = ('(',')')
    for i in infix:
        if(len(stack)>0): top = stack[len(stack)-1]

        if type(i) == Property: # Operand
            postfix.append(i)
        # Operator
        elif i.value == '(': stack.append(i)
        elif i.value != ')':
            if(len(stack)==0 or top.prec < i.prec or top.value == '('):
                stack.append(i)
            else:
                while(top.prec >= i.prec and top.value not in paren):
                    postfix.append(stack.pop())
                    top = stack[len(stack)-1]
                stack.append(i)
        else:
            while top.value != '(':
                postfix.append(stack.pop())
                top = stack[len(stack)-1]
            stack.pop()

    while len(stack) > 0:
        postfix.append(stack.pop())

    return postfix

if __name__ == '__main__':
    a = Relation(["F","m","a"],"{F}={m}*{a}")
    print(a.getName())
    print(a.toString())
