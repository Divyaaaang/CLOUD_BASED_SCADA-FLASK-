from flask import Flask, jsonify, request, render_template, redirect, url_for, session
import pymongo
from pymongo import MongoClient
import json
from bson import json_util
import requests

if __name__=="__main__":
    #setting up connection with my web application using the below connecting string
    cluster1 = pymongo.MongoClient("mongodb+srv://python:python@cluster1.zptukby.mongodb.net/?retryWrites=true&w=majority",serverSelectionTimeoutMS=60000)
    print("CONGRATULATIONS DIVYANG!!!! DATA HAS BEEN DUMPED")
    db1 = cluster1["labview"]
    collection1 =db1["python"]


    cluster2 = pymongo.MongoClient("mongodb+srv://python:python@cluster1.zptukby.mongodb.net/?retryWrites=true&w=majority",serverSelectionTimeoutMS=60000)
    print("NEWWWW")
    db2 = cluster2["Alarm"]
    collection2 =db2["labview"]






    #initializing my flask ap
    app = Flask(__name__,static_folder='static',template_folder='templates')
    #code below defines a route for a Flask web application that responds to HTTP GET requests to the "/new" URL.
    @app.route('/')
    def index():
        return render_template('login.html')
        
    
 #----------------------LOGIN PASSWORD PAGE OF DASHBOARD-----------------------------------------------   
@app.route('/dashboard', methods=['POST'])
def dashboard():
    username = request.form['username']
    password = request.form['password']
    
    # Check if the username and password are valid
    if username == 'divyang' and password == "":
        return redirect(url_for('main_dashboard'))
    else:
        return render_template('login.html', error=True)    
    
    

@app.route("/dash",methods=["GET"])
def main_dashboard():
     new_para2 = list(collection1.find({}))     
     return render_template('dashboard.html', data=new_para2)


@app.route("/API",methods=["GET"])
def get_names():
        new_para= list(collection1.find({}))
        return jsonify(new_para)

#------------------MAIN-CHARTS------------------------
@app.route("/data")
def get_data():
    # Make HTTP request to Flask API to fetch sales data
    response = requests.get("http://localhost:5000/API")
    data = response.json()

    # Create new dictionary with only data for Jan, Feb, and March
    subset = {}
    for item in data:
        if item['Input'].lower().strip() in ['inlet-temperature', 'bed-temperature', 'exhaust-temperature']:
            subset[item['Input']] = int(item['Reading'])

    # Create donut chart data
    chart_data = {
        "labels": list(subset.keys()),
        "datasets": [
            {
                "data": list(subset.values()),
                
            }]
    }

    return jsonify(chart_data)

@app.route('/dash')
def charts():
    return render_template('dashboard.html')

#-------------------graphs & analytics-------------------------
@app.route('/analytics')
def analytics():
        return render_template('TotalGraphs.html')


#------------------ALARM--------------------------------------
@app.route("/a",methods=["GET"])
def get_alarm():
        new_para= list(collection2.find({}))
        return jsonify(new_para)


@app.route('/bar')
def bar():
        return render_template('alarm.html')
@app.route('/line')
def line():
        return render_template('line.html')



#------------------------ABOUT-------------------
@app.route('/about')
def about():
        return render_template('about.html')

@app.route('/Plant')
def plant():
        return render_template('Plant.html')


 

if __name__=='__main__':
        app.run(host='0.0.0.0', debug=True)