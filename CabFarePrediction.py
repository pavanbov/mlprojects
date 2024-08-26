import pandas as pd
from sklearn.svm import SVC 
from sklearn.linear_model import LinearRegression
print("bot:hello,please note that hi=0,reg=1,classify=2")
print("you:sure thank you")
print("bot:with pleasure,how can i help you")
msg=input("you:")
distance= float(input("can you provide distance: "))
no_of_passengers = int(input("can i know how many no_of_passengers: "))
time= int(input("at what time do you want ride: "))
vehicle_model = int(input("specify vehicle_model: "))
traffic= int(input("if  traffic: "))
wheather = int(input("rainy  wheather: "))
v_demand = int(input("is there v_demand: "))
no_of_tolls = int(input("can i know no_of_tolls: "))
waiting = int(input(" is there any late: ")) 
if '0' in msg:
        print('hi')
elif '1' in msg:
       def reg(file,impacts,outcome,inps):
              data = pd.read_csv(file)
              X = data[impacts]
              Y = data[outcome]
              linear_regressor = LinearRegression()
              linear_regressor.fit(X, Y)
              nx = [inps]
              pred = linear_regressor.predict(nx)
              return pred
      
       p = reg('cabfareprediction.csv',["distance","no_of_passengers","time","vehicle model","traffic","wheather","v_demand","no_of_tolls","waiting"],"value",[distance,no_of_passengers,time,vehicle_model,traffic,wheather,v_demand,no_of_tolls,waiting])
       print("The % of selecting data1 is: ",float(p[0]))
elif '2' in msg:
     def classify(file,impacts,outcome,inps):
               data = pd.read_csv(file)
               X = data[impacts]
               Y = data[outcome]
               Y = Y.round()
               clf = SVC(kernel='linear') 
               clf.fit(X, Y)
               nx = [inps]
               pred = clf.predict(nx)
               return pred 
    
     p = classify('cabfareprediction.csv',["distance","no_of_passengers","time","vehicle model","traffic","wheather","v_demand","no_of_tolls","waiting"],"value",[distance,no_of_passengers,time,vehicle_model,traffic,wheather,v_demand,no_of_tolls,waiting])
     print("The % of selecting data1 is: ",float(p[0]))  
  



  
   

