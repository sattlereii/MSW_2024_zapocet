import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

titanic_data = pd.read_csv('train.csv')
print(titanic_data.head())

titanic_data['Age'].fillna(titanic_data['Age'].median(), inplace=True)
titanic_data.drop('Cabin', axis=1, inplace=True)
titanic_data['Embarked'].fillna(titanic_data['Embarked'].mode()[0], inplace=True)
print(titanic_data.isnull().sum())

# Míra přežití podle pohlaví
plt.figure(figsize=(8, 6))
sns.countplot(x='Sex', hue='Survived', data=titanic_data)
plt.title('Míra přežití podle pohlaví')
plt.show()

# Míra přežití podle třídy
plt.figure(figsize=(8, 6))
sns.countplot(x='Pclass', hue='Survived', data=titanic_data)
plt.title('Míra přežití podle třídy')
plt.show()

# Věková distribuce přeživších a nepřeživších
plt.figure(figsize=(10, 6))
sns.histplot(titanic_data[titanic_data['Survived'] == 1]['Age'], bins=30, kde=False, color='green', label='Přeživší')
sns.histplot(titanic_data[titanic_data['Survived'] == 0]['Age'], bins=30, kde=False, color='red', label='Nepřeživší')
plt.legend()
plt.title('Věková distribuce přeživších a nepřeživších')
plt.show()

# Distribuce ceny lístku podle třídy
plt.figure(figsize=(10, 6))
sns.boxplot(x='Pclass', y='Fare', data=titanic_data)
plt.title('Distribuce ceny lístku podle třídy')
plt.show()

# Míra přežití podle přístavu nalodění
plt.figure(figsize=(8, 6))
sns.countplot(x='Embarked', hue='Survived', data=titanic_data)
plt.title('Míra přežití podle přístavu nalodění')
plt.show()
