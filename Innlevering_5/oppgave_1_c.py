# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 09:52:15 2022

@author: filip
"""
fortsetter = True
while fortsetter:
    file = open ('../innlevering_downloads/max_vind_sola_enkelttall.txt' , 'r', encoding='UTF8')
    try:
        fortsetter = False
    except FileNotFoundError:
            print("kan ikke finne fila")
            print("prøv på nytt")
        
summen = 0

for linje in file:
    try:
        summen += float(linje)
    except ValueError:
        print("En linje inneholder ikke et tall")
print (f'summen ble: {summen}')
file.close()

