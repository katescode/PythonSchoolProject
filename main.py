import hw1
import hwLists
import ifYelse
import loops
import defs
import pPandas
import webPandas

def main():
    UseTestData = True
    if UseTestData:
        print("используются тестовые данные")
    
    #hw1.Hw1(UseTestData)            # задание 3
    #hwLists.HwLists()               # задание "список"
    #ifYelse.IfYelse(UseTestData)    # задание "if-else"
    #loops.Loops(UseTestData)        # задание "циклы"
    #defs.Defs(UseTestData)          # задание "функции"
    #pPandas.PPandas(UseTestData)    # задание "pandas"
    webPandas.wPandas()              # задание "pandas титаник"



if __name__ == '__main__':
    main()
