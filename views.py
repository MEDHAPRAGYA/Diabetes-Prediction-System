from django.shortcuts import render
import pandas as pd #Access and manipulation of dataset
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def home(request):
    return render(request, 'home.html')
def predict(request):
    return render(request, 'predict.html')
def result(request):
    data = pd.read_csv(r'C:\Users\ARPIT\OneDrive\Desktop\DiabetesPrediction\diabetes.csv')
    X = data.drop("Diabetes_012", axis=1)
    Y = data["Diabetes_012"]
    X_train, Y_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2)

    model = LogisticRegression()
    model.fit(X_train, Y_train)

    val1 = float(request.GET['n1'])
    val2 = float(request.GET['n2'])
    val3 = float(request.GET['n3'])
    val4 = float(request.GET['n4'])
    val5 = float(request.GET['n5'])
    val6 = float(request.GET['n6'])
    val7 = float(request.GET['n7'])
    val8 = float(request.GET['n8'])
    val9 = float(request.GET['n9'])
    val10 = float(request.GET['n10'])
    val11 = float(request.GET['n11'])
    val12 = float(request.GET['n12'])
    val13 = float(request.GET['n13'])
    val14 = float(request.GET['n14'])
    val15 = float(request.GET['n15'])
    val16 = float(request.GET['n16'])
    val17 = float(request.GET['n17'])
    val18 = float(request.GET['n18'])
    val19 = float(request.GET['n19'])
    val20 = float(request.GET['n20'])
    val21 = float(request.GET['n21'])

    pred = model.predict([[val1, val2, val3, val4, val5, val6, val7, val8, val9, val10, val11, val12, val13, val14, val15, val16, val17, val18, val19, val20, val21]])

    result1 = ""
    if int(pred)==0:
        result1 = "The patient is Non-Diabetic"
    elif int(pred)==1:
        result1 = "The patient is Pre-Diabetic"
    else:
        result1 = "The patient is Diabetic"

    return render(request, 'predict.html', {"result2":result1})