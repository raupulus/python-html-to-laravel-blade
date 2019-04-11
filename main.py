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
import re

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

## Patrones de búsqueda y reemplazo
patron_imagen = 'ZZZZ'
patron_enlace = '.*(<a){1}.*(href="){1}.*("){1}'
patron_css = 'ZZZZ'
patron_js = 'ZZZ'

#######################################
# #             Funciones           # #
#######################################


def convert_css(line):
    ## Extrae el css del archivo

    return line


def convert_js(line):
    ## Extrae el Javascript del archivo
    return line


def convertir_enlace(line):
    # link = re.sub(('(<a){1}.*(href="){1}.*("){1}',  1)
    # link = re.search(r'(?<=(<a)\w{0,n}(href="))\w+(")$', line).group(0)

    link_slice_start = (re.compile('.*<a.*href="')).search(line)
    link_start = link_slice_start.span()[1]

    link_slice_fin = (re.compile('.*<a.*href="[^"]*"')).search(line)
    link_fin = link_slice_fin.span()[1]

    ## Todo → Comprobar que hay líneas obtenidas o meter en tryCatch anteriores

    print(link_slice_fin)

    link = line[link_start:link_fin-1]


    ## Todo → Comprobar link:
    ## Si es http/https no meter en url()
    ##


    ## if ():
    new_link = 'href="url(/' + link + ')"'


    new_line = re.sub('href="[^"]*"', new_link, line)

    print(str(link_start) + ' - ' + str(link_fin))
    print(link)
    print(line)
    print(new_line)

    return new_line


def convert_image(line):
    ## Extrae las imágene del archivo
    return line


def procesar_linea(line):
    ## Procesa cada línea y cambia su valor si es necesario, luego la devuelve

    line_filtered = ''

    if re.search(patron_imagen, line):
        line_filtered = convert_image(line)
    elif re.search(patron_enlace, line):
        line_filtered = convertir_enlace(line)
    elif re.search(patron_css, line):
        line_filtered = line
    else:
        line_filtered = line

    #print(line_filtered)

    return line_filtered


def procesar_archivo(file_name):
    file_opened = open(file_name, 'r')
    lines = file_opened.readlines()

    line_clean = []

    for line in lines:
        line_clean.append(procesar_linea(line))

    ## TODO → Save file
    file_opened.close()


def buscar_archivos():
    ##
    ## Busca todos los archivos html y los devuelve en un array
    ## Devolverá un array vacío en caso de no encontrar ninguno.
    ##

    files = [f for f in glob.glob("*.html", recursive=False)]

    return files


def main():
    ## Procesa la lógica archivo a archivo y línea a línea

    file_names = buscar_archivos()

    if not file_names:
        print('No hay Archivos')
        exit()

    for file_name in file_names:
        procesar_archivo(file_name)


main()
