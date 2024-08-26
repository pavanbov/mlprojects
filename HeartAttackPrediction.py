# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 22:59:35 2020

@author: Student
"""


import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVC 
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
    Y=Y.round()
    clf = SVC(kernel='linear') 
    clf.fit(X, Y)
    nx = [inps]
    pred = clf.predict(nx)
    return pred
msg1 = input("You: ")
if "hello" in msg1:
    print("Bot:hello")
    print("Bot:how may i help you?")
msg2 = input("You: ")    
if "predict" in msg2:
    print("Bot:what do you want to predict exactly")
msg3 = input("You: ") 
print("Bot:How do you want to predict the data(classification/regression)")
msg = input("You: ")
if "regression" in msg:
    print("Bot:please enter the regression data")
elif "classification" in msg:
    print("Bot:please enter the classification data")
        

Age = int(input("Enter age "))
Sex = int(input("Enter sex "))
Chestpain = int(input("Enter value chest pain: "))
BP = int(input("Enter bp: "))
Cholestrol = int(input("Enter cholestrol: "))
Sugar= int(input("Enter sugar: "))
Heartrate = int(input("Enter heart rate: "))
Inherited = int(input("Enter inherited: "))
Oxygenlevels= int(input("Enter oxygen levels: "))
if "regression" in msg:
    p = reg('heartattack.csv',["Age","Sex","Chestpain","BP","Cholestrol","Sugar","Heartrate","Inherited","Oxygenlevels"],"Outcome",[Age,Sex,Chestpain,BP,Cholestrol,Sugar,Heartrate,Inherited,Oxygenlevels])
    print("The % percentage of heartattack: ",float(p[0])*100)
elif "classification" in msg:
      p = classify('heartattack.csv',["Age","Sex","Chestpain","BP","Cholestrol","Sugar","Heartrate","Inherited","Oxygenlevels"],"Outcome",[Age,Sex,Chestpain,BP,Cholestrol,Sugar,Heartrate,Inherited,Oxygenlevels])
      print("The % percentage of heartattack: ",float(p[0]))
print("Bot:hope u got ur requirement.Any other queries?")