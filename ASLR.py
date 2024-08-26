import pandas as pd
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt
data = pd.read_csv('AreaSafetyPrediction.csv')
print(data.head())
print(data.describe())
X = data[["area","sex ratio","r cases","crimes","wine shops","men literacy","porn access","psych cases","desserted area","ring roads","slum areas","season","time of visit"]]
Y = data["outcome"]
linear_regressor = LinearRegression()
linear_regressor.fit(X, Y)
test_data = [[1,756,44,175,13,71,4,33,0.2,2,0.1,4,1]]
pred = linear_regressor.predict(test_data)
print(pred[0])
area = X['area'][:1]
plt.scatter(X['area'], Y, color='b')
plt.plot(X['area'][:5], Y[:5],color='black',linewidth=3)
plt.xlabel('Area')  
plt.ylabel('Safety') 
plt.show()