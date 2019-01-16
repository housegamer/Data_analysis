import pandas as pd 


df1 = pd.DataFrame({'HPI':[80,62,60,87],
					'Int_rate':[2,3,2,2],
					'US_GDP_Thousands':[50,55,64,55]},	
					index = [2001,2002,2003,2004])

df2 = pd.DataFrame({'HPI':[80,68,60,87],
					'Int_rate':[2,3,2,2],
					'US_GDP_Thousands':[50,55,64,55]},	
					index = [2005,2006,2007,2008])


df3 = pd.DataFrame({'HPI':[80,61,60,87],
					'Int_rate':[2,3,2,2],
					'US_GDP_Thousands':[50,52,50,53]},	
					index = [2001,2002,2003,2004])


#Concatenating data
'''concat = pd.concat([df1,df2,df3])
print(concat)'''

# Appending data to the end
df4 = df1.append(df3)
print(df4)