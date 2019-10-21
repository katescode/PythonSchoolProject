import hw1
import hwLists
import ifYelse
import loops

def main():
    UseTestData = True
    if UseTestData:
        print("используются тестовые данные")

    hw1.Hw1(UseTestData)            # задание 3
    hwLists.HwLists()               # задание "список"
    ifYelse.IfYelse(UseTestData)    # задание "if-else"
    loops.Loops(UseTestData) # задание "циклы"


if __name__ == '__main__':
    main()