#!/usr/bin/python3
# -*- encoding: utf-8 -*-

# @author     Raúl Caro Pastorino
# @email      dev@fryntiz.es
# @web        https://fryntiz.es
# @gitlab     https://gitlab.com/fryntiz
# @github     https://github.com/fryntiz
# @twitter    https://twitter.com/fryntiz
# @telegram   https://t.me/fryntiz

# Create Date: 2019
# Project Name:
# Description:
#
# Dependencies:
#
# Revision 0.01 - File Created
# Additional Comments:

# @copyright  Copyright © 2019 Raúl Caro Pastorino
# @license    https://wwww.gnu.org/licenses/gpl.txt

# Copyright (C) 2019  Raúl Caro Pastorino
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

# Guía de estilos aplicada: PEP8

#######################################
# #           Descripción           # #
#######################################

#######################################
# #       Importar Librerías        # #
#######################################
import time  # Importamos la libreria time --> time.sleep
import os  # Importamos la libreria para comandos de la consola/shell
import random  # Genera números aleatorios --> random.randrange(1,100)
# import nombre_libreria as nuevo_nombre_libreria
import glob

#######################################
    # #             Variables           # #
#######################################
sleep = time.sleep

## Rutas de salidas
htmlFiles = 'htmlBlade'
pathPublic = 'public'

## Ruta dentro de public para almacenar las rutas de los assets
pathAssets = 'assets'
pathImg = pathAssets + '/img'
pathCss = pathAssets + '/css'
pathJs = pathAssets + '/js'

#######################################
# #             Funciones           # #
#######################################
def buscarArchivos():
    ##
    ## Busca todos los archivos html y los devuelve en un array
    ## Devolverá un array vacío en caso de no encontrar ninguno.
    ##

    files = [f for f in glob.glob("*.html", recursive=False)]

    return files
def convertCss():
    ## Extrae el css del archivo
    pass

def convertJs():
    ## Extrae el Javascript del archivo
    pass

def convertImage():
    ## Extrae las imágene del archivo
    pass

def procesarLinea():
    ## Añade una nueva línea a un archivo
    pass

def procesarArchivo(file):

    pass

def main():
    ## Procesa la lógica archivo a archivo y línea a línea

    files = buscarArchivos()

    if not files:
        print('No hay Archivos')
        exit()

    for file in files:
        procesarArchivo(file)

main()