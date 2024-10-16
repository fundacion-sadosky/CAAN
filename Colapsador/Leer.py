# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 10:39:45 2023

@author: Richard
"""

import pandas as pd

import os

csvs = os.listdir('Nuevos/')

# df = pd.read_csv("Nuevos/Adjetivos.csv", encoding='latin-1')

dic = {}

for x in csvs:
      df = pd.read_csv("Nuevos/" + x, encoding='latin-1')
      L = df.columns.values.tolist()
      for y in L:
          a = list(df[y])
          dic[y] = [y] + a
          
# print(dic)      

import json

def save_pet(pet,filename):
    with open(filename, 'w') as f:
        f.write(json.dumps(pet))

def load_pet(filename):
    with open(filename) as f:
        pet = json.loads(f.read())
    return pet

save_pet(dic, "Diccionarios/diccionario.json")

s = "querés ir al baño"

s = "fuimos a correr con el perrito gordito"

l = s.split(" ")

os = ""

for x in l: 
   try: 
     for keys in dic:
        b = dic[keys]
        for y in b:
             if x == y:
                 os = os + " " + keys  
                 raise StopIteration
   except StopIteration:
        pass  

os = os[1:]        

print(os)  


# df = pd.read_csv("Palabras/Verbos encolumnados.csv", encoding='latin-1')

 

# print(list(df["correr"]))