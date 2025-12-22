from nlm import *
import json


function_translation_key={
    "BAND":BAND,
    "BXOR":BXOR,
    "BNOT":BNOT,
    "BORR":BORR,
    "BSSL":BSSL,
    "BSSR":BSSR,
    "BBIC":BBIC,
    "AADD":AADD,
    "AMIN":AMIN,
    "AMUL":AMUL
}

#loaded truth table
def exec_truth_table(path):
    """Pulls truth table from the json file in path, compares it to values generated from nlm.py. debugging system"""
    selection=str
    with open(path,"r") as f:
        global ltt
        ltt=(json.load(f))
    
    while selection not in ltt:
        for i in ltt:
            print(i)
        selection=input("Truth Table to run: ")
    
    outs=[]
    for i in ltt[selection][1]:
        outs.append(function_translation_key[i](chr(ltt[selection][0][0]),chr(ltt[selection][0][1])))
    for i in range(len(outs)):
        print(f"{ord(outs[i])} | {ltt[selection][2][i]} > ",end="")
        if outs[i] == chr(ltt[selection][2][i]):
            print(True)
        else:
            print(False)

