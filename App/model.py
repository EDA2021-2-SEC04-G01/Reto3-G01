import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from datetime import datetime

assert cf

#TODO Meta=183 líneas o menos ##

# Construccion de modelos
def newAnalyzer():
    analyzer = {
        'views':lt.newList('SINGLE_LINKED'),
        'timeIndex': (om.newMap(omaptype='BST',comparefunction=compareKeys)),
        'citiesIndex':om.newMap(omaptype='RBT'),
        'durationsIndex':(om.newMap(omaptype='RBT',comparefunction=compareKeys)),
        'datesIndex':om.newMap(omaptype='RBT',comparefunction=compareKeys),
        'latitudesIndex':om.newMap(omaptype='RBT',comparefunction=compareKeys),
        'longitudesIndex':om.newMap(omaptype='RBT',comparefunction=compareKeys)
    }
    return analyzer

def compareKeys(key1,key2):
    if key1==key2 :   return  0
    elif key1>key2:   return  1
    elif key1<key2:   return -1

# Funciones para agregar informacion al catalogo

def addToIndex(analyzer,view,nameIndex:str,variable:str):

    index = analyzer[nameIndex]
    var = view[variable]
    if nameIndex =='datesIndex' or nameIndex=='timeIndex':

        var = datetime.strptime(var,'%Y-%m-%d %H:%M:%S')
        if nameIndex =='datesIndex': var = var.date()
        else:                        var = var.time()
    
    if om.contains(index,var):  lista = om.get(index,var)['value']
    else:                       lista = lt.newList()

    lt.addLast(lista,view)
    om.put(index,var,lista)

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento

#REQ 1

def viewsPerCity(nombreCiudad,cont):
    index = cont['citiesIndex']
    size = om.size(index)
    height = om.height(index)
    return (size,height)
#REQ 2

def viewsPerDuration(rangeMin,rangeMax):
    pass

#REQ 3
def countViewsPerTime(rangeMin,rangeMax):
    pass