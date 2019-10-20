def Loops(UseTD):
    print('\n\nзадание "циклы"\n')
    global UseTestData
    UseTestData = UseTD
    #inBetwOddEncript()
    #inBetwLeapYear()
    #inBetwRuVowels()
    #inBetwLetterInName()


def inBetwOddEncript():
    if UseTestData:
        word = 'подшипник'
    else:
        word =input('введите слово')

    answ = oddEncript(word)
    print(answ)
def inBetwLeapYear():
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
        word = 'Зимушка-зима'
    else:
        word = input('введите слово')
    RuVowels = ['а','о','и','у','я','ю','ё','е']
    answ = takeFromRange(word,RuVowels)
    print(answ)
def inBetwLetterInName():
    if UseTestData:
        name = 'Сергей'
    else:
        name = input('Введите ваше имя')
    printStr = ['Буква','в этом имени -','']
    answ = indexAndItem(name, printStr)
    print(answ)
def inBetwOddDivBy35():
    if UseTestData:
        num_1 = 25
        num_2 = 45
    else:
        num_1 = int(input('введите первое число'))
        num_2 = int(input('введите второе'))
    answ = ''
    print(answ)
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

def oddEncript(word):
    answ =''
    for index, item in enumerate(word):
        if IsOddNumber(index):
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
def takeFromRange(word, range):
    answ = ''
    for char in word:
        if char in range:
            answ+=char
    return answ
def indexAndItem(name, printStr):
    answ = ''
    for index,char in enumerate(name):
        answ+= str(printStr[0]+" "+str(index+1)+" "+printStr[1]+" "+char+" "+printStr[2]+'\n')
    return answ
def IsOddNumber(number):
    answ = False
    if number % 2 == 0:
        answ = True
    return answ
def oddDivBy():
    pass