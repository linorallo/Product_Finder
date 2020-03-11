import bs4
try:
    import Product_Finder.backend.sortResults as sortResults
except:
    import sortResults
import datetime as date
from urllib.request import urlopen as urlReq
from bs4 import BeautifulSoup as soup 
neweggDBPK = 1
def searchInNewegg(searchString, blockedWord, searchPageDepth, sortPreference, currency):
    searchString = searchString.replace(' ','+')
    results=[]
    currentPage = 1
    datetime = date.datetime.now()
    while currentPage <= searchPageDepth : 
        if currentPage != 0 :
            if currentPage <= (searchPageDepth + 1) : 
                urlSite = "https://www.newegg.com/p/pl?d=" + searchString + "&Page=" + str(currentPage)
                webSite = urlReq(urlSite)
                html = webSite.read()
                webSite.close()
                page_soup = soup(html, 'html.parser')
        itemsWholeGrid = page_soup.find('div',{'class':'items-view is-grid'})
        try:
            itemsWhole = itemsWholeGrid.findAll('div',{'class':'item-container'})
        except AttributeError as err:
            print(err)
            break
        for item in itemsWhole:
            def itemAnalysis():
                #print('--------------------------------')
                text = item.find('div',{'class':'item-info'})
                name=str(text.find('a',{'class':'item-title'}).text)
                price = str(text.find('li',{'class':'price-current'}))[78:85].strip('</strong>').replace(',','')
                try:
                    discount = str(text.find('span',{'class':'price-save-percent'}).text).strip('%')
                except:
                    #print('discount not found')
                    discount = 0
                    if discount == 'None' :
                        discount = 0
                if discount=='':
                    discount=0
                itemNumber = str(len(results)+1)
                link = str(text.find('a',{'class':'item-title'})['href']).partition('?')[0].strip('https://')
                try:
                    img = item.find('img',{})['data-src']
                except:
                    img= item.find('img',{})['src']
                results.append((str(itemNumber), str(price), name, link, str(discount), str(datetime) ,str(neweggDBPK),img))
                
                #print("item #"+ itemNumber +": "+ name +" $"+ price + ' OFF: '+ discount )
            bWordFound = 0
            for bWord in blockedWord:
                if bWord in str(item):  
                    bWordFound+=1
            if bWordFound == 0 :
                itemAnalysis()
        currentPage=currentPage+1
    print('results in NewEgg :' + str(len(results)))
    if sortPreference == 'Increasing' :
        return sortResults.sortIncreasing(results)
    if sortPreference == 'Decreasing' :
        return sortResults.sortDecreasing(results)

        