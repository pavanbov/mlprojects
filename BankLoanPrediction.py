# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 03:46:38 2020

@author: Srihitha
"""


import pandas as pd
from sklearn.svm import SVC 
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
def classify(file,impacts,outcome,inps):
    data = pd.read_csv(file) 
    X = data[impacts]
    Y = data[outcome]
    Y = Y.round()
    clf = SVC(kernel='linear') 
    clf.fit(X, Y) 
    nx = [inps]
    pred1= clf.predict(nx)
    return pred1
print("Bot: Hiii")
msg0=input("You: ")
print("Bot: How can i help you?")
msg=input("You: ")
#preds=msg.split(" ")
#for pred in preds:
    #if pred in data:
        #print(data[pred])
print("Bot: Can you please choose regression or classification for your bank loan ?")
msg1=input("You: ")
print("Bot: How much amount do you want? : ")        
Loan_amt = int(input("You : "))
print("Bot: What is your cibil score? : ")
cibil_score = int(input("You :"))
print("Bot:  May i know the cibil score of your surity ?: ")
surity_cibil = int(input("You :"))
print("Bot: What is your Annual income?: ")
Annual_income = int(input("You :"))
print("Bot : What is the net worth of your Collateral?: ")
Collateral = int(input("You :"))
print("Bot: If you are a govt employee enter '1' else '0': ")
Employment = int(input("You :"))
print("Bot : Do you have past credits ?if any enter '0' else '1': ")
Past_cred = int(input("You :"))
print("Bot : Do you have any criminal records in the past ?if any enter '0' else '1': ")
hist = int(input("You : "))
if "regression" in msg1:
    p = reg('BankLoanPrediction.csv',["Loan_amt","cibil_score","surity_cibil","Annual_income","Collateral","Employment","Past_cred","hist"],"Outcome",[Loan_amt,cibil_score,surity_cibil,Annual_income,Collateral,Employment,Past_cred,hist])
    print("The regression of your predicted loan is : ",float(p[0]))
if "classification" in msg1:
    p = classify('BankLoanPrediction.csv',["Loan_amt","cibil_score","surity_cibil","Annual_income","Collateral","Employment","Past_cred","hist"],"Output_class",[Loan_amt,cibil_score,surity_cibil,Annual_income,Collateral,Employment,Past_cred,hist])
    print("The classification value of your predicted loan is: ",float(p[0]))