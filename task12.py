import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#data reading
data = pd.read_csv(r'data/winequality-red.csv', sep=';')
#Shape of dataset
print(data.shape)
#Columns of dataset
print(data.columns)

#Rename columns of dataset into standard format
renamed_columns = {
    'fixed acidity': 'fixed_acidity',
    'volatile acidity': 'volatile_acidity',
    'citric acid': 'citric_acid',
    'residual sugar': 'residual_sugar',
    'chlorides': 'chlorides',
    'free sulfur dioxide': 'free_sulfur_dioxide',
    'total sulfur dioxide': 'total_sulfur_dioxide',
    'density': 'density',
    'pH': 'ph',
    'sulphates': 'sulphates',
    'alcohol': 'alcohol',
    'quality': 'quality'
}
data.rename(columns=renamed_columns, inplace=True)

#Select top variables
top_variables = ['volatile_acidity', 'citric_acid', 'chlorides', 'total_sulfur_dioxide', 'density', 'sulphates', 'alcohol', 'quality']
data = data[top_variables]

#Generate summary statistics for three key variables.
key_variables = ['volatile_acidity', 'sulphates', 'alcohol']
data[key_variables].describe().transpose()

for i in key_variables:
    if i == "quality":
        break
    sns.barplot(x="quality",y = i,data=data ,palette ='pastel', hue="quality")
    plt.show()

data['quality'].unique()

#We can transform column quality to binary value
#If the quality value is less than or eqaul to 6 then 'Low'
#If quality value is greater than 6 then 'High'
data['quality'] = np.where(data['quality'] > 6, 'High', 'Low')
data['quality'].value_counts()