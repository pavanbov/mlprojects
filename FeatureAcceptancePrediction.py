import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVC

def reg(file,impacts,outcome,inps):
    data = pd.read_csv(file)
    X = data[impacts]
    Y = data[outcome]
    linear_regressor = LinearRegression()
    linear_regressor.fit(X, Y)
    nx = [inps]
    pred = linear_regressor.predict(nx)
    return pred
def classify(file,impacts,outcome,inps):
    data = pd.read_csv(file)
    X = data[impacts]
    Y = data[outcome]
    clf = SVC(kernel='linear')
    clf.fit(X, Y)
    nx = [inps]
    pred = clf.predict(nx)
    return pred
msg = input("Give a parameter: ")
print("Do you want to know regression")
print("how much height do you want?")
height = float(input("i want my device height to be: "))
print("how much width do you want?")
width = float(input(" width should be: "))
print("how much Ram do you want?")
RAM = float(input("Ram should be: "))
print("how much internal storage  do you want?")
Internal = float(input("Internal storage of: "))
print("what is the capacity of battery ?")
battery = float(input(" battery capacity of: "))
print("do you want ur tablet to be light weight")
weight = float(input("yeah! appox. weight should be "))
print("how much budget do u spend to buy tablet?")
cost = float(input("cost is "))
print("which brand do you prefer?")
Brand = float(input("the available brands are "))
print("what about camera quality?")
Bpixel = float(input("the best quality is: "))
print("then what about front camera?") 
Fpixel = float(input("preferable quality is: "))
if "regression" in msg:
      p = reg('featureacceptanceprediction.csv',["height","width","RAM","Internal","battery","weight","cost","Brand","Bpixel","Fpixel"],"Accept",[height,width,RAM,Internal,battery,weight,cost,Brand,Bpixel,Fpixel])
      print("The % of selecting mobile is: ",float(p[0])*100)
if "classify" in msg:
       p = classify('featureacceptanceprediction.csv',["height","width","RAM","Internal","battery","weight","cost","Brand","Bpixel","Fpixel"],"outcome",[height,width,RAM,Internal,battery,weight,cost,Brand,Bpixel,Fpixel])
       print("The % of selecting mobile is: ",float(p[0])*100)


