from property import *
from Operator import *
from relation import *
from ExpressionTree import *

M1 = Property("mass",value=10,unit="kg")
A1 = Property("acc",value=2,unit="m/s^2")
F1 = Property("frc",value=20,unit="N")

r = Relation("{mass}*{acc}-{frc}",properties=[M1,A1,F1])

F1.value = r.solve("frc")

print(F1.toString())


print("\n\nPart 2\n\n")
exp = "{pos_1}={pos}+{vel}*{time}*{0.5}*{acc}*{time}^{2}"
a = Relation(exp)
print("a created")
s = ""
for i in r.parseExp("{frc}={mass}*{acc}"):
    print(i.name)
    s += i.name + ", "

print(s)
