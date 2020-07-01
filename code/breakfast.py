from gurobipy import *

#朝食のメニュー最適化

model=Model("breakfast")

x=model.addVar(vtype="C")
y=model.addVar(vtype="C")

model.update()

model.addConstr(3*x+2*y>=9)
model.addConstr(1/15*x+2/15*y>=1/3)
model.addConstr(1/6*x>=1/4)
model.addConstr(x-3*y<=0)
model.addConstr(2*x-y>=0)
model.addConstr(x>=0)
model.addConstr(y>=0)

model.setObjective(-50*x-65*y,GRB.MAXIMIZE)

model.optimize()
print("Opt. Val.=", model.ObjVal)
print("(x,y)=", x.X, y.X)