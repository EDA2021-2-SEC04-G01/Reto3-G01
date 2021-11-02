from DISClib.ADT import list as lt
from tabulate import tabulate
import textwrap
#CREACIÓN DE TABLAS
def distribuir(elemento,cantidad):
    str_distribuido = '\n'.join((textwrap.wrap(elemento,cantidad)))
    return str_distribuido

def chkUnknown(origen,clave):
    if origen[clave]==None or origen[clave]=='' or origen[clave]==5000 or origen[clave]=='2100-12-24': return 'Unknown' #El 5000 se pone para compensar una de las funciones de comparación de años.
    else: return origen[clave]
def selectInfo(position,ListArtworks,FilteredList):
#       ↓↓↓ Todo este montón de líneas se encargan de sacar la info. necesaria del diccionario grande y con textwrap lo separa en líneas de un igual tamaño.
        artwork = lt.getElement(ListArtworks,position)

        datetime = artwork['datetime']
        city=distribuir(chkUnknown(artwork,'city'),20)
        state=distribuir(chkUnknown(artwork,'state'),10)
        country=distribuir(chkUnknown(artwork,'country'),20)
        shape=distribuir(chkUnknown(artwork,'shape'),20)
        duration_seconds=distribuir(chkUnknown(artwork,'duration (seconds)'),15)

#       Se crea una lista con todo lo que pide el requerimiento.

        artwork_entrega = [datetime,city,state,country,shape,duration_seconds]

#       Se pone un nuevo registro con la info de cada obra en la lista grande declarada al inicio.
        FilteredList.append(artwork_entrega)

def createTable(filteredList,listTable):
    for position in range(1,4):
        selectInfo(position,filteredList,listTable)
    for position in range(lt.size(filteredList)-2,lt.size(filteredList)+1):
        selectInfo(position,filteredList,listTable)

    headers = ['datetime','city','state','country','shape','duration (seconds)']

    table = tabulate(listTable,headers=headers,numalign='right',tablefmt='grid') 
    return table
#↑↑↑ Termina el formatting de las tablas ↑↑↑