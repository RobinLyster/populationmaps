"""
Created on Wed Oct 28 09:49:32 2020

@author: Robin

OI JACK

Basically you can run this as is, in which case the output will
be every individual colour on the PNG's decimal value followed by the population
inside it, or you can attempt to change the function calculate_population
to do other cool things. It's pretty simple to follow, and there's some unused
code at the bottom you could use.

"""
import pandas
import xlrd
from matplotlib import image

def load_png():
    """
    loads the world map

    """
    print("Starting...")
    png = image.imread('15min.png')
    png = 255 * png
    print("Image Loaded")
    return png

def load_text():
    """
    loads the population grid

    """
    f = open('15min.asc', 'r')
    data = f.read()
    array=[]
    for line in data:
        if 'E' in line:
            e = line.replace('E','*10**')
            array.append(e)
        try:
            array.append(float(line))
        except:
            continue
    return array

def calculate_population():
    """    
    Waaaaa

    """
    colours = []
    populations = []
    list_number = 0
    people = 0
    for x in range(720):
        for y in range(1440):
            if float(array[(720*x)+y]) > 0:
                current_colour = (1000000 * PNG[x, y, 0]) + (1000 * PNG[x, y, 1]) + (PNG[x, y, 2])
                try:
                    list_number = colours.index(current_colour)
                except ValueError:
                    colours.append(current_colour)
                    populations.append(0)
                    list_number = len(colours)-1
                else:
                    list_number = colours.index(current_colour)
                populations[list_number] = populations[list_number] + float(array[(720*x)+y])
    #            if(PNG[x, y, 0] == 0 and PNG[x, y, 1] == 0 and PNG[x, y, 2] == 0):
                people = people + float(array[(720*x)+y])
            if y == 1339 and x%24 == 0:
                print(90-(x/4), round((people/79694445.55), 2), round(people))

    for i in range(len(colours)):
        print(int(round(colours[i])), round(populations[i]))

PNG = load_png()
array = load_text()
calculate_population()

