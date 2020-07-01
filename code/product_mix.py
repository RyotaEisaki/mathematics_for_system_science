from gurobipy import *

# 混合物生成問題

a={
    (1,1):.20,(1,2):.15,(1,3):.30,
    (2,1):.30,(2,2):.30,(2,3):.10,
    (3,1):.15,(3,2):.65,(3,3):0,
    (4,1):.10,(4,2):.05,(4,3):.80,
}

I,p=multidict({1:.35*5,2:.30*5,3:.20*8,4:.05*20})
K,LB,UB=multidict({1:[.2,.2],2:[0,0.35],3:[0.45,1]})

model=Model("product mix")
x={}
for i in I:
    x[i]=model.addVar()
model.update()
model.addConstr(quicksum(x[i] for i in I)==1)
for k in K:
    model.addConstr(quicksum(a[i,k]*x[i] for i in I)<=UB[k])
    model.addConstr(quicksum(a[i,k]*x[i] for i in I)>=LB[k])
model.setObjective(quicksum(p[i]*x[i] for i in I), GRB.MINIMIZE)
model.optimize()
for i in I:
    print(i,x[i].X)