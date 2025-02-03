

#import Library

import pandas as pd
import matplotlib.pyplot as plt

#import dataset
data=pd.read_csv("Bogura.csv")
#print(data)

#Data Preprocessing
dataFill=data.fillna(value=450)
pd.set_option('display.max_column',None)
# print(dataFill)

#Slicing the dataset
x=dataFill.iloc[:,7:8].values
y=dataFill.iloc[:,9].values
# print(x)

# splitting the dataset

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.4,random_state=0)
# print(x_train)
# print(x_test)

from sklearn.preprocessing import MinMaxScaler
scale1=MinMaxScaler()
x_train=scale1.fit_transform(x_train)
# print(x_train)
# print(x_test)


from sklearn.svm import SVC
cli=SVC(kernel="linear",random_state=0)
cli.fit(x_train,y_train)
y_predict=cli.predict(x_test)

from sklearn.metrics import confusion_matrix,accuracy_score
cm=confusion_matrix(y_test,y_predict)
print(cm)
acc=accuracy_score(y_test,y_predict)
print(acc)

# graph

# Scatter Plot
plt.figure(figsize=(8, 6))
plt.scatter(data["Half-Yearly Income"], data["Member of Family"], color='r', alpha=0.8, edgecolors='k')
plt.title("Half-Yearly Income vs Member of Family")
plt.grid(ls='--', alpha=0.8)
plt.show()

# Histogram
plt.figure(figsize=(8, 6))
data["Half-Yearly Income"].plot(kind='hist', bins=16, color='green', edgecolor='blue', alpha=0.8)
plt.title("Distribution of Half-Yearly Income")
plt.grid(ls='--', alpha=0.8)
plt.show()

# Box Plot
plt.figure(figsize=(8, 6))
data.boxplot(column=["Half-Yearly Income"], patch_artist=True, boxprops=dict(facecolor='yellow'))
plt.title("Half-Yearly Income Box Plot")
plt.grid(ls='--', alpha=0.8)
plt.show()

# Bar Plot
plt.figure(figsize=(8, 6))
data.plot(kind="bar", x="Half-Yearly Income", y="Member of Family", color='pink', alpha=0.8)
plt.title("Half-Yearly Income vs Member of Family")
plt.grid(ls='--', alpha=0.8)
plt.show()

# Pie Chart
plt.figure(figsize=(8, 6))
data.groupby("Half-Yearly Income")["Member of Family"].sum().plot(kind='pie', autopct='%1.1f%%', colormap='viridis')
plt.ylabel("")
plt.title("Member of Family Distribution by Half-Yearly Income")
plt.show()