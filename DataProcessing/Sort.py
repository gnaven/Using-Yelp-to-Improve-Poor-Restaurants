import pandas as pd


mega = pd.read_csv('SortedMaindata.csv', sep= ",", delimiter=",", encoding='utf-8')

mega['Income Range']= pd.cut(mega['Avg AGI'], bins=[0,100,200,300,400], labels=[1,2,3,4])
#mega=mega[np.isfinite(mega['Income Range'])]
print(mega)

df1= mega

input_class='Avg AGI'
input_val=1
df1=df1.iloc[(df1[input_class]-input_val).argsort()]

print (max(df1['Avg AGI']))
df1['Income Range'].astype(int)

from pandas import ExcelWriter

def ExcelWrite(yourdf, file,sheet):

    writer = ExcelWriter(file)
    yourdf.to_excel(writer, sheet)
    writer.save()

# different datasets for income levels
df_IR_1=df1[df1['Income Range']==1]
df_IR_2=df1[df1['Income Range']==2]
df_IR_3=df1[df1['Income Range']==3]
df_IR_4=df1[df1['Income Range']==4]

# within each income range dataframe divided according to rating
#Rating 1-2.5: bad,Ration 2.6-3.9: Average, Rating 4-5: good
df_star_IR1_1 = df_IR_1[(df_IR_1.stars_y >=1) & (df_IR_1.stars_y<=2.5)]
df_star_IR1_2 = df_IR_1[(df_IR_1.stars_y >2.5) & (df_IR_1.stars_y<4)]
df_star_IR1_3 = df_IR_1[(df_IR_1.stars_y >=4)]

df_star_IR1_1['text'].to_csv('income1star1.txt', sep='\t', index=False)
df_star_IR1_2['text'].to_csv('income1star2.txt', sep='\t', index=False)
df_star_IR1_3['text'].to_csv('income1star3.txt', sep='\t', index=False)



df_star_IR2_1 = df_IR_2[(df_IR_2.stars_y >=1) & (df_IR_2.stars_y<=2.5)]
df_star_IR2_2 = df_IR_2[(df_IR_2.stars_y >2.5) & (df_IR_2.stars_y<4)]
df_star_IR2_3 = df_IR_2[(df_IR_2.stars_y >=4)]

df_star_IR2_1['text'].to_csv('income2star1.txt', sep='\t', index=False)
df_star_IR2_2['text'].to_csv('income2star2.txt', sep='\t', index=False)
df_star_IR2_3['text'].to_csv('income2star3.txt', sep='\t', index=False)



df_star_IR3_1 = df_IR_3[(df_IR_3.stars_y >=1) & (df_IR_3.stars_y<=2.5)]
df_star_IR3_2 = df_IR_3[(df_IR_3.stars_y >2.5) & (df_IR_3.stars_y<4)]
df_star_IR3_3 = df_IR_3[(df_IR_3.stars_y >=4)]

df_star_IR3_1['text'].to_csv('income3star1.txt', sep='\t', index=False)
df_star_IR3_1['text'].to_csv('income3star2.txt', sep='\t', index=False)
df_star_IR3_3['text'].to_csv('income3star3.txt', sep='\t', index=False)


df_star_IR4_1 = df_IR_4[(df_IR_4.stars_y >=1) & (df_IR_4.stars_y<=2.5)]
df_star_IR4_2 = df_IR_4[(df_IR_4.stars_y >2.5) & (df_IR_4.stars_y<4)]
df_star_IR4_3 = df_IR_4[(df_IR_4.stars_y >=4)]


df_star_IR4_1['text'].to_csv('income4star1.txt', sep='\t', index=False)
df_star_IR4_2['text'].to_csv('income4star2.txt', sep='\t', index=False)
df_star_IR4_3['text'].to_csv('income4star3.txt', sep='\t', index=False)








