# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 09:49:32 2020

@author: Robin

"""
import random
import math
import xlrd
from PIL import Image
image_name = '2.5min.png'
test_image = 'oneo.png'
image = Image.open(image_name)
image = image.convert('RGB')
colors = image.getcolors()
pixelMap = image.load()
newImg = Image.new(image.mode, image.size)
pixelsNew = newImg.load()
width, height = newImg.size
divisionone = 100
divisiontwo = 100
newImg.save(test_image)
world = 7969436033.912283
def load_sheet():
    """
    loads the population grid

    """
    book = xlrd.open_workbook('2.5min.xlsx')
    sheet = book.sheet_by_name('grid')
    print("Spreadsheet Loaded")
    return sheet
def calculate_population_long_first():

    population = 0
    n = 1
    previous = 0
    population_list = [0]
    population_new = 0
    colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    for y in range(width):
        for x in range(height):
            if SHEET.cell_value(x, y) > 0:
                population += SHEET.cell_value(x, y)
        if population >= n * world/divisionone:
            population_list.append(population)
            population_new = population_list[n] - population_list[n-1]
            n += 1
#            for h in range(height):
#                pixelsNew[y,h] = (0, 0, 0)
            m = 1
            population_2 = 0
            for a in range(height):
                for b in range(previous, y+1):
                    if pixelMap[b, a] == (255, 255, 255):
                        pixelsNew[b, a] = (255, 255, 255)
                    else:
                        pixelsNew[b, a] = colour
                    if SHEET.cell_value(a, b) > 0:
                        population_2 += SHEET.cell_value(a, b)
                if population_2 >= m * (population_new/divisiontwo):
                    colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                    m += 1
#                    for g in range(previous , y):
#                        pixelsNew[g,a] = (0, 0, 0)
            previous = y+1
    for y in range(int(math.floor(73*height/90)), height):
        for x in range(width):
            pixelsNew[x, y] = (255, 255, 255)
    image.close()
    newImg.save(test_image)
def calculate_population_lat_first():

    population = 0
    n = 1
    previous = 0
    population_list = [0]
    population_new = 0
    colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    for x in range(height):
        for y in range(width):
            if SHEET.cell_value(x, y) > 0:
                population += SHEET.cell_value(x, y)
        if population >= n * world/divisionone:
            population_list.append(population)
            population_new = population_list[n] - population_list[n-1]
            n += 1
#            for h in range(height):
#                pixelsNew[y,h] = (0, 0, 0)
            m = 1
            population_2 = 0
            for b in range(width):
                for a in range(previous, x+1):
                    if pixelMap[b, a] == (255, 255, 255):
                        pixelsNew[b, a] = (255, 255, 255)
                    else:
                        pixelsNew[b, a] = colour
                    if SHEET.cell_value(a, b) > 0:
                        population_2 += SHEET.cell_value(a, b)
                if population_2 >= m * (population_new/divisiontwo):
                    colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                    m += 1
#                    for g in range(previous , y):
#                        pixelsNew[g,a] = (0, 0, 0)
            previous = x+1
    for y in range(int(math.floor(73*height/90)), height):
        for x in range(width):
            pixelsNew[x, y] = (255, 255, 255)
    image.close()
    newImg.save(test_image)
SHEET = load_sheet()
calculate_population_long_first()
test_image = 'twoo.png'
calculate_population_lat_first()
