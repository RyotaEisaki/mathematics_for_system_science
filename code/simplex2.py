from gurobipy import *

model=Model("simplex2")

x1=model.addVar(vtype="C")
x2=model.addVar(vtype="C")


model.update()

model.addConstr(-2*x1+x2<=1)
model.addConstr(x1-x2<=-4)
model.addConstr(x1+x2<=2)


model.addConstr(x1>=0)
model.addConstr(x2>=0)


model.setObjective(3*x1+2*x2,GRB.MAXIMIZE)

model.optimize()
print("Opt. Val.=", model.ObjVal)
print("(x1,x2)=", x1.X,x2.X)
