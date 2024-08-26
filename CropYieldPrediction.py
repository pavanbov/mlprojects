# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 23:35:11 2020

@author: admin
"""

import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.svm import SVC

print('hi,how may i help you?')


        

def reg(file,impacts,outcome,inps):
    data = pd.read_csv(file)
    X = data[impacts]
    Y = data[outcome]
    linear_regressor = LinearRegression()
    linear_regressor.fit(X, Y)
    nx = [inps]
    pred = linear_regressor.predict(nx)
    return pred


def classify(file,impacts,outcome,inps):
    data = pd.read_csv(file)
    X = data[impacts]
    Y = data[outcome]
    clf = SVC(kernel='linear')
    clf.fit(X, Y)
    nx = [inps]
    pred = clf.predict(nx)
    return pred

msg=input('you:')
if 'predict' in msg:
    a=print('choose regresssion or classification:')
    msg=input('you:')
    Area = int(input("In how much Area you want to predict: ")) 
    Moisture = float(input("Moisture levels of the area(between 12.0 to 14.0): "))
    rainfall = float(input("rainfall received  in meters: "))
    Maxtemp = int(input(" Maxtemp in your area: "))
    Mintemp = int(input(" Mintemp in your area: "))
    Humidity = int(input("what is Humidity present(in %) : "))
    Soiltype = int(input("what is your field area Soiltype(1-clay,2-black soil,3-red soil,4-sandy soil): "))
    Fertilizers = int(input("Fertilizers  used in field(in %): "))
    pests = int(input("Are pests present in your field(yes-1,No-0) : "))
    pathogens = int(input("Are pathogens in your field(yes-1,No-0): "))
    if "regression" in msg:
        r = reg('CropYieldPrediction.csv',["Area","Moisture","rainfall","Maxtemp","Mintemp","Humidity","Soiltype","Fertilizers","pests","pathogens"],"Outcomes",[Area,Moisture,rainfall,Maxtemp,Mintemp,Humidity,Soiltype,Fertilizers,pests,pathogens])
        print("The value of crop yielding is: ",float(r[0]))
    elif "classification" in msg:
        q = classify('CropYieldPrediction.csv',["Area","Moisture","rainfall","Maxtemp","Mintemp","Humidity","Soiltype","Fertilizers","pests","pathogens"],"OUTCOME",[Area,Moisture,rainfall,Maxtemp,Mintemp,Humidity,Soiltype,Fertilizers,pests,pathogens])
        print("The class of crop yielding is: ",float(q[0]))
else:
    print('Sorry! I cannot understand!')



    
#p = predict('CropYieldPrediction.csv',["Area","Moisture","rainfall","Maxtemp","Mintemp","Humidity","Soiltype","Fertilizers","pests","pathogens"],"Outcomes",[Area,Moisture,rainfall,Maxtemp,Mintemp,Humidity,Soiltype,Fertilizers,pests,pathogens])







