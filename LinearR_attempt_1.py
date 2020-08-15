from sklearn import linear_model
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder as le


def csv2d(file = 'iris_flower_data.csv'):

    classes = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']

    dataset = pd.read_csv(file ,names = classes)

    encoder = le()
    dataset['class'] = encoder.fit_transform(dataset['class'])

    global x,y

    x , y  = dataset.drop('class',axis = 1) , dataset['class']



def pred():

    csv2d()

    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.20)

    linear = linear_model.LinearRegression()

    linear.fit(x_train,y_train)


    y_predict = list(linear.predict(x_test))

    y_test = list(y_test)

    y_predict = list(map(round,y_predict))
    y_predict = list(map(int,y_predict))


    return accuracy_score(y_test,y_predict)

number_pred = int(input("How many times you wanna predict? "))

avg_pred_acc = 0

for i in range(number_pred):
    avg_pred_acc += pred()

print(f"The avrage of accuracies are:{avg_pred_acc/number_pred}")
