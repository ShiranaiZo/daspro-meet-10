import ast
from modul_lol import *

def indonesia_merdeka(L):
    if isEmpty(L):
        return 0
    else:
        return ((max(first_List(L)) * 1000000) + indonesia_merdeka(tail_List(L)))

list_of_list = ast.literal_eval(input())
print(indonesia_merdeka(list_of_list))