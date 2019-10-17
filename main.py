import hw1
import hwLists
import ifYelse
import entrData
from inBetwWrapper import *

def main():
    isItTest = True
    inBetwWarp = InBetwWrapper()
    inBetwWarp.set_isItTest(isItTest)
    inBetwWarp.TodayYourNameIs()
    #answ = entrData.EntrSmthg('say','str',0)
    #print(answ)

    hw1.Hw1(isItTest,inBetwWarp)            # задание 3
    #hwLists.HwLists()               # задание "список"
    #ifYelse.IfYelse(isItTest)    # задание "if-else"




#----------------------------------------------------------------------------
# def a_decorator_passing_arguments(function_to_decorate):
#     def a_wrapper_accepting_arguments(arg1, arg2):
#         print("Смотри, что я получил:", arg1, arg2)
#         function_to_decorate(arg1, arg2)
#     return a_wrapper_accepting_arguments
#
#
# @a_decorator_passing_arguments
# def print_full_names(first_name, last_name):
#     print("Меня зовут", first_name, last_name)
#----------------------------------------------------------------------------


if __name__ == '__main__':
    main()