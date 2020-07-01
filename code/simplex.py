from gurobipy import *

model=Model("simplex")

x1=model.addVar(vtype="C")
x2=model.addVar(vtype="C")
x3=model.addVar(vtype="C")

model.update()

model.addConstr(x1+x2+2*x3<=4)
model.addConstr(2*x1+3*x3<=5)
model.addConstr(2*x1+x2+3*x3<=7)
model.addConstr(x1>=0)
model.addConstr(x2>=0)
model.addConstr(x3>=0)

model.setObjective(3*x1+2*x2+4*x3,GRB.MAXIMIZE)

model.optimize()
print("Opt. Val.=", model.ObjVal)
print("(x1,x2,x3)=", x1.X,x2.X,x3.X)