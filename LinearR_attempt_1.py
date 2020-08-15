##########
##########                      Notice that this code will return the average of accuracy of n times prediction and it would predict the last column! 
##########


from sklearn import linear_model
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder as le



def csv2d(file = 'iris_flower_data.csv'):

    my_file = open(file, 'r')
    column_number = len(my_file.readline().split(','))

    classes = [str(each_column) for each_column in range(column_number)]

    column_number -= 1

    dataset = pd.read_csv(file ,names = classes)

    encoder = le()
    dataset[str(column_number)] = encoder.fit_transform(dataset[str(column_number)])

    global x,y

    x , y  = dataset.drop(str(column_number),axis = 1) , dataset[str(column_number)]



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

print(f"The average of accuracies are:{avg_pred_acc/number_pred}")
