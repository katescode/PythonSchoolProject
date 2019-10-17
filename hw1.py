from inBetwWrapper import *

def Hw1(UseTD,inBetwWarp):
    print("\nзадание 3\n")

    """temp"""
    global UseTestData
    UseTestData = inBetwWarp.get_isItTest()
    """temp"""


    # inBetwTodayYourNameIs()
    # inBetwLetterCounter()
    # inBetwRemainder()
    # inBetwGeoMean()
    # inBetwFuncWX()
    # inBetwBmi()
    # inBetwMultiple3()
    # inBetwRoot3OfGeoMean()
    # inBetwGeoMeanStrings()
    # inBetwStringLenPow()

def inBetwTodayYourNameIs():
    if UseTestData:
        name = 'Андрей'
    else:
        name = input('Введите ваше имя ')
    answ=TodayYourNameIs(name)
    print(answ)

def inBetwLetterCounter():
    if UseTestData:
        word = 'Очаровательно'
    else:
        word = input('Введите слово для подсчета букв ')
    answ = LetterCounter(word)
    print("В слове " + word + " " + str(answ) + " букв")
def inBetwRemainder():
    if UseTestData:
        a = 117
        b = 23
    else:
        a = int(input('Введите a '))
        b = int(input('Введите b '))
    answ = Remainder(a,b)
    print("Остаток от деления " + str(a) + " на " + str(b) + " = " + str(answ))
def inBetwGeoMean():
    if UseTestData:
        a = 12
        b = 17
        c = 25
    else:
        a = int(input('Введите число a '))
        b = int(input('Введите число b '))
        c = int(input('Введите число c '))
    answ=GeoMean(a, b, c)
    print("Среднее геометрическое чисел " + str(a) + ", " + str(b) + " и " + str(c) + " это " + str(answ))
def inBetwFuncWX():
    if UseTestData:
        x = 100500
    else:
        x = int(input('Введите x '))
    answ = FuncWX(x)
    print("результатом функции 6.996+45*pow(x/2,2)+2*x при x = " + str(x) + " будет " + str(answ))
def inBetwBmi():
    if UseTestData:
         weight = 80
         height = 1.8
    else:
        weight = float(input('Введите вес '))
        height = float(input('Введите рост в метрах '))
    if(height>3):
        import math
        numCount = len(str(math.trunc(height)))
        while numCount>1:
            height=height/10
            numCount = len(str(math.trunc(height)))
        print("рост изменён на",height)
    answ = Bmi(weight, height)
    print("Индекс массы тела при весе " + str(weight) + "кг и росте " + str(height) + "м состовляет " + str(answ))

    if __name__ != '__main__':
        return answ
def inBetwMultiple3():
    if UseTestData:
        a = 23
    else:
        a = int(input('Введите число a '))
    answ = Multiple3(a)
    print("Вы ввели число которое при умножении на 3 дает  " + str(answ))
def inBetwRoot3OfGeoMean():
    if UseTestData:
        a=270
        b=12.8
    else:
        a = float(input('Введите a '))
        b = float(input('Введите b '))
    answ = Root3OfGeoMean(a,b)
    print("корень 3 степени из среднего арифметического чисел ", a, " и ", b, "равняется", answ)
def inBetwGeoMeanStrings():
    if UseTestData:
        string_1='Hello, world!'
        string_2='Python<3'
        string_3='qwerty'
    else:
        string_1 = input('Введите первое слово ')
        string_2 = input('Введите второе слово ')
        string_3 = input('Введите третье слово ')
    answ = GeoMeanStrings(string_1, string_2, string_3)
    print("Среднее геометрическое строк " + string_1 + ", " + string_2 + " и " +
          string_1 + " это " + str(answ))
def inBetwStringLenPow():
    if UseTestData:
        string = 'привет'
        power = 2
    else:
        string = input('Введите первое строку ')
        power = int(input('Введите целое число '))
    answ = StringLenPow(string, power)
    # строка, кол-во символов в строке, кол-во символов в строке в степени
    print(string,LetterCounter(string),answ)

def TodayYourNameIs(name):
    answ = 'Сегодня Вас зовут '+ name
    return answ
def LetterCounter(word):
    answ = len(word)
    return answ
def Remainder(a,b):
    answ = a % b
    return answ
def GeoMean (a,b,c):
    answ= pow(a * b * c, 1 / 3)
    return answ
def FuncWX(x):
    answ = 6.996 + 45 * pow(x / 2, 2) + 2 * x
    return answ
def Bmi(weight, height):
    answ = weight / pow(height, 2)
    return answ
def Multiple3(a):
    answ = a * 3
    return answ
def Root3OfGeoMean(a,b):
    root = 3
    import math
    Mean = math.sqrt(a * b)
    answ= pow(Mean, 1 / root)
    return answ
def GeoMeanStrings(string_1,string_2,string_3):
    answ = GeoMean(len(string_1),len(string_2),len(string_3))
    return answ
def StringLenPow(string, power):
    stringlen = len(string);
    answ = pow(len(string),power)
    return  answ

def UseTestDataChanger(changeTo):
    global UseTestData
    UseTestData = changeTo

def TestDataIs():
    return UseTestData