import pandas as pd
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt
data = pd.read_csv('prices.csv')
print(data.head())
print(data.describe())
X = data[["Distance"]]
Y = data["Value"]
linear_regressor = LinearRegression()
linear_regressor.fit(X, Y)
pred = linear_regressor.predict([[6.575]])
print("Predicted value: ",pred[0])
plt.scatter(X['Distance'], Y, color='b')
plt.plot(X['Distance'], linear_regressor.predict(X),color='black',linewidth=3)
plt.xlabel('Distance')  
plt.ylabel('Value') 
plt.show()