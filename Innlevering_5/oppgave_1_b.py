# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 12:51:51 2022

@author: filip
"""

def funksjontemp (x, y):
    return y-x

while True:
    try: 
        verdi1 = float(input("skriv inn første temp"))
        verdi2 = float(input("skriv inn neste temp"))
        e = funksjontemp(verdi1,verdi2)
        print("endring i temperatur er:",e)
        break
    except: 
        print("skriv inn et tall!!")
      
        
    
    

