from gurobipy import *

model=Model("simplex")

x1=model.addVar(vtype="C")
x2=model.addVar(vtype="C")
x3=model.addVar(vtype="C")
x4=model.addVar(vtype="C")

model.update()

model.addConstr(3*x1+5*x2+2*x3-x4<=4)
model.addConstr(-x1+4*x2+3*x3-2*x4<=-2)
model.addConstr(-2*x1+5*x2+4*x3<=-3)
model.addConstr(2*x1+3*x2-3*x4<=-2)

model.addConstr(x1>=0)
model.addConstr(x2>=0)
model.addConstr(x3>=0)
model.addConstr(x4>=0)

model.setObjective(-x1-x2-x3-x4,GRB.MAXIMIZE)

model.optimize()
print("Opt. Val.=", model.ObjVal)
print("(x1,x2,x3,x4)=", x1.X,x2.X,x3.X,x4.X)