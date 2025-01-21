
import pandas as pd
from PIL.ImageOps import scale

data = pd.read_csv("demoData.csv")
X=data.iloc[:,1:5].values
Y=data.iloc[:,-1:].values
#print(X)
#print(Y)

from sklearn.preprocessing import LabelEncoder
lb = LabelEncoder()
X[:,0] = lb.fit_transform(X[:,0])
print(X)

lb2 = LabelEncoder()
Y = lb2.fit_transform(Y)

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
print(X_train)
print(X_test)
from sklearn.preprocessing import MinMaxScaler
scale = MinMaxScaler()
X_train_scaled = scale.fit_transform(X_train)
print(X_train_scaled)