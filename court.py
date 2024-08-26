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
no=float(input("Enter No: "))
typ=float(input("Enter Type: "))
count =float(input("Enter Count: "))
ch = int(input("What do you want to perform?\n1. Regression\n2. Classification\nEnter your choice: "))
if ch == 1:
   p = reg('court.csv',["court_no","case_type","case_count"],"can_give",[no,typ,count])
   print("The % of assignment  is: ",float(p[0])*100)
elif ch == 2:
    p = classify('court.csv',["court_no","case_type","case_count"],"can_give",[no,typ,count])
    if int(p[0]) == 0:
        print("Do not assign")
    elif int(p[0]) == 1:
        print("Do assign")







