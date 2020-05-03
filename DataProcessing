import pandas as pd

dfr = pd.read_csv('/Users/xu/Desktop/QuarantineShoppingInput.csv', delimiter = ',')
dfr = dfr[['County', 'Establishment Type', 'Entity Name', 'Street Name', 'City', 'State', 'Zip Code', 'Location']]
dfr = dfr.applymap(lambda x: str(x).strip())
options = ['JAC', 'JABC']
dfr = dfr[dfr['Establishment Type'].isin(options)]

print(dfr.head())

dfp = pd.read_csv('/Users/xu/Desktop/Food_Pantry_List.csv', delimiter = ',')
dfp = dfp[['Agency Name', 'Hours of Operation', 'Location']]
dfp = dfp.applymap(lambda x: str(x).strip())
dfp = dfp[dfp['Location'].notnull()]
#print(dfp.head())

names = dfr['Entity Name'].tolist()
names = names + dfp['Agency Name'].tolist()
print(len(names))

locations = []
for location in dfr['Location'].tolist():
    locations.append(location[location.rfind('('):])
for location in dfp['Location'].tolist():
    locations.append(location[location.rfind('('):])
print(len(locations))
