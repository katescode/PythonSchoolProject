def Defs(UseTD):
    print("\nзадание 'функции'\n")
    global UseTestData
    UseTestData = UseTD
    #UseTestData = False

    inBtwSquare()
    inBtwSum2()
    inBtwPower()
    inBtwGet_median()
    inBtwAvg_order()  # ????????
    inBtwRurEur()


def inBtwSquare():
    if UseTestData:
        num = 20
    else:
        num = int(input('введите число'))
    square_result = square(num)
    print(square_result)

def inBtwSum2():
    if UseTestData:
        num1 = 42
        num2 = 73
    else:
        num = int(input('введите первое число'))
        num = int(input('введите второе число'))
    answ = sum_2(num1, num2)
    print(answ)

def inBtwPower():
    if UseTestData:
        num = 2
        inPow = 3
    else:
        num = int(input('введите число'))
        inPow = int(input('введите степень'))
    answ = power(num, inPow)
    print(answ)

def inBtwGet_median():
    numList = []
    if UseTestData:
        numList = [5, 2, 1, 3, 4]
    else:
        num = int(input('введите количество чисел'))
        while (num > 0):
            num = num - 1
            numList.append(int(input('введите число')))
    answ = get_median(numList)
    print(answ)

def inBtwAvg_order():
    user_db = [{'orders': 12}, {'orders': 30}, {'orders': 45}]
    avg_order(user_db)

def inBtwRurEur():
    ticket_bd = [{'price': 400}, {'price': 200}, {'price': 150}]
    guide_bd = [{'price': 50}, {'price': 40}]
    snack_bd = [{'price': 100}, {'price': 95}, {'price': 150}]
    curency = 70
    answ = RurEur(ticket_bd, guide_bd, snack_bd, curency)
    print(answ)




def square(num):
    answ = pow(num, 2)
    return answ

def sum_2(num1, num2):
    answ = num1 + num2
    return answ

def power(num, inPow):
    answ = pow(num, inPow)
    return answ

def get_median(numList):
    sortedNumList = sort(numList)
    count = len(sortedNumList)
    isOdd = count % 2
    if isOdd == 0:
        med = count / 2
        mediana = (sortedNumList[med] + sortedNumList[med + 1]) / 2

    else:
        med = (count // 2) + 1
        mediana = sortedNumList[med]
    return mediana

def RurEur(*args):
    curency = args[-1]
    count = len(args) - 1
    while count > 0:
        count = count - 1
        for price in args[count]:
            answ = price['price'] * curency

def sort(numList):
    count = len(numList)
    for i in range(count):
        for j in range(count - i - 1):
            if numList[j] > numList[j + 1]:
                temp = numList[j]
                numList[j] = numList[j + 1]
                numList[j + 1] = temp
    answ = numList
    return answ

def avg_order(user_db):
    order_sum = sum([user['orders'] for user in user_db])
    orders_per_user = order_sum / len(user_db)
    print(orders_per_user)

