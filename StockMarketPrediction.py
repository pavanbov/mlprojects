import pandas as pd
from sklearn.svm import SVC
from sklearn.svm import SVR
def reg(file,impacts,outcome,inps):
    data = pd.read_csv(file)
    X = data[impacts]
    Y = data[outcome]
    lr = SVR(kernel='poly')
    lr.fit(X,Y)
    nx = [inps]
    pred = lr.predict(nx)
    return pred
def classify(file,impacts,outcome,inps):
    data = pd.read_csv(file)
    X = data[impacts]
    Y = data[outcome]
    clf = SVC(kernel='poly')
    clf.fit(X,Y)
    nx = [inps]
    pred = clf.predict(nx)
    return pred
LTP=float(input("Enter LTP: "))
change=float(input("Enter CHANGE: "))
tradedqty =float(input("Enter TRADEDQTY: "))
value =float(input("Enter VALUE: "))
openx = float(input("Enter OPENX: "))
high = float(input("Enter HIGH: "))
low = float(input("Enter LOW: "))
prevclose= float(input("Enter PREVCLOSE: "))
weight= float(input("Enter WEIGHT: "))
ch = int(input("What do you want to perform?\n1. Regression\n2. Classification\nEnter your choice: "))
if ch == 1:
   p = reg('StockMarketPrediction.csv',["LTP","change","tradedqty","value","openx","high","low","prevclose","weight"],"outcome",[LTP,change,tradedqty,value,openx,high,low,prevclose,weight])
   print("The % of investment  is: ",float(p[0])*100)
elif ch == 2:
    p = classify('StockMarketPrediction.csv',["LTP","change","tradedqty","value","openx","high","low","prevclose","weight"],"outcome",[LTP,change,tradedqty,value,openx,high,low,prevclose,weight])
    if int(p[0]) == 0:
        print("Do not invest")
    elif int(p[0]) == 1:
        print("Do invest")







