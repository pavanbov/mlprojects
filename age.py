import pandas as pd
from sklearn.svm import SVC
from sklearn.linear_model import LinearRegression
def regression(file,impacts,outcome,inps):
    data = pd.read_csv(file)
    X = data[impacts]
    Y = data[outcome]
    linear_regressor = LinearRegression()
    linear_regressor.fit(X, Y)
    nx = [inps]
    pred = linear_regressor.predict(nx)
    return pred
p = regression("age.csv",['age'],'height',22)
print(p)