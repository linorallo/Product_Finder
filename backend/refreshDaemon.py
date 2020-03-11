import Product_Finder.backend.db as db
import Product_Finder.backend.dbScripts as dbScripts
from datetime import timedelta, datetime

def checkProductUpdates():
    actualTime = datetime.now()
    timeDelta= timedelta(hours=5)
    timeLimit= actualTime-timeDelta
    dateFormat = '%Y-%m-%d %H:%M:%S'
    for item in dbScripts.retrieveAll() :
        discoveredTime = datetime.strptime(item[5],dateFormat)
        if discoveredTime - timeLimit :
            if 
