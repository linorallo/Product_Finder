from flask import Flask
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask import request
import json
try:
    import Product_Finder.backend.db as db
    import Product_Finder.backend.dbScripts
    import Product_Finder.backend.sortResults as sortResults
    import Product_Finder.backend.main as main
    #import Product_Finder.backend.main_standalone as main_standalone
except:
    import db
    import dbScripts
    import sortResults
    import main
    #import main_standalone

app = Flask(__name__)
CORS(app)

@app.route('/')
###@app.route('/search')
def create_app():
    response =[] 
    for result in db.retrieveHomepageDeals() :
        response.append({'name':result[0],'price':result[1], 'discount':result[2],'link': result[3],'img':result[4]})
    # response = db.retrieveHomepageDeals()
    return jsonify({'results':response,}) 
    #return jsonify(response)

@app.route('/search2/<string:searchString>')
def search(searchString):
    print('in specific search')
    searchWords=[]
    blockedWords=[]
    blockedString=searchString
    while True:
        searchWord=searchString.partition('+')
        searchWords.append(searchWord[0].partition('-')[0])
        if '+' not in searchWord[1]:
            break
        searchString = searchWord[2]
    print(searchWords)
    while True:
        blockedStr = blockedString.partition('-')
        if '-' not in blockedStr[1]:
            break
        if blockedStr[1] == '-':
           blockedWords.append((blockedStr[2].partition('+')[0]).partition('-')[0])
        blockedString = blockedStr[2]
    print(blockedWords)
    response=[]
    for result in db.readFromDB(searchWords, blockedWords):
        response.append({'name':result[0],'price':result[1], 'discount':result[2],'link': result[3], 'img': result[4]})
    #results =  sortResults.sortIncreasing(response)
    return jsonify({'results':response}) 

@app.route('/search/<store>/<searchString>', methods=['GET','POST'])
def searchRequest(store,searchString):
    if request.method == 'POST':
        pass
    searchPageDepth =2
    searchWords=[]
    blockedWords=[]
    blockedString=searchString
    while True:
        searchWord=searchString.partition('+')
        searchWords.append(searchWord[0].partition('-')[0])
        if '+' not in searchWord[1]:
            break
        searchString = searchWord[2]
    print(searchWords)
    while True:
        blockedStr = blockedString.partition('-')
        if '-' not in blockedStr[1]:
            break
        if blockedStr[1] == '-':
           blockedWords.append((blockedStr[2].partition('+')[0]).partition('-')[0])
        blockedString = blockedStr[2]
    print(blockedWords)
    searchStr =''
    for word in searchWords :
        searchStr = searchStr + word
    response = [] 
    print(searchStr)
    for result in main.apiSearch(store,searchStr,blockedWords, searchPageDepth) :
        print(result)
        response.append({'name':result[2],'price':result[1], 'discount':result[4],'link': result[3], 'img': result[7]})
    #main_standalone
    return jsonify({'results':response}) 

