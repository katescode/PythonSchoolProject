
#say is input message if void put "void"
#type can be 'str' for string, 'int' - int, 'flt'-float
#limit if void put 0 for string is len(srt)
    # for int is arrey[min, max] can look like arrey[min, 'less'] or arrey['more', max]


def EntrSmthg(type, message, limit):
    type = 'str'
    Say="un dia otro dia y otro"
    global say
    say = Say
    answ = Typer(type)
    print('answ end')


def Typer(type):
    switcher= {
            'str': EntrString,
            'int': EntrInt,
            'flt': EntrFloat}
    Answr = switcher.get(type,lambda:'invalide')
    Answr()






def EntrString():

    answ = input("string no limit ")

    return answ


def EntrFloat():
    answ = input("Float no limit")
    return  answ

def EntrInt():
    answ = input("Int no limit")
    return  answ

def EntrIntLimeted(say):
    answ = input("int limited",say)
    return  answ
