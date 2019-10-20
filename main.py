import hw1
import hwLists
import ifYelse
import entrData
import loops

def main():
    UseTestData = True
    if UseTestData:
        print("используются тестовые данные")

    # answ = entrData.EntrSmthg('say','str',0)
    # print(answ)
    # hw1.Hw1(UseTestData)            # задание 3
    # hwLists.HwLists()               # задание "список"
    # ifYelse.IfYelse(UseTestData)    # задание "if-else"
    loops.Loops(UseTestData) # задание "циклы"


if __name__ == '__main__':
    main()