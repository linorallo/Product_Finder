def deleteDuplicates() :
    return 'DELETE FROM product    WHERE idproduct NOT IN      (  SELECT MAX(idproduct)    GROUP BY productLink  )'

def retrieveAll():
    return 'SELECT productLink, productPrice FROM  product'

def updatePriceProduct(linkProduct, newPrice):
    return 'UPDATE product SET productPrice = ' + newPrice + ' WHERE productLink  = "' + linkProduct + '";'

def searchProducts(searchList, blockedWords) :
    query = 'SELECT productName, productPrice, productDiscount, productLink, productImg, productDiscoverDate FROM product WHERE '
    iterationNumber=0
    for searchWord in searchList :
        if iterationNumber == 0 :
            query = query + ' productName LIKE "%' + searchWord + '%" '
            iterationNumber += 1
        else:
            query = query + 'AND productName LIKE "%' + searchWord + '%" '
    for blockedWord in blockedWords :
        query = query + 'AND productName NOT LIKE "%' + blockedWord + '%" ' 
    return query + ' ;'

def discountSearch():
    return 'SELECT productName, productPrice, productDiscount, productLink, productImg FROM product WHERE productDiscount >=20'