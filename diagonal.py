# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 09:49:32 2020

@author: Robin

"""
import xlrd
from PIL import Image 
import random
import math
image_name = '15min.png'
test_image = 'diagonal.png'   
image = Image.open(image_name)
image = image.convert('RGB') 
colors = image.getcolors()
pixelMap = image.load()
newImg = Image.new(image.mode,image.size) 
pixelsNew = newImg.load()
width,height = newImg.size
divisionone = 10000
divisiontwo = 5
newImg.save(test_image)
colour = (0, 0, 0)
world = 7969435930
def load_sheet():
    """
    loads the population grid

    """
    book = xlrd.open_workbook('15min.xlsx')
    print("halfway")
    sheet = book.sheet_by_name('grid')
    print("Spreadsheet Loaded")
    return sheet
def calculate_population_long_first():
    s = 0
    population = 0
    n = 1
    k = 0
    p = 0
    colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    for i in range(width + height - 1):
        if i<height:
            k = i + 1
        elif i < width:
            k = height
        else:
            k = height + width - i - 1
        for j in range(k):
            p += 1
            if i<height:
                x = j
                y = k - j - 1
            else:
                x = j + i - height + 1
                y = height - j - 1
            try:
                if SHEET.cell_value(y , x) >= 0:
                    population += SHEET.cell_value(y, x)
                    if pixelMap[x,y]==(255,255,255):
                        pixelsNew[x,y] = (255,255,255)
                    else:
                        pixelsNew[x,y] = colour
            except:
                if s%1000 == 0:
                    print(p, s)
                s = s + 1
        if population >= n * world/divisionone and n < divisionone:
            colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            n = math.ceil(population/(world/divisionone))
    image.close() 
    newImg.save(test_image)

SHEET = load_sheet()
calculate_population_long_first()
