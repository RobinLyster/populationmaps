# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 09:49:32 2020

@author: Robin

"""
from matplotlib import image
import math

def load_png():
    """
    loads the world map

    """
    print("Starting...")
    png = image.imread('2.5min_future.png')
    png = 255 * png
    print("Image Loaded")
    return png

def calculate_population():
    """    
    Waaaaa

    """
    colours = []
    areas = []
    list_number = 0
    area = 0
    for x in range(4320):
        area = 708422.8 * 57.095 * abs(math.sin(3.1416*(90-x/24)/180) - math.sin(3.1416*(90-(x-1)/24)/180)) * (3.1416/4320)
        for y in range(8640):
            current_colour = (1000000 * PNG[x, y, 0]) + (1000 * PNG[x, y, 1]) + (PNG[x, y, 2])
            try:
                list_number = colours.index(current_colour)
            except ValueError:
                colours.append(current_colour)
                areas.append(0)
                list_number = len(colours)-1
            else:
                list_number = colours.index(current_colour)
            areas[list_number] = areas[list_number] + area
            if y == 8639 and x%24 == 0:
                print(90-(x/24), area)
    for i in range(len(colours)):
        print(int(round(colours[i])), round(areas[i]))

PNG = load_png()
calculate_population()


