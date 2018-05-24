import pandas as pd
import re
import nltk
import string
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from pymining import itemmining
#removes punctuation and stop words

def ReadProcessedSent(textfile):
    Sentencelist=[]
    with open(textfile) as f:
        for line in f:
            line = line.replace("[", "")
            line = line.replace("]", "")
            if line.strip():
                line = line.replace("\n","")
                Sentencelist.append(line.split(","))
    return Sentencelist


def FreqentPattern(fileloc):

    megawordlist= ReadProcessedSent(fileloc)
    relim_input = itemmining.get_relim_input(megawordlist)
    patternlist=itemmining.relim(relim_input, min_support=0.007*len(megawordlist))
    return patternlist

def ExcelWrite(yourdf, file):

    writer = pd.ExcelWriter(file)
    yourdf.to_excel(writer, "Sheet1")
    writer.save()

def ConvertoExcel(dict,filename):

    df= pd.DataFrame(list(dict.items()), columns=['Pattern','Frequency'])
    ExcelWrite(df,filename)

patternlist=FreqentPattern("C:\\Users\\naven\\Desktop\\UofR Fall 2017\\CSC 240\\research\\ProcessFile\\income1star1new.txt")

for keys, values in patternlist.items():
    patternlist[(str(keys).replace("frozenset",""))]=patternlist.pop(keys)

ConvertoExcel(patternlist,"I1S1_Pattern.xlsx")





