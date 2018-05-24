import json
import pandas as pd


def load_file(fileloc):
    data = []

    # read file line by line and strip white space
    x=0
    with open(fileloc, encoding='utf-8') as f:
        #try:
        for line in f:
            x+=1
            data.append(json.loads(line.rstrip()))
        #except:
        print(x,"   ")

        print("second ", x)
    return data

#sorts out the dataset to keep only food places
def rowselect(dataframe):
    TFlist=[]
    for categ in dataframe['categories'].tolist():
        x=0
        for i in categ:
            if i== 'Food' or i=='Restaurants':
                TFlist.append(True)
                x=1
                break
        if x==0:
            TFlist.append(False)

    return TFlist

#load data file
data = load_file('business.json')
bus_df = pd.DataFrame.from_dict(data)
bus_df= bus_df.iloc[1:]
bus_df=bus_df[rowselect(bus_df)]
bus_df=bus_df.reset_index(drop=True)


incomeDF= pd.read_csv('Income.csv')
review = load_file('review.json')
review_df = pd.DataFrame.from_dict(review)

bus=bus_df[['business_id','name','postal_code','review_count','stars','state']]
bus= bus.rename(columns={'postal_code':'ZIPCODE'})
#converts the whole income data set to strings to draw comparisons with ZIPCODE
i = incomeDF.applymap(str)
BI= bus.merge(i,on=['ZIPCODE'])
#removing the columns that's not needed
Clean_BI= BI[['business_id','name','review_count','stars','state','ZIPCODE','Adjusted gross income (AGI)','Avg AGI']]
#usd only to convert the Avg agi column to floats fromt strings

MegaSet= review_df.merge(Clean_BI,on='business_id',how='inner')
#MegaSet['Avg AGI'].astype(float)


#print(MegaSet)
MegaSet.to_csv('SortedMaindata.csv', sep= ',',encoding= 'utf-8')
#MegaSet.to_json('Mains.json', date_format = 'iso', orient = 'records')
#used to convert pd to excel
from pandas import ExcelWriter

def ExcelWrite(yourdf, file,sheet):

    writer = ExcelWriter(file)
    yourdf.to_excel(writer, sheet)
    writer.save()
#ExcelWrite(MegaSet,'Processed.xlsx','Sheet1')
