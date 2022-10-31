# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 13:23:14 2022

@author: filip
"""
def funksjonlinje ():
    with open('../innlevering_downloads/max_vind_sola_enkelttall.txt' , 'r', encoding='UTF8') as fp:
        num_lines = sum(1 for line in fp if line.rstrip())
        print('Total lines:', num_lines)
        
