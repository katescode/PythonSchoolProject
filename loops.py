def Loops(UseTD):
    print('\n\nзадание "циклы"\n')
    global UseTestData
    UseTestData = UseTD
    #inBetwoddencript()
    #inBetwleapYear()
    inBetwRuVowels() #dnt


def inBetwoddencript():
    if UseTestData:
        word = 'подшипник'
    else:
        word =input('введите слово')

    answ = oddencript(word)
    print(answ)
def inBetwleapYear():
    if UseTestData:
        year_1 = 2013
        year_2 = 2020
    else:
        year_1 = int(input('введите первый год'))
        year_2 = int(input('введите последний год'))
    answ = leapYear(year_1, year_2)
    print(*answ, sep = "\n")
def inBetwRuVowels():
    if UseTestData:
        pass
    else:
        pass

def inBetw():
    if UseTestData:
        pass
    else:
        pass
def inBetw():
    if UseTestData:
        pass
    else:
        pass
def inBetw():
    if UseTestData:
        pass
    else:
        pass
def inBetw():
    if UseTestData:
        pass
    else:
        pass
def inBetw():
    if UseTestData:
        pass
    else:
        pass
def inBetw():
    if UseTestData:
        pass
    else:
        pass
def inBetw():
    if UseTestData:
        pass
    else:
        pass
def inBetw():
    if UseTestData:
        pass
    else:
        pass
def inBetw():
    if UseTestData:
        pass
    else:
        pass
def inBetw():
    if UseTestData:
        pass
    else:
        pass
def inBetw():
    if UseTestData:
        pass
    else:
        pass
def inBetw():
    if UseTestData:
        pass
    else:
        pass

def oddencript(word):
    answ =''
    for index, item in enumerate(word):
        if index%2==0:
            answ+=item
    return answ
def leapYear(year_1,year_2):
    answ=[]
    for item in range(int(year_1),int(year_2)+1):
        if(item%4==0 and((item%100!=0) ^ (item%400==0))):
            answ.append(str(item)+" год високосный")
        else:
            pass
            answ.append(str(item) + " год невисокосный")
    return answ
def takeFromRange(word):
    pass