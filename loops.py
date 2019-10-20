def Loops(UseTD):
    print('\n\nзадание "циклы"\n')
    global UseTestData
    UseTestData = UseTD
    #inBetwOddEncript()
    #inBetwLeapYear()
    #inBetwRuVowels()
    #inBetwLetterInName()
    #inBetwOddDivBy35()
    #inBetwSqr3For1to10()
    #inBetwThisNumberCanDivBy()
    #inBetwThisNumbersCanDivBy()  #----can do better-----



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

    divBy=[3,5]
    answ = oddDivBy(num_1,num_2, divBy)
    print(answ)

def inBetwSqr3For1to10():
    fromto = range(1,11)
    paws =[1,2,3]
    answ = pawToStringForRange(fromto,paws)
    print(answ)
def inBetwThisNumberCanDivBy():
    if UseTestData:
        number=84
    else:
        number = int(input('введите число'))
    answ = ThisNumberCanDivBy(number)
    #print(answ)
    print(*answ, sep = " ")
def inBetwThisNumbersCanDivBy():
    if UseTestData:
        num_1 = 12
        num_2 = 38
    else:
        num_1 = int(input('введите первое число'))
        num_2 = int(input('введите второе'))
    answ = ThisNumbersCanDivBy(num_1,num_2)

    if str(answ) !=str([1]) and answ!=None:
        print(answ)

def inBetw():
    if UseTestData:
        n=10
    else:
        n = int(input('введите число из ряда Фибоначчи'))
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

def oddEncript(word):
    answ =''
    for index, item in enumerate(word):
        if IsNumberDivBy(index,2):
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
def IsNumberDivBy(number, div):
    answ = False
    if number % div == 0:
        answ = True
    return answ
def oddDivBy(num_1,num_2, divBy):
    answ = ''
    if num_1<0 or num_2<num_1:
        return 'Введен не верный диапазон чисел'
    for num in range(num_1,num_2+1):
        if not IsNumberDivBy(num,2):
            for divby in divBy:
                if IsNumberDivBy(num,divby):
                    answ+=str(num)+ ' '
                    break
    return answ
def pawToStringForRange(ranges, pows):
    answ = ''
    for num in ranges:
        #print(num)
        for pws in pows:
            answ+=str(pow(num,pws))+' '
        answ += '\n'
    return answ
def ThisNumberCanDivBy(number):
    answ=[]
    for div in range(1, number+1):
        if IsNumberDivBy(number,div):
            answ.append(div)
    return answ
def ThisNumbersCanDivBy(*numbers):#can do better
    divs = []
    for num in numbers:
        divs.append(ThisNumberCanDivBy(num))
    forEachDivs=divs[0]
    answ = []
    notAllowd = []
    print(divs)
    for div in divs:
        for index,fED in enumerate(forEachDivs):
            have = False
            for thediv in div:
                if fED == thediv:
                    have = True
                    print(str(fED)+" "+str(thediv))
            if not have:
                forEachDivs[index]==0
                answ.remove(fED)
                notAllowd.append(fED)
                print(forEachDivs[index],'hi')
            else:
                if (fED not in answ) and (fED not in notAllowd):
                    answ.append(fED)
    return answ
def countFibonacci(numero):

    pass

# def inBetwcheckTeory():
#     ThisNumbersCanDivBy(10,5,70,30,60,40)
#
# def checkTeory(*numbers):
#     divs = []
#     for num in numbers:
#         divs.append(ThisNumberCanDivBy(num))
#     forEachDivs=divs[0]
#     for div in divs:
#         for index,fED in enumerate(forEachDivs):
#             have = False
#             for thediv in div:
#                 if fED == thediv:
#                     have = True
#             if not have:
#                 del forEachDivs[index]
#     print(forEachDivs)