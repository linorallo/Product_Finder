import operator
def sortIncreasing(results):
    print(operator.itemgetter(1))
    results.sort(key = operator.itemgetter(1))
    return results
def sortDecreasing(results):
    results.sort(key = operator.itemgetter(1), reverse = True)
    return results
def sortIncreasingDiscoount(results):
    results.sort(key = operator.itemgetter(1))
    return results