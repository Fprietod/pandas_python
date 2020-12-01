import pandas as pd 
#Create a key: value collection of series to use to
#populate the dataframe for testing

data = {'Month':pd.Series(['January','February', 'March','April',
'May','June','August','September','October','November','December']),
'Rainfall':pd.Series([1.65, 1.25, 1.94, 2.75, 2.75, 3.65, 5.05,
1.50,1.33,0.07,0.50,2.30]),
}

#Creamos el DataFrame usando datos estaticos
df = pd.DataFrame(data)
print("Nuestro data Frame")
print(df, "\n")