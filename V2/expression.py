from sympy import *
from sympy.parsing.sympy_parser import parse_expr
from relatable import *
from property import Property

class Expression (Relatable):

    def __init__(self, expr, name=None):
        self.tag = expr
        self.name = super().getName(str(self.tag))
        self.expr = parse_expr(expr, evaluate=False)
        self.props = []
        self.vars = list(self.expr.free_symbols)
        self.status = 1
        self.color = self.setColor()

    def setProps(self, instantiated_props):
        self.props=instantiated_props

        # Adds Props that weren't previously instantiated
        new_props = []
        for var in self.vars:
            if str(var) not in ([prop.tag for prop in self.props]):
                new_props.append(Property(str(var)))
        self.props.extend(new_props)

        # Adds this relation to all connected props
        for p in self.props:
            p.addRelation(self)

        self.setStatus()
        return new_props

    def setStatus(self):
        valued_vars = 0
        for prop in self.props:
            if prop.value != None:
                valued_vars += 1

        status_options = {
        len(self.vars) : 3,   # 3 Solved
        len(self.vars)-1 : 2, # 2 Solvable
        0:0                   # 0 No valued props
        # else : 1 ->         # 1 Some valued props
        }

        self.status = status_options.get(valued_vars,1)
        self.setColor()


    def solve(self):
        if self.status == 3:
            raise ValueError("Already solved")
        if self.status != 2:
            raise ValueError("Solved or Not enough values")
        else:
            toSolve = [prop for prop in self.props if prop.value == None][0]
            valued = [prop for prop in self.props if prop != toSolve]
            vals = [(prop.tag,prop.value) for prop in valued]
            ans = solveset(self.expr,toSolve.tag).subs(vals)
            toSolve.setValue(ans)
            self.setStatus()
            toSolve.setStatus()


if __name__ == '__main__':
    props = {
    "FRC" : None,
    "ACC" : 3,
    "MAS" : 2,
    "ARE" : None,
    "PRS" : None,
    "LEN" : None
    }

    PropObjs = {}
    for tag, val in props.items():
        x = Property(tag,value=val)
        PropObjs[tag] = x

    x = Expression("MAS * ACC - FRC")
    instantiated_props = [PropObjs[str(sym)] for sym in x.vars]
    x.setProps(instantiated_props)
    x.solve()
