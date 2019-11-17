def Loops(UseTD):
    print('\n\nзадание "циклы"\n')
    global UseTestData
    UseTestData = UseTD

    inBetwOddEncript()
    inBetwLeapYear()
    inBetwRuVowels()
    inBetwLetterInName()
    inBetwOddDivBy35()

    inBetwSqr3For1to10()
    inBetwThisNumberCanDivBy()
    inBetwThisNumbersCanDivBy()
    inBetwCountLastFibonacci()
    inBetwMultiplyLine()

    inBetwMaxDivForNumbers()
    inBetwWichOutABC()
    doYouLikePython()
    inBetwIsSimpleNumber()
    inBetwNoRuVowelsOnEvenPosition()

    inBetwCountTimeForBankDeposit()
    inBetwLiftOverWeight()
    inBetwYouDieIn()
    inBetwSpendingMoney()
    inBetwWaterBot()



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
def inBetwCountLastFibonacci():
    if UseTestData:
        n=10
    else:
        n = int(input('введите число из ряда Фибоначчи'))
    answ = countFibonacci(n)
    print(answ[-1])
def inBetwMultiplyLine():
    if UseTestData:
        number = 15
    else:
        number =int(input('введите число'))
    answ = multiplyTable(number, ['',' X ',' = '],[1,10])
    print(answ)

def inBetwMaxDivForNumbers():
    if UseTestData:
        num_1 = 1812
        num_2 = 2500
    else:
        num_1 = int(input('введите первое число'))
        num_2 = int(input('введите второе'))
    answ = maxDivForNumbers(num_1, num_2)
    if str(answ) != str([1]) and answ != None:
        print(answ)
    else:
        print("Общих делителей не найдено")
def inBetwWichOutABC():
    if UseTestData:
        string='абстракция'
    else:
        string = input('введитие строку')
    outRange =['а','б','в']
    answ = takeOutRange(string,outRange)
    print(answ)
def doYouLikePython():
    for i in range(0,5):

        if UseTestData:
            userSaid = "Нет"
        else:
            userSaid = input('Любители вы питон')
        if userSaid =="Да":
            print("Это отлично")
            break
        elif userSaid =="Нет":
            if i == 4:
                print("Это безнадёжно")
                break
            print("Увы, это неправильный ответ")
def inBetwIsSimpleNumber():
    if UseTestData:
        number=173
    else:
        number = int(input('введите число'))
    if len(ThisNumberCanDivBy(number)) == 2:
        print("Простое")
    else:
        print("Не является простым")
def inBetwNoRuVowelsOnEvenPosition():
    if UseTestData:
        string = 'прелестная строка'
        #string = "пока"
    else:
        string = input('введитие строку')
    RuVowels = ['а','о','и','у','я','ю','ё','е']
    answ = NoOneOnEvenPosition(string,RuVowels)
    if answ:
        print("Какая хорошая строка!")
    else:
        print("Строка мне не нравится!")

def inBetwCountTimeForBankDeposit():
    if UseTestData:
        Y = 170000
        Z = 1000000
    else:
        num_1 = int(input('введите размер вклада'))
        num_2 = int(input('введите желаемая сумма '))
    answ = countTimeForBankDeposit(Y, Z, 10)
    print(str(answ))
def inBetwLiftOverWeight():
    if UseTestData:
        weight = 77
    else:
        weight =input('вес входящих')
    nomore = 400
    answ = MoreThanFor(nomore, weight)
    print('Перевес',str(answ),'кг')
def inBetwYouDieIn():
    if UseTestData:
        current_health=500
        attack=80
    else:
        current_health=input('введите здоровье')
        attack=input('введите силу атаки')
    answ = LessThanFor(current_health,attack)
    print(str(answ))
def inBetwSpendingMoney():
    if UseTestData:
        balance = 10000
        spent = 2800
    else:
        balance = input('введите баланс')
        spent = input('введите расходы за раз')
    answ = arrLessThan(balance,spent)
    for stillHave in answ:
        if stillHave>0:
            print(str(stillHave))
        else:
            print("Слишком большие расходы")
def inBetwWaterBot():
    if UseTestData:
        value = 1000
        firstTime = 5
    else:
        value = input('введите объем')
        firstTime = input('введите количество литров при первом заходе')
    answ = MoreThanMultyplyFor(value,firstTime)
    print(str(answ))


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
    for div in divs:
        for index,fED in enumerate(forEachDivs):
            have = False
            for thediv in div:
                if fED == thediv:
                    have = True
            if not have:
                forEachDivs[index]==0
                answ.remove(fED)
                notAllowd.append(fED)
            else:
                if (fED not in answ) and (fED not in notAllowd):
                    answ.append(fED)
    return answ
def countFibonacci(numero):
    fib = []
    for index, num in enumerate(range(1,int(numero)+1)):
        if index>1:
            fib.append(fib[index-2]+fib[index-1])
        else:
            fib.append(1)
    return fib
def multiplyTable(number, printStr,rng):
    rang=range(rng[0],rng[1]+1)
    answ = ''
    for r in rang:
        answ+=printStr[0]+str(number)+printStr[1]+str(r)+printStr[2]+str(number*r)+"\n"

    return answ
def maxDivForNumbers(*nums):
    answ = None
    allDiv = ThisNumbersCanDivBy(*nums)
    if len(allDiv)>1:
        answ=max(allDiv)
    return answ
def takeOutRange(word, range):
    answ = ''
    for char in word:
        if char not in range:
            answ+=char
    return answ
def NoOneOnEvenPosition(word, range):
    answ = True
    for index,char in enumerate(word):
        if  IsNumberDivBy(index,2):
            if char in range:
                answ = False
                break
    return answ
def countTimeForBankDeposit(depositSum, richSum, percent):
    answ = 0
    while(depositSum<richSum):
        depositSum+=depositSum*percent/100
        answ+=1
    return answ
def MoreThanFor(maxpoint, add):
    still = 0
    while(still<maxpoint):
        still+=add
    answ = still-maxpoint
    return answ
def LessThanFor(haveNow,loose):
    answ = 0
    while(0<haveNow):
        haveNow-=loose
        if 0<haveNow:
            answ += 1
    return answ
def arrLessThan(haveNow,loose):
    answ = []
    while(0<haveNow):
        haveNow-=loose
        answ.append(haveNow)
    return answ
def MoreThanMultyplyFor(maxpoint, add):
    still = 0
    addnow=add
    answ = 0
    while(still<maxpoint):
        still+=addnow
        addnow+=add
        answ+=1
    return answ

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