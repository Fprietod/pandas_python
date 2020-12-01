import pandas as pd 
#Create a key: value collection of series to use to
#populate the dataframe for testing

data = {'Month':pd.Series(['January','February', 'March','April',
'May','June','August','September','October','November','December']),
'Rainfall':pd.Series([1.65, 1.25, 1.94, 2.75, 2.75, 3.65, 5.05,
1.50,1.33,0.07,0.50,2.30]),
}

#Creamos el DataFrame usando datos estaticos
#df = pd.DataFrame(data)
#dfc = pd.read_csv(r'./rain.csv')
dfj = pd.read_json(r'./rain.json')
#print("Nuestro data Frame")
#print(dfj, "\n")
#Encontrar los valores faltantes con ceors
dfzeros = dfj.fillna(0)
#print("nuestros valores sin ceros son: \n ",dfzeros)

#Remover los campos con los valores perdidos con zeros
dfclean = dfj.dropna(0)
print("nuestros valores sin el cero son: \n",dfclean)

#Crear una cuenta de todos los campos que contiene vacio
count = 0
for index, row in dfj.iterrows():
    if any(row.isnull()):
        count = count + 1
print("\n Numero de campos con nulos es " + str(count))
#Data analysis
print("Mean: ")
print(dfclean.mean())
# Median
print("\n ","Median")
print(dfclean.median())
#Desviación estandar
print("\n Desviaciónn estandar")
print(dfclean.std())

#Selecting parts of a Data Frame 
# Indexing: Select single columns using a column(temperature) Returns a Series
# example dfclean[temperature]
# Select multiple columns using columm names Must specify a list of column names
#dfclean[[Temperature, Rainfall]]
# Illoc and Loc
# Select a certain row number using iloc: print(Third row \n , dfclean.iloc[2])
#Select a certain row using a certain value
# print(Third row \n, dfindexed.loc[March]);
#Imprime rainfall y su promedio para los primeros tres meses
rainfall = dfclean['Rainfall'][0:3]
print(rainfall, "\n")
print("Mean Rainfall: ", rainfall.mean(),"\n")

print("\n Solo la temperatura y datos de rainfall")

dfTempRain = (dfclean[['Temperature','Rainfall']])
print(dfTempRain)
print("mean \n",dfTempRain.mean())
#Loc function
index = dfclean['Month']
dfindexed = dfclean.set_index(index)

#Re quiere propiedad indexada al data frama
print("Encuentra los campos con el valor \n",dfindexed.loc['March'])