import pandas as pd
from sklearn.svm import SVC
from sklearn.linear_model import LinearRegression
def classify(file,impacts,outcome,inps):
    data = pd.read_csv(file)
    X = data[impacts]
    Y = data[outcome]
    clf=SVC(kernel='linear')
    clf.fit(X,Y)
    nx = [inps]
    pred = clf.predict(nx)
    return pred
p = classify("age.csv",['age','height'],'higher',[20,175])
print(p)