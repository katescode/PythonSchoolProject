import pandas as pd
import matplotlib as mp
import seaborn as sns
import numpy as np

sns.set()



def wPandas():

    print("pandas титаник")
    inBetw()


def inBetw():
    traindata = loadDataFromCSV()
    traindata = delRow(traindata,'PassengerId','Ticket','Cabin')
    traindata['Fare']=round(traindata['Fare'],2)
    traindata['Embarked'].fillna('No data', inplace = True)
    #firstOutputs(traindata)
    #secondFiltrs(traindata)
    #secondValueCount(traindata)
    secondGroupby(traindata)

def firstOutputs(traindata):
    headFunc(traindata,0)
    headFunc(traindata,10)
    traindata.info()
    print(traindata.describe().T)
    print(traindata)
    onlyOneRow(traindata,"Pclass" )
    headFunc(traindata[(traindata["Pclass"]==1)&(traindata["Survived"]==0)],10)
    print(traindata['Fare'].min())
    print(traindata[traindata['Age']>=18]['Fare'].min())
def secondFiltrs(traindata):
    print(traindata[traindata['Fare']==0]['Age'].max())
    print(traindata[traindata['Age']<18]['Fare'].min())
    print(traindata[traindata['Fare']>0]['Fare'].min())
    print(traindata[traindata['Pclass']==1]['Fare'].median())
def secondValueCount(traindata):
    print(traindata['Survived'].value_counts())
    print(traindata[traindata['Sex']=='male']['Survived'].value_counts())
    print(traindata[traindata['Sex']=='female']['Survived'].value_counts())
    SexValCount(traindata)
    print(traindata[traindata['Pclass']==1]['Survived'].value_counts())
    SexNClassValCOunt(traindata)
def secondGroupby(traindata):
    pass



def loadDataFromCSV():
    df = pd.read_csv('train.csv')
    return df
def delRow(df,*args): 
    for row in args:
        df.drop([row], axis = 1, inplace = True)
    return df
def headFunc(df,num):
    if num == False :
        print(df.head())
    else:
        print(df.head(num))
def onlyOneRow(df, row):
    headFunc(df[df[row]==1],10)   

def SexValCount(traindata):
    for date in traindata['Sex'].unique():
        if date == 'male':
            print('Данные о мужчинах')
        else:
            print('Данные о женщинаж')
        print(traindata[traindata['Sex']==date]['Survived'].value_counts())
def SexNClassValCOunt(traindata):
    for dClass in sorted(traindata['Pclass'].unique()):
        if dClass ==1:
            print('пассажиры первого класса')
        if dClass ==2:
            print('пассажиры второго класса')
        if dClass ==3:
            print('пассажиры третьего класса')
        else:
            pass
        
        for date in traindata['Sex'].unique():
            if date == 'male':
                print('Данные о мужчинах')
            else:
                print('Данные о женщинаж')
            print(traindata[(traindata['Sex']==date)&(traindata['Pclass']==dClass)]['Survived'].value_counts())
        





