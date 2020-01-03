#NOT OPERATIONAL
from property import *
from Operator import *

# TODO: Change name globally to ExTree
class Et:
    # Constructor to create a node
    def __init__(self, node, left=None, right=None):
        self.node = node
        self.value = node.value
        self.left = left
        self.right = right

    # Returns the string representing the formula for the current expression tree
    # XXX: Should be gotten rid of, should use Relation.toString()
    def toString(self):
        # QUESTION: Does spliting up the left and right cause issues in certain circumstances?
        s = ""
        if self.left is not None:
            s+=self.left.toString()

        s+=str(self.node.name)

        if self.right is not None:
            s+=self.right.toString()

        return s

    # A helper function to do inorder traversal, or for printing the expression that is being evaluated
    # NOTE: Does not include parenthesis
    def inorder(self):
        # QUESTION: Does spliting up the left and right cause issues in certain circumstances?
        s = ""
        if self.left is not None:
            s+=self.left.inorder()
        try:
            s+=str(self.value)
        except:
            print("node {} has no value".format(t.node.getName()))

        if self.right is not None:
            s+=self.right.inorder()
        return s

    def solve(self):
        return evaluateExpressionTree(self)

# Returns root of constructed tree for
# given postfix expression
def constructTree(pflist):
    stack = []

    postfix = pflist
    # Traverse through every character of input expression
    for node in postfix :

        # If operand, simply push into stack
        if type(node) == Property:
            t = Et(node)
            stack.append(t)

        # Operator
        else:
            assert type(node) == Operator, "Invalid node type"
            # Pop two top nodes
            t = Et(node)
            t1 = stack.pop()
            t2 = stack.pop()

            # make them children
            t.right = t1
            t.left = t2

            # Add this subexpression to stack
            stack.append(t)

    # Only element  will be the root of expression tree
    t = stack.pop()

    return t

def evaluateExpressionTree(root):
    #print(root.node)
    # empty tree
    if root is None:
        return 0

    # leaf node
    if root.left is None and root.right is None:
        return int(root.value)

    # evaluate left tree
    left_sum = evaluateExpressionTree(root.left)
    #print("Left Sum: "+str(left_sum))

    # evaluate right tree
    right_sum = evaluateExpressionTree(root.right)
    #print("Right Sum: "+str(right_sum))

    # construct operation switch
    def switch(val):
        switcher = {
            '+': left_sum + right_sum,
            '-': left_sum - right_sum,
            '*': left_sum * right_sum,
            '/': left_sum / right_sum,
            '^': left_sum ** right_sum
        }
        return switcher.get(val, "Invalid Operation")

    # check which operation to apply
    s = switch(root.value)
    if(s == "Invalid Operation"):
        raise NotImplementedError
    else:
        return s

if __name__ == '__main__':
    r = constructTree("4,3,+,2,7,*,24,+,-")
    a=4
    o = Et(str(a))
    print(inorder(o))
    print(inorder(r))
    print(evaluateExpressionTree(r))
