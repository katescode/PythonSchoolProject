import pandas as pd

def PPandas(UseTD):
    print("\nзадание 'pandas'\n")
    global UseTestData
    UseTestData = UseTD
    #inBetwNewSeriesThree()
    #inBetwAddIndex()
    #inBetwDateIndexDate()
    #InBetwWethMoscow()
    #InBetwWethDifVoronjMsk()
    #inBetwNumeroTwo()
    #inBetwMidDiff()

    #inBetwCreateDf()
    #inBetwDfColumnOneByOne()
    #inBewThroughPoint()
    #inBetwMidDiffThroughtPoint()
    inBetwAddDiffRow()

def inBetwNewSeriesThree():
    ser = [5, 10, 11, 15, 17, 20]
    series = NewSeries(ser)
    answ = series[3]
    print(answ)
    answ = series[4]
    print(answ)
def inBetwAddIndex():
    ser = [5, 10, 11, 15, 17, 20]
    index = [ 'a', 'b', 'c', 'd', 'e', 'f']
    seriesWIndex = addIndexAndSeries(ser,index)
    print(seriesWIndex['d'])
    print(seriesWIndex['e'])
    print(seriesWIndex['f'])
def inBetwDateIndexDate():
    index = ["20.10.2019","21.10.2019","22.10.2019",
             "23.10.2019","24.10.2019","25.10.2019","26.10.2019"]
    indexed = addIndex(index)
    return indexed
def InBetwWethMoscow():
    answ = WethMoscow()
    print(answ["22.10.2019"])
def InBetwWethDifVoronjMsk():
    answ = DifVoronjMsk()
    print(answ)
def inBetwNumeroTwo():
    answ = DifVoronjMsk()
    print(answ[2])
def inBetwMidDiff():
    answ = DifVoronjMsk()
    print(answ.median())

def inBetwCreateDf():
    answ= CreateDf()
    print(answ)
def inBetwDfColumnOneByOne():
    answ= CreateDf()
    print(answ[0])
    print(answ[1])
def inBewThroughPoint():
    answ= CreateDf()
    a=answ.take([1],axis=1)
    print(a)
def inBetwMidDiffThroughtPoint():
    answ= CreateDf()
    a=answ[0]-answ[1]
    print(a)
def inBetwAddDiffRow():
    answ = CreateDf()
    #a = answ[0] - answ[1]
    answ[2]=answ[0] - answ[1]
    print(answ)

def WethMoscow():
    indx = inBetwDateIndexDate()
    sers = [25, 100, 85, 10, 0, 0, 10]
    answ = addSeries(sers, indx)
    return answ
def WethVoronj():
    indx = inBetwDateIndexDate()
    sers = [30, 70, 10, 30, 25, 100, 0]
    answ = addSeries(sers, indx)
    return answ
def NewSeries(ser):
    data = ser
    series = pd.Series(ser)
    return series
def addIndexAndSeries(seriess,indexx):
    seriesWIndex =pd.Series(seriess,index=indexx)
    return seriesWIndex
def addSeries(ser,indx):
    seriesWIndex = pd.Series(ser,index=indx.index)
    return seriesWIndex
def addIndex(ind):
    whIndex =pd.Series(index=ind)
    return whIndex
def DifVoronjMsk():
    msk = WethMoscow()
    vrnj = WethVoronj()
    diff = []
    idx = 0
    for val in msk:
        diff.append(val-vrnj[idx])
        idx+=1
    sDiff=addSeries(diff,msk)
    return sDiff

def CreateDf():
    msk = WethMoscow()
    vrnj = WethVoronj()
    list_of_series = [msk, vrnj]
    df = pd.DataFrame(list_of_series).transpose()
    return df