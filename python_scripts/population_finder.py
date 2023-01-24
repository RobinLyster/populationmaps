# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 09:49:32 2020

@author: Robin


Basically you can run this as is, in which case the output will
be every individual colour on the PNG's decimal value followed by the population
inside it, or you can attempt to change the function calculate_population
to do other cool things. It's pretty simple to follow, and there's some unused
code at the bottom you could use.

"""
import xlrd
from matplotlib import image

def load_png():
    """
    loads the world map

    """
    print("Starting...")
    png = image.imread('2.5min_future.png')
    png = 255 * png
    print("Image Loaded")
    return png

def load_sheet():
    """
    loads the population grid

    """
    book = xlrd.open_workbook('2.5min.xlsx')
    print("halfway")
    sheet = book.sheet_by_name('grid')
    print("Spreadsheet Loaded")
    return sheet

def calculate_population():
    """    
    Waaaaa

    """
    colours = []
    populations = []
    list_number = 0
    people = 0
    for x in range(4320):
        for y in range(8640):
            if SHEET.cell_value(x, y) > 0:
                current_colour = (1000000 * PNG[x, y, 0]) + (1000 * PNG[x, y, 1]) + (PNG[x, y, 2])
                try:
                    list_number = colours.index(current_colour)
                except ValueError:
                    colours.append(current_colour)
                    populations.append(0)
                    list_number = len(colours)-1
                else:
                    list_number = colours.index(current_colour)
                populations[list_number] = populations[list_number] + SHEET.cell_value(x, y)
    #            if(PNG[x, y, 0] == 0 and PNG[x, y, 1] == 0 and PNG[x, y, 2] == 0):
                people = people + SHEET.cell_value(x, y)
            if y == 8640 and x%24 == 0:
                print(90-(x/24), round((people/79694445.55), 2), round(people))

    for i in range(len(colours)):
        print(int(round(colours[i])), round(populations[i]))

PNG = load_png()
SHEET = load_sheet()
calculate_population()

