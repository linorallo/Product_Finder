from flask import Flask
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import json
import Product_Finder.backend.amazon_v2
from Product_Finder.backend import *
#import templates.views
import Product_Finder.backend.db as db
import Product_Finder.backend.dbScripts
import Product_Finder.backend.sortResults as sortResults

app = Flask(__name__)
CORS(app)
@app.route('/')
def create_app():
    response =[] 
    for result in db.retrieveHomepageDeals() :
        response.append({'name':result[0],'price':result[1], 'discount':result[2],'link': result[3]})
    # response = db.retrieveHomepageDeals()
    return jsonify({'results':response,}) 
    #return jsonify(response)
@app.route('/search/<string:searchString>')
def search(searchString):
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
    results=[]
    for result in db.readFromDB(searchWords, blockedWords):
        results.append({'name':result[0],'price':result[1], 'discount':result[2],'link': result[3]})
    #results =  sortResults.sortIncreasingDiscoount(results)
    return jsonify({'results':results}) 

