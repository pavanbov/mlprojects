from flask import Flask,jsonify, make_response,send_file,request,redirect
from flask_cors import CORS, cross_origin
from fileinput import filename
import os
app = Flask(__name__)
from files import get_files,Linear,Logistic,SV,KM,NB,KNN,RFC,DT
#print(get_files())
@app.route('/')
@cross_origin()
def home():
    return jsonify(get_files())
@app.route('/delete/<name>')
@cross_origin()
def delete(name):
    if os.path.isfile("csvs/"+name+".csv"):
        os.unlink("csvs/"+name+".csv")
    return "deleted"
@app.route('/upload', methods = ['GET','POST'])  
@cross_origin()
def success():  
    if request.method == 'POST': 
        f = request.files['file']
        f.save("csvs/"+f.filename)
        return redirect("http://127.0.0.1:5500",code=302)
@app.route('/images/<name>')
@cross_origin()
def images(name):
    return send_file("images/"+name)
@app.route('/<algo>/<int:id>/<inps>')
@cross_origin()
def algorun(algo,id,inps):
    if algo == "LinearRegression":
        return jsonify(Linear(id,inps))
    elif algo == "LogisticRegression":
        return jsonify(Logistic(id,inps))
    elif algo == "NaiveBayes":
        return jsonify(NB(id,inps))
    elif algo == "SVC":
        return jsonify(SV(id,inps))
    elif algo == "DecisionTree":
        return jsonify(DT(id,inps))
    elif algo == "RandomForest":
        return jsonify(RFC(id,inps))
    elif algo == "KNN":
        return jsonify(KNN(id,inps))
    elif algo == "KMeans":
        return jsonify(KM(id,inps))

if __name__ == '__main__':
    app.run()