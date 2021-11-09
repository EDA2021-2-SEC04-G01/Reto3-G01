import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from datetime import datetime
import folium as f
assert cf

#TODO Meta=183 líneas o menos ##

# Construccion de modelos
def newAnalyzer():
    analyzer = {
        'views':lt.newList('SINGLE_LINKED'),
        'timesIndex': (om.newMap(omaptype='BST',comparefunction=compareKeys)),
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

    if nameIndex=='durationsIndex' or nameIndex=='latitudesIndex' or nameIndex=='longitudesIndex': var = float(var)

    if nameIndex =='datesIndex' or nameIndex=='timesIndex':
        var = var[:-3]
        var = datetime.strptime(var,'%Y-%m-%d %H:%M')
        if nameIndex =='datesIndex': var = var.date()
        else:                        var = var.time()
    
    if om.contains(index,var):  lista = om.get(index,var)['value']
    else:                       lista = lt.newList()

    lt.addLast(lista,view)
    om.put(index,var,lista)

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista
def compareDurations(view1,view2):
    return float(view1['duration (seconds)'])>float(view2['duration (seconds)'])

def compareDates(view1,view2):
    date1= datetime.strptime(view1['datetime'],'%Y-%m-%d %H:%M:%S').date()
    date2= datetime.strptime(view2['datetime'],'%Y-%m-%d %H:%M:%S').date()
    return date1<date2

def compareTimes(view1,view2):
    time1= datetime.strptime(view1['datetime'],'%Y-%m-%d %H:%M:%S').time()
    time2= datetime.strptime(view2['datetime'],'%Y-%m-%d %H:%M:%S').time()
    return time1<time2

def compareLocations(view1,view2):
    latitude1 = view1['latitude']
    longitude1 = view1['longitude']
    latitude2 = view2['latitude']
    longitude2 = view2['longitude']

    return longitude1+latitude1>latitude2+longitude2


# Funciones de ordenamiento

def sortbyDates(list):
    sa.sort(list,compareDates)

def sortbyTime(list):
    sa.sort(list,compareTimes)

def sortbyDurations(list):
    sa.sort(list,compareDurations)

def sortLocations(list):
    sa.sort(list,compareLocations)
#+++====================================================================================================================+++
#REQ 1
def viewsPerCity(nombreCiudad,cont):
    index = cont['citiesIndex']
    size = om.size(index)
    height = om.height(index)
    keys = om.keySet(index)
    listTable=[]

    greatnum = 0
    great = None

    for key in lt.iterator(keys):
        size = lt.size(om.get(index,key)['value'])
        if size>greatnum:
            greatnum = size
            great = om.get(index,key)['key']
    
    cityInfo = om.get(index,nombreCiudad)['value']
    sortbyDates(cityInfo)
    return (cityInfo,listTable)

#+++====================================================================================================================+++
#REQ 2,3 y 4
def almostEveryThing(cont,rangeMin,rangeMax,nameIndex, isDate:bool,isTime:bool):
    cantidades = om.newMap('RBT',comparefunction=compareKeys)
    index = cont[nameIndex]
    lista = om.values(index,rangeMin,rangeMax)
    filteredList=lt.newList('ARRAY_LIST')
    variable = 'datetime'

    if isDate:    
            rangeMin = datetime.strptime(rangeMin,'%Y-%m-%d').date()
            rangeMax = datetime.strptime(rangeMax,'%Y-%m-%d').date()

    elif isTime:
            rangeMin = datetime.strptime(rangeMin,'%H:%M').time()
            rangeMax = datetime.strptime(rangeMax,'%H:%M').time()
    
    else: variable = 'duration'

    for list in lt.iterator(lista):
        for value in lt.iterator(list): 
            addToIndex(cantidades,value,nameIndex,variable)
            lt.addLast(filteredList,value)

    
    # Key = om.maxKey(cantidades)
    # returnValue = lt.size(Key)
    Key = None
    returnValue=None
    if isDate:      
                    sortbyDates(filteredList)
                    # Key = om.minKey(cantidades)
                    # returnValue = lt.size(Key)
    elif isTime:    sortbyTime(filteredList)
    else:           sortbyDurations(filteredList)

    total = lt.size(filteredList)

    return (filteredList,Key,returnValue,total)

#+++====================================================================================================================+++
#REQ 5
def searchLocation(cont,latitudeMin,latitudeMax,longMin,longMax):

    filteredList = lt.newList('ARRAY_LIST')
    indexLatitude = cont['latitudesIndex']
    lista1 = om.values(indexLatitude,latitudeMin,latitudeMax)
    
    for list in lt.iterator(lista1):
        for value in lt.iterator(list):
            if float(value['longitude']) >=longMin and float(value['longitude'])<=longMax: lt.addLast(filteredList,value) #Toca así porque range() solo admite int
    sortbyDates(filteredList)
    numElem = lt.size(filteredList)
    return (filteredList,numElem)

#REQ 6
def bono(locations):
    latMin = float(lt.firstElement(locations)['latitude'])
    longMin = float(lt.firstElement(locations)['longitude'])
    latMax = float(lt.lastElement(locations)['latitude'])
    longMax = float(lt.firstElement(locations)['longitude'])
    promLat = (latMin+latMax)/2
    promLong = (longMin+longMax)/2
    
    mapa = f.Map(location=[promLat,promLong],zoom_start=6)
    for view in lt.iterator(locations):
        f.Marker(location=[float(view['latitude']), float(view['longitude'])],popup=view['datetime'],icon=f.Icon(color='red',icon='info-sign')).add_to(mapa)
    mapa.save("Docs\\Mapas\\mapa.html")
