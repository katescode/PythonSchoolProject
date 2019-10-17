class InBetwWrapper():

    def __init__(self):
        self.isItTest = False
        self.TestDataList = {}

    def set_isItTest(self, changeTo):
        self.isItTest = changeTo

    def get_isItTest(self):
        isTestOn = self.isItTest
        return isTestOn

    def set_testData(self,funcName, data):
        self.TestDataList[funcName] = data
        datas=self.TestDataList[funcName]
        print(datas)

    def TakeTheDatas(self,allData):
        if self.isItTest:
            print("используются тестовые данные")
            testdata=allData[0]#self.TestDataList[funcKey]
            return testdata
        else:

            return "input it by yourself"


    def inBetwin(*args, **kwargs):
        def outer(func):
            def wrapit(self):
                allFuncData = args
                dataArr = InBetwWrapper.TakeTheDatas(self, allFuncData)
                results = func(self,dataArr)

                print(results)
            return wrapit
        return outer

    @inBetwin(['test', 'test', 'data'],{'str':[1,0]},)
    def wrapped(self,args):
        print("it was wrapped", args)

                        #[type, message, limit, count],[]
    @inBetwin(['Андрей'],['str','Введите ваше имя',0,1],['Сегодня Вас зовут '])
    def TodayYourNameIs(self,name):
        answ = name[0]
        return answ
