import glob
import pandas as pd
import os
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.cluster import KMeans
def get_files(): 
    path = "csvs"
    files = glob.glob(path + "/*.csv")
    files_n = []
    for file in files:
        files_n.append(file.replace("csvs\\","").replace(".csv",""))
    return files_n
def get_data(id,type):
    files = get_files()
    url = "csvs/"+files[id]+".csv"
    df = pd.read_csv(url)
    columns = df.columns
    features = columns[:-2]
    X = df[features]
    if type == 1:
        outcome = columns[-2]
    elif type == 2:
        outcome = columns[-1]
    Y = df[outcome]
    return [X,Y]
def draw(X,Y,id):
    file = get_files()[id]
    plt.scatter(X.iloc[:,0], Y, color='b')
    plt.xlabel('Feature')  
    plt.ylabel('Outcome')
    if os.path.isfile("images/"+file+".png"):
        os.unlink("images/"+file+".png")
    plt.savefig("images/"+file+".png")
def drawMap(id):
    file = get_files()[id]
    url = "csvs/"+file+".csv"
    data = pd.read_csv(url)
    plt.imshow( data , cmap = 'coolwarm' , interpolation = 'nearest' )
    plt.title( file )
    if os.path.isfile("images/"+file+" Heatmap.png"):
        os.unlink("images/"+file+" Heatmap.png")
    plt.savefig("images/"+file+" Heatmap.png")
def Linear(id,inps):
    [X,Y] = get_data(id,1)
    mdl = LinearRegression()
    mdl.fit(X, Y)
    pred = mdl.predict([inps.split(',')])
    score = mdl.score(X[:10], Y[:10])*100
    draw(X,Y,id)
    return {"pred":pred[0],"score":score}
def Logistic(id,inps):
    [X,Y] = get_data(id,2)
    mdl = LogisticRegression()
    mdl.fit(X, Y)
    pred = mdl.predict([inps.split(',')])
    score = mdl.score(X[:10], Y[:10])*100
    draw(X,Y,id)
    return {"pred":str(pred[0]),"score":str(score)}
def SV(id,inps):
    [X,Y] = get_data(id,2)
    mdl = SVC(kernel='poly')
    mdl.fit(X, Y)
    pred = mdl.predict([inps.split(',')])
    score = mdl.score(X[:10], Y[:10])*100
    draw(X,Y,id)
    return {"pred":str(pred[0]),"score":str(score)}
def KM(id,inps):
    [X,Y] = get_data(id,2)
    k = 2
    mdl = KMeans(n_clusters=k)
    mdl.fit(X, Y)
    centroids = mdl.cluster_centers_
    pred = mdl.predict([inps.split(',')])
    score = mdl.score(X[:10], Y[:10])*100
    draw(X,Y,id)
    return {"pred":str(pred[0]),"score":str(score)}
def NB(id,inps):
    [X,Y] = get_data(id,2)
    mdl = GaussianNB()
    mdl.fit(X, Y)
    pred = mdl.predict([inps.split(',')])
    draw(X,Y,id)
    score = mdl.score(X[:10], Y[:10])*100
    return {"pred":str(pred[0]),"score":str(score)}
def KNN(id,inps):
    [X,Y] = get_data(id,2)
    mdl = KNeighborsClassifier()
    mdl.fit(X, Y)
    pred = mdl.predict([inps.split(',')])
    score = mdl.score(X[:10], Y[:10])*100
    draw(X,Y,id)
    return {"pred":str(pred[0]),"score":str(score)}
def RFC(id,inps):
    [X,Y] = get_data(id,2)
    mdl = RandomForestClassifier(criterion='entropy')
    mdl.fit(X, Y)
    pred = mdl.predict([inps.split(',')])
    score = mdl.score(X[:10], Y[:10])*100
    draw(X,Y,id)
    return {"pred":str(pred[0]),"score":str(score)}
def DT(id,inps):
    [X,Y] = get_data(id,2)
    mdl = DecisionTreeClassifier(max_leaf_nodes=3, random_state=1)
    mdl.fit(X, Y)
    pred = mdl.predict([inps.split(',')])
    score = mdl.score(X[:10], Y[:10])*100
    draw(X,Y,id)
    return {"pred":str(pred[0]),"score":str(score)}