import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
df = pd.read_csv('realtor-data.csv')

#print(df.head())
#print(df.info())
#print(df.describe())

df['price'].hist()
plt.xlabel('price')
plt.ylabel('Os Y')
plt.title("wykres")
plt.show()

numeric_columns = df.select_dtypes(include=[np.number])
correlation_matrix = numeric_columns.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title("macierz korelacji")
plt.show
