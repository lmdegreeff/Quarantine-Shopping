import pandas as pd

dfr = pd.read_csv('/Users/xu/Desktop/QuarantineShoppingInput.csv', delimiter = ',')
dfr = dfr[['County', 'Establishment Type', 'Entity Name', 'Street Name', 'City', 'State', 'Zip Code', 'Location']]
dfr = dfr.applymap(lambda x: str(x).strip())
options = ['JAC', 'JABC']
dfr = dfr[dfr['Establishment Type'].isin(options)]

print(dfr.head())

dfp = pd.read_csv('/Users/xu/Desktop/Food_Pantry_List.csv', delimiter = ',')
df_info = dfp[['Phone Number', 'Hours of Operation']]
dfp = dfp[['Agency Name', 'Location']]
dfp = dfp.applymap(lambda x: str(x).strip())
dfp = dfp[dfp['Location'].notnull()]
#print(dfp.head())

names = dfr['Entity Name'].tolist()
names = names + dfp['Agency Name'].tolist()
print(names)

locations = []
for location in dfr['Location'].tolist():
    locations.append(location[location.rfind('('):])
for location in dfp['Location'].tolist():
    locations.append(location[location.rfind('('):])
#print(locations)

info = []
for location in dfr['Location'].tolist():
    info.append('no information available')
for index, row in df_info.iterrows():
    info.append(str(row['Phone Number']) + ' ' + row['Hours of Operation'])
#print(info)
