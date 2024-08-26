import pandas as pd
from sklearn.linear_model import LinearRegression
def reg(file,impacts,outcome,inps):
    data = pd.read_csv(file)
    X = data[impacts]
    Y = data[outcome]
    linear_regressor = LinearRegression()
    linear_regressor.fit(X, Y)
    nx = [inps]
    pred = linear_regressor.predict(nx)
    return pred
FANS = float(input("Enter fan: "))
LIGHTS = float(input("Enter light: "))
ACs = float(input("Enter AC: "))
COMPUTERS = float(input("Enter computer: "))
VEHICLES = float(input("Enter vehicle: ")) 
p = reg('PlantationPrediction.csv',["FANS","LIGHTS","ACs","COMPUTERS","VEHICLES"],"PLANTS",[FANS,LIGHTS,ACs,COMPUTERS,VEHICLES])
print("The number of plants needed  are: ",float(p[0]))