import pandas as pd 


df1 = pd.DataFrame({'Year':[2001,2002,2003,2004],
					'Int_rate':[2,3,2,2],
					'US_GDP_Thousands':[50,55,64,55]})
					#index = [2001,2002,2003,2004]),

'''df2 = pd.DataFrame({"HPI":[80,68,60,87],
					"Int_rate":[2,3,2,2],
					"US_GDP_Thousands":[50,55,64,55]},	
					index = [2005,2006,2007,2008])'''

df3 = pd.DataFrame({'Year':[2001,2003,2004,2005],
					'Unemployment':[6,7,8,9],
					'Low_Tier_HPI':[50,52,50,53]})
					#index = [2001,2002,2003,2004])



#Merging
#print(pd.merge(df1,df2, on=['HPI','Int_rate']))

# Joining
'''df1.set_index("HPI", inplace = True)
df3.set_index("HPI", inplace = True)

joined = df1.join(df3)
print(joined)'''

merged = pd.merge(df1,df3, on = 'Year')
merged.set_index('Year', inplace= True)
print(merged)


#IMPORT INFO
''' When the index doesnt matter, you would generally use MEREGE,
JOIN when the index does matter, CONCAT or APPENDING when ususing long DATES'''