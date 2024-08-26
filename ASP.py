import pandas as pd
from sklearn.linear_model import LinearRegression
data = pd.read_csv("Area Safety Prediction.csv")
X = data[["area","sex ratio","r cases","crimes","wine shops","men literacy","porn access","psych cases","desserted area","ring roads","slum areas","season","time of visit"]]
Y = data["outcome"]
linear_regressor = LinearRegression()
linear_regressor.fit(X, Y)
pred = linear_regressor.predict([[1,756,44,175,13,71,4,33,0.2,2,0.1,4,1],[2,850,77,162,10,72,5,45,0.2,4,0.3,2,2]])
print(pred)
from sklearn.svm import SVC
Y = data['class']
clf = SVC(kernel='linear') 
clf.fit(X, Y)
pred = clf.predict([[1,756,44,175,13,71,4,33,0.2,2,0.1,4,1],[2,850,77,162,10,72,5,45,0.2,4,0.3,2,2]])
print(pred)