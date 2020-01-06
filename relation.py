import ExpressionTree as ET
from property import *
from Operator import *
from relatable import *
import re
from random import random

"""
A relation between a set of properties
Takes multiple inputs to solve for the final output
A child of method
e.g. {F,m,a} takes two solves for the third
"""
class Relation:

    def __init__(self,expression,properties=[]):
        self.props = properties #A Collection of property objects
        if len(self.props) != 0:
            for p in self.props:
                p.addRelation(self)
        #Precondition: Expression given so that it equals 0
        self.expression = expression #For giving a printable string
        self.vars = self.parseVars(expression) #Assigns the property placeholder tags that parseVars provides
        self.evaluable = ET.constructTree(self.parseExp(expression)) #Creates an ExpressionTree from the postfix that parseExp returns

    def getProps(self):
        return props


    def getName(self):
        return self.expression.replace('{','').replace('}','').replace('|','')


    def toString(self):
        return self.getName()


    # Parses the expression for the variable
    def parseVars(self,s):
        return re.findall('\{(.*?)\}',s)

    def parseExp(self,s):
        inf = []
        # Takes the right side of the equation, and seperates all variables and operators, then splits all into a list
        s = s.replace('{','|').replace('}','|')[1:-1].split('|')
        for i in s:
            if isOperator(i):
                inf.append(Operator(i))
            else:
                if i in set(prop.tag for prop in self.props):
                    for prop in self.props:
                        if i == prop.tag:
                            inf.append(prop)
                            break
                else:
                    newProp = Property(i)
                    newProp.addRelation(self)
                    self.props.append(newProp)
                    inf.append(newProp)
        # print("--- Infix list created ---")
        # print([p.name for p in inf])

        return infToPostf(inf)


    # TODO: Use the assigned formula to solve for the given 'variable'
    def solve(self, var):
        # Check for other variable's values
        for prop in self.props:
            if (prop.value == None and prop != var):
                prop.solve()

        # Evaluate the new expression tree and return the answer
        def f(x):
            prop.value = x
            return ET.evaluateExpressionTree(self.evaluable)

        a = random()*1000
        b = 0
        x = a+b/2
        if(f(a)*f(b) > 0):
            print(f(a))
            print(f(b))
            print("fa and fb must be different signs")
        else:
            run = True
            tries = 0
            while run and tries < 100:
                if abs(f(x)) < 0.001:
                    prop.value = x
                    run = false
                    break
                if f(a)*f(x) > 0:
                    a=x
                else:
                    b=x
                x=(a+b)/2
                tries += 1




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
                while(top.prec >= i.prec and top.value not in paren and len(stack) > 1):
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

    # print("--- Postfix list created ---")
    # print([p.name for p in postfix])
    return postfix

if __name__ == '__main__':
    a = Relation(["F","m","a"],"{F}={m}*{a}")
    print(a.getName())
    print(a.toString())
