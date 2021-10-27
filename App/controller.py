"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def init():
    """
    Llama la funcion de inicializacion  del modelo.
    """
    # catalog es utilizado para interactuar con el modelo
    analyzer = model.newAnalyzer()
    return analyzer

# Funciones para la carga de datos
def loadData(analyzer, viewsfile):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    viewsfile = cf.data_dir + viewsfile
    input_file = csv.DictReader(open(viewsfile, encoding="utf-8"),
                                delimiter=",")
    for view in input_file:
        model.addToIndex(analyzer, view,'citiesIndex','city')
        model.addToIndex(analyzer, view,'durationsIndex','duration (seconds)')
        model.addToIndex(analyzer, view,'datesIndex','datetime')
        model.addToIndex(analyzer, view,'timeIndex','datetime')
        model.addToIndex(analyzer, view,'latitudesIndex','latitude')
        model.addToIndex(analyzer, view,'longitudesIndex','longitude')
    return analyzer



# Funciones de consulta sobre el catálogo

def requerimiento_1(nombreCiudad,cont):
    rta=model.viewsPerCity(nombreCiudad,cont)
    
    return rta

def requerimiento_2(rangeMin,rangeMax):
    rta=model.viewsPerDuration(rangeMin,rangeMax)
    return rta

def requerimiento_3(rangeMin,rangeMax):
    rta=model.countViewsPerTime(rangeMin,rangeMax) 
    pass
