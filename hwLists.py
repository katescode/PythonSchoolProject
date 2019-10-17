def HwLists():
    print('\n\nзадание "список"\n')
    OurBestStudents =TookTheList()
    print(OurBestStudents[0])
    print(OurBestStudents[2])
    print(OurBestStudents[-1])

def TookTheList():
    OurBestStudents = ['Александр','Константин',
                       'Мария','Диана',
                       'Алексей','Максим',
                       'Светлана','Арина',
                       'Серафим','Ад',
                       'Павел','Виктория',
                       'Елена','Галина','Вячеслав']
    return OurBestStudents