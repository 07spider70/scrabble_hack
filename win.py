# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 14:08:52 2018

@author: janci
"""
import itertools as it


#scrabble values
hodnoty = {
    'eaionrtlsu':1,
    'dg':2,
    'bcmp':3,
    'fhvwy':4,
    'k':5,
    'jx':8,
    'qz':10
        }



#import list of all correct words for scrabble
def get_words(path='words.txt'):
    data = []
    with open(path,'r') as file:
        for i in file.readlines():
            data.append(i[:-1:])
    return data

#create list of all words from 1 to 'd' length
def dlzka(d,data):
    vys=[]
    for i in data:
        for j in range(1,d+1):
            
            if len(i)==j:
                vys.append(i)
    return vys

#according to dic of values it count score of word
def get_score(slovo):
    score=0
    for i in slovo:
        for j in hodnoty.keys():
            if i in j:
                score+=(hodnoty[j])
    return score

"""
f take z_p = string of our letters, dlzka = length of word,  data = list of words and possibly the starting letter
f make combinations and return list of possible words with scores
"""  
def pismena(z_p,dlzka,data,zac_pism=""):
    vys = []
    for j in range(1,dlzka+1):
        if zac_pism=="":
            p = it.combinations(z_p,j)
            for i in p:
                tem = "".join(i)
                if (tem) in data and (tem) not in vys:
                    vys.append(tem)
                    vys.append(get_score(tem))
            
        
        else:
            p = it.combinations(z_p,j)
            for i in p:
                slov = "".join(i)
                if slov[0]==zac_pism and slov in data and slov not in vys:
                    vys.append(slov)
                    vys.append(get_score(slov))
    return vys
        
#f for readable output
def beauty_out(text,dl):
    if len(text)==0:
        return None
    else:
        for i in range(0,len(text)-1,2):
            
            print("{:{}} .....value: {}".format(text[i],dl,text[i+1]))
            

#f take string of out letters, max length of word and possibly first letter of word
def main(zoznam_pismen,dlzku_slova,zac=""):
    dat=get_words()
    vys = pismena(zoznam_pismen,dlzku_slova,dlzka(dlzku_slova,dat),zac)
    #print(vys)
    beauty_out(vys,dlzku_slova)