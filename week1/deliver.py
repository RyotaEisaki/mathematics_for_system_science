from gurobipy import *

# 輸送問題

# demand
I,d=multidict({1:25, 2:10, 3:20, 4:30, 5:15})

# capacity
J,M=multidict({1:40,2:20,3:40})

c={(1,1):40, (1,2):95, (1,3):100,
    (2,1):10, (2,2):50, (2,3):75,
    (3,1):35, (3,2):20, (3,3):40,
    (4,1):50, (4,2):35, (4,3):15,
    (5,1):65, (5,2):40, (5,3):20,
    }



model=Model('transportation')
x={}
for i in I:
    for j in J:
        x[i,j]=model.addVar(vtype="C", name="x(%s,%s)"%(i,j))
model.update()

for i in I:
    model.addConstr(quicksum(x[i,j] for j in J)==d[i],name='Demand(%s)'%i)
for j in J:
    model.addConstr(quicksum(x[i,j] for i in I)<=M[j],name="Capacity(%s)"%j)

model.setObjective(quicksum(c[i,j]*x[i,j] for (i,j) in x), GRB.MINIMIZE)

model.optimize()
print("Optimal value: ", model.objVal)
EPS=1.e-6
for (i,j) in x:
    if x[i,j].X >EPS:
        print("sending quantity %10s from factory %3s to customer %3s"%(x[i,j].X,j,i))