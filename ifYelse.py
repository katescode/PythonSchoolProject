def IfYelse(UseTD):
    print('\n\nзадание "if-else"\n')
    global UseTestData
    UseTestData = UseTD

    inBetwIsWordShort()
    inBetwIsWordContinueF()
    inBetwinIsWordContinueAny()
    inBetwIsSqrtAreInteger()
    inBetwDayOfWeekByNumber()
    inBetwBmiConclusion()
    #UseTestData = False
    inBetwMarkMeaning()
    inBetwHowAboutRestaurant()
    inBetwIsDivBy235()


def inBetwIsWordShort():
    if UseTestData:
        word = 'ОченьДлинноеСлово'
        #word='1234567'
    else:
        word = input('Введите слово ')

    NotShortIfMoreThan = 7;
    answ = IsWordShort(len(word),NotShortIfMoreThan)
    if answ:
        print('Это слово короткое')
    else:
        print('Это слово длинное')
def inBetwIsWordContinueF():
    if UseTestData:
        word = 'ОченьДлинноеСлово'
        #word = 'фрелл'
    else:
        word = input('Введите слово ')
    IsRareIfContinue = 'ф'
    answ = IsWordContinue(word, IsRareIfContinue)
    if answ:
        print('Ого! Вы ввели редкое слово')
    else:
        print('Эх, это не очень редкое слово...')
def inBetwinIsWordContinueAny():
    if UseTestData:
        word = 'ОченьДлинноеСлово'
        #word = 'фрелл'
        Letter = 'и'
    else:
        word = input('Введите слово ')
        Letter = input('Введите букву (при введении нескольких будет взята первая) ')[0]

    answ = IsWordContinue(word, Letter)

    if answ:
        print('Выбранная буква есть в ведёном слове')
    else:
        print('Выбранной буквы нет в введёном слове')
def inBetwIsSqrtAreInteger():
    if UseTestData:
        #number = 169
        number = 9
    else:
        number = int(input('Введите число'))
    import math
    numsqrt =  math.sqrt(number)
    answ = IsThisNumAreInteger(numsqrt)
    if answ:
        print(int(numsqrt))
    else:
        print('Квадратный корень из',number, "не целое число")
def inBetwDayOfWeekByNumber():
    if UseTestData:
        number = 5
    else:
        ShouldEntrNumber = True
        while ShouldEntrNumber:
            number = int(input('Введите число от 1 до 7'))
            if (number > 0 and number < 8):
                ShouldEntrNumber = False
            else:
                print("Попытайтесь снова...")
    answ =DayOfWeekByNumber(number)
    print(answ)
def inBetwBmiConclusion():
    import hw1
    if UseTestData:
        hw1.UseTestDataChanger(True)
    else:
        hw1.UseTestDataChanger(False)
    bmi = hw1.inBetwBmi()
    #Else-if
    #answ = BmiConclusionByindex(bmi)

    # [от(включая), до(невкюлчая), вывод]
    BmiKeys = [['less', 18.5, 'Недостаточная масса тела'],
               [18.5, 25, 'Норма'],
               [25, 'more', 'Избыточная масса тела']]
    answ = DoubleArreyRangeFounder(BmiKeys, bmi)
    print(answ)
def inBetwMarkMeaning():
    if UseTestData:
        mark = 4                #int 1-10
    else:
        ShouldEntrNumber = True
        while ShouldEntrNumber:
            mark = int(input('Введите число от 1 до 10'))
            if (mark > 0 and mark < 11):
                ShouldEntrNumber = False
            else:
                print("Попытайтесь снова...")
    #[от(включая), до(невкюлчая), вывод]
    markKey = [[1,4,'неудовлетворительно'],
               [4,6,'удовлетворительно'],
               [6,8,'хорошо'],
               [8,11,'отлично']]

    answ = DoubleArreyRangeFounder(markKey,mark)
    print(answ)
def inBetwHowAboutRestaurant():
    if UseTestData:
        balance = 455
    else:
        balance = int(input('Введите количество оставшихся денег'))
    #[от(включая)'less' или число, до(невкюлчая) 'more' или число, вывод]
    balanceKeys = [['less', 2500, 'Придётся потерпеть'],
               [2500, 5000, 'Эх, только фастфуд'],
               [5000, 'more', 'Сегодня твой выбор-ресторан']]
    answ = DoubleArreyRangeFounder(balanceKeys, balance)
    print(answ)
def inBetwIsDivBy235():
    if UseTestData:
        number=452
    else:
        number = int(input('Введите число'))
    ArrDivBy = [2,3,5]
    ArrAnsw =['число делится без остатка на '+str(ArrDivBy[0]),
              'число делится без остатка на '+str(ArrDivBy[1]),
              'число делится без остатка на ' + str(ArrDivBy[2]),
              'число не делится ни на '+str(ArrDivBy[0])+', ни на '+str(ArrDivBy[1])+', ни на '+str(ArrDivBy[2])+' без остатка']
    answ = IsDivByFirstOf(ArrDivBy, ArrAnsw ,number)
    print(answ)

def IsWordShort(word,NotShortIfMoreThan):
    answ = False
    if word<=NotShortIfMoreThan:
        answ = True
    return bool(answ)
def IsWordContinue(word,letter):
    answ = False
    if letter in word:
        answ = True
    return answ
def IsThisNumAreInteger(number):
    answ = False
    if(number%1==0):
        int(number)
        answ = True


    return answ
def DayOfWeekByNumber(number):
    Dias = ['Понедельник','Вторник','Среда','Четверг','Пятница','Суббота','Воскресенье']
    answ = Dias[number-1]
    return answ
def DoubleArreyRangeFounder(doubArr,num):
    for item in range(len(doubArr)):
        From = doubArr[item][0]
        To = doubArr[item][1]
        if To=='more' or From == 'less':
            if To=='more' and From != 'less':
                if num > From:
                    Answ = doubArr[item][2]
                    return Answ;
            elif From =='less' and To!='more':
                if num < To:
                    Answ = doubArr[item][2]
                    return Answ;
            elif From == 'less' and To=='more':
                Answ = doubArr[item][2]
                return Answ;
        elif num>=From and num<To:
            Answ = doubArr[item][2]
            return Answ;



    raise Exception("Wrong num or doubArr in DoubleArreyRangeFounder");
def IsDivByFirstOf(ArrDivBy,ArrAnsw,number):
    for indx, num in enumerate(ArrDivBy):
        IsInt = number/num
        if IsThisNumAreInteger(IsInt):
            answ = ArrAnsw[indx]
            return answ
    answ = ArrAnsw[-1]
    return answ

