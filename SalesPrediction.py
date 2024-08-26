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
    Y = Y.round()
    clf = SVC(kernel='linear')
    clf.fit(X, Y)
    nx = [inps]
    pred = clf.predict(nx)
    return pred
msg=input("""bot:how can i help you:?
you:""")
if "predict" in msg:
    x=input("""bot:do u want to do prediction?
you:""")
    if "yes" in x:
        year = int(input("""bot:could u plz Enter year?
You:"""))
        quarter = int(input("""bot:could you plz Enter quarter?                                         
you:"""))
        types = int(input("""bot:could you plz Enter type value?
you:"""))
        ps = int(input("""bot:could you plz Enter previous sale?
you:"""))
        cost = int(input("""bot:could you plz Enter cost?
you:"""))
        battery = int(input("""bot:could you plz Enter battery? 
you:"""))
        aoos = int(input("""bot:could you plz Enter online availability?
you:"""))
        noo = int(input("""bot:could you plz Enter no. of outlets?
you:"""))
        noc = int(input("""bot:could you plz enter no of competitors?
you:"""))
        y=input("""bot: select an algorithm regression or classification?
you:""")
        if "regression" in y:
            s = reg('SalesPrediction.csv',["year","quarter","types","ps","cost","battery","aoos","noo","noc"],"sales",[year,quarter,types,ps,cost,battery,aoos,noo,noc])
            print("The value of sales: ",float(s[0]))
        if "classification" in y:
             s = reg('SalesPrediction.csv',["year","quarter","types","ps","cost","battery","aoos","noo","noc"],"sales",[year,quarter,types,ps,cost,battery,aoos,noo,noc])
             print("The value of sales: ",float(s[0]))
             s = classify('SalesPrediction.csv',["year","quarter","types","ps","cost","battery","aoos","noo","noc"],"sc",[year,quarter,types,ps,cost,battery,aoos,noo,noc])
             print("classification:",float(s[0]))
    if "no" in x:
          print("bot:thank you have a nice day")
else:
    print("sorry its not available!!")
            
            
            
    
    


