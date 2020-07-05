from gurobipy import *

# 多制約0-1ナップサック問題

# 問題のデータを生成する関数
def example():
    # velue
    J,v=multidict({1:7,2:9,3:5,4:5})
    # wight and volume data
    a={(1,1):0,(1,2):0,(1,3):0,(1,4):0,
        (2,1):3,(2,2):6,(2,3):5,(2,4):4,
    }
    # limit
    I,b=multidict({1:0,2:12})
    return I,J,v,a,b

def mkp(I, J, v, a, b):
    model=Model("mkp")
    x={} #変数を辞書に保管
    for j in J:
        x[j]=model.addVar(vtype="B", name="x(%d)"%j)
    model.update()
    for i in I:
        model.addConstr(quicksum(a[i,j]*x[j] for j in J)<= b[i])
    model.setObjective(quicksum(v[j]*x[j] for j in J), GRB.MAXIMIZE)
    model.optimize()
    return model

# メインプログラム
if __name__=="__main__":
    I,J,v,a,b=example()
    model=mkp(I,J,v,a,b)
    model.update()
    model.write("mkp.lp") #作成したモデルのファイルへの書き出し
    model.write("mkp.mps") #作成したモデルのファイルへの書き出し
    print("Optimum value=", model.ObjVal)
    ESP=1.e-6
    for v in model.getVars():
        if v.X>ESP:
            print(v.VarName,v.X)