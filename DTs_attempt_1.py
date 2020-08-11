import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor as DTs
from sklearn.model_selection import train_test_split
from sklearn.tree import export_graphviz
import pydotplus
from sklearn.preprocessing import LabelEncoder as le



classes = ['school','sex','age','address','famsize','Pstatus','Medu','Fedu','Mjob','Fjob','reason','guardian','traveltime',
           'studytime','failures','schoolsup','famsup','paid','activities','nursery','higher','internet',
           'famrel','freetime','goout','health','absences','G1','G2','G3']

dataset = pd.read_csv('student-mat.csv')

for i in range(30):

    if type(dataset[classes[i]].loc[0]) == np.int64:
        encoder = le()
        n_data = encoder.fit_transform(dataset[classes[i]])
        for k in range(len(dataset)):
            dataset.iat[k,i] = n_data[k]

x , y  = dataset.drop('G3',axis = 1) , dataset['G3']


x_train, x_test , y_train , y_test = train_test_split(x,y,test_size=0.20)


regressor = DTs(criterion='mse',random_state=100,max_depth=30)
regressor.fit(x_train,y_train)

#export_graphviz(regressor,out_file='reg_tree.dot')

y_pred = regressor.predict(x_test)


#print(y_test)
