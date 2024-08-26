import pandas as pd
from sklearn.svm import SVC
def classify(file,impacts,outcome,inps):
    data = pd.read_csv(file)
    X = data[impacts]
    Y = data[outcome]
    clf=SVC(kernel='linear')
    clf.fit(X,Y)
    nx = [inps]
    pred = clf.predict(nx)
    return pred
TEMPERATURE= int(input("Enter temperature: "))
TIME = int(input("Enter time: "))
VOLTAGE = int(input("Enter voltage: "))
p = classify("quality.csv",['temperature','time','voltage'],'quality',[TEMPERATURE,TIME,VOLTAGE])
if int(p[0]) == 0:
    print("Bad quality")
elif int(p[0]) == 1:
    print("Good quality")