import threading
from threading import *
try:
    import Product_Finder.backend.amazon_v2 as amazon_v2
    import Product_Finder.backend.newegg_scrapper as newegg_scrapper
    import Product_Finder.backend.mercadolibre_scrapper as mercadolibre_scrapper
    import Product_Finder.backend.sortResults as sortResults
    import Product_Finder.backend.db as db
except:
    import amazon_v2
    import newegg_scrapper
    import mercadolibre_scrapper
    import sortResults
    import db
import queue
import datetime
class searchAmazon(Thread):
    def __init__(self, threadID, name, counter, *args):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.args = args
    def run(self) :
        print('Amazon thread initiated...')
        resultQueue = self.args[0][0]
        searchParameters = self.args[0][1]
        resultQueue.put(amazon_v2.searchInAmazon(searchParameters[0],searchParameters[1],searchParameters[2],searchParameters[3],searchParameters[4], ))

class searchNewegg(Thread):
    def __init__(self, threadID, name, counter, *args):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.args = args
    def run(self) :
        print('Newegg thread initiated...')
        resultQueue = self.args[0][0]
        searchParameters = self.args[0][1]
        resultQueue.put(newegg_scrapper.searchInNewegg(searchParameters[0],searchParameters[1],searchParameters[2],searchParameters[3],searchParameters[4], ))
class searchMercadoLibre(Thread):
    def __init__(self, threadID, name, counter, *args):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.args = args
    def run(self) :
        print('Mercado_libre thread initiated...')
        resultQueue = self.args[0][0]
        searchParameters = self.args[0][1]
        resultQueue.put(mercadolibre_scrapper.searchInMercadoLibre(searchParameters[0],searchParameters[1],searchParameters[2],searchParameters[3],searchParameters[4], ))
searchList = []
blockWords = []
def apiSearch(searchStr, blockedWords, searchPageDepth):
    sortPreference = 'Increasing'
    currency = 'USD'
    #for result in db.readFromDB(searchStr, blockedWords):
    choiceAmazon=choiceNewegg=choiceML=''
    results = []
    searchParameters=[searchStr,blockedWords,searchPageDepth, sortPreference,currency]
    outputQ = queue.Queue()
    amazonThread = searchAmazon(1,'amazonThread',1,([outputQ,searchParameters]))
    amazonThread.start()
    neweggThread = searchNewegg(1,'neweggThread',1,([outputQ,searchParameters]))
    neweggThread.start()
    mercadolibreThread = searchMercadoLibre(1,'mercadolibreThread',1,([outputQ,searchParameters]))
    mercadolibreThread.start()
    mercadolibreThreadStatus=''
    while True:
        if amazonThread.is_alive() == False :
            amazonThreadStatus = False
        else:
            amazonThreadStatus = True
        if neweggThread.is_alive() == False :
            neweggThreadStatus = False
        else:
            neweggThreadStatus =  True
        if mercadolibreThread.is_alive() == False :
            mercadolibreThreadStatus = False
        else:
            mercadolibreThreadStatus = True
        if amazonThreadStatus == False :
            if neweggThreadStatus == False :
                if mercadolibreThreadStatus == False:
                    break
    print('All threads closed')
    results = []
    queue_length = outputQ.qsize()
    for x in range(queue_length):
        results = results + outputQ.get()
    print('result"s lengt: ' + str(len(results)))
    #results = sortResults.sortIncreasing(results)
    db.saveToDB(results)     
    return results



