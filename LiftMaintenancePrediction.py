import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVC
def reg(file,impacts,outcome,inps):
    data = pd.read_csv("LiftMaintainancePrediction.csv")
    X = data[impacts]
    Y = data[outcome]
    linear_regressor = LinearRegression()
    linear_regressor.fit(X, Y)
    nx = [inps]
    pred = linear_regressor.predict(nx)
    return pred
def classify(file,impacts,outcome,inps):
    data = pd.read_csv("LiftMaintainancePrediction.csv")
    X = data[impacts]
    Y = data[outcome]
    clf=SVC(kernel='linear')
    clf.fit(X,Y)
    nx = [inps]
    pred = clf.predict(nx)
    return pred
msg=input(" you: ")
if "predict" in msg:
    print("What do you want to predict?")
    print('1.regression\n 2.classify')
    b=int(input('enter your choice'))   
    if b==1:    
        TEMPERATURE= int(input("Enter temperature: "))
        CAPACITY = int(input("Enter capacity: "))
        SPEED = int(input("Enter speed: "))
        DOOR_OPENING_TIME = int(input("Enter door opening time: "))
        p = float(input("Enter p: "))
        q = int(input("Enter q: "))
        r=float(input("enter r: "))
        p = reg('db.csv',["TEMPERATURE","CAPACITY","SPEED","DOOR_OPENING_TIME","p","q","r"],"OUTCOMES",[TEMPERATURE,CAPACITY,SPEED,DOOR_OPENING_TIME,p,q,r])
        print("Lift maintainance is: ",float(p[0])) 
    elif b==2:   
        TEMPERATURE= int(input("Enter temperature: "))
        CAPACITY = int(input("Enter capacity: "))
        SPEED = int(input("Enter speed: "))
        DOOR_OPENING_TIME = int(input("Enter door opening time: "))
        p = float(input("Enter p: "))
        q = int(input("Enter q: "))
        r=float(input("enter r: "))
        p = classify('db.csv',["TEMPERATURE","CAPACITY","SPEED","DOOR_OPENING_TIME","p","q","r"],"CLASS",[TEMPERATURE,CAPACITY,SPEED,DOOR_OPENING_TIME,p,q,r])
        print("Lift maintainance is: ",float(p[0])*100)
        if int(p[0]) == 0:
            print("Lift doesn't needs maintenance")
        elif int(p[0]) == 1:
            print("Lift needs maintenance")