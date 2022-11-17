import ast
from modul_lol import *

def penjumlahan_prima(S):
    if isEmpty(S):
        return 0
    else:
        if isinstance(first_List(S), int):
            if  IsPrima(first_List(S)):
                return penjumlahan_prima(tail_List(S)) + first_List(S)
            else:
                return penjumlahan_prima(tail_List(S))
        else:
            return penjumlahan_prima(first_List(S)) + penjumlahan_prima(tail_List(S))

list_of_list = ast.literal_eval(input())
print(penjumlahan_prima(list_of_list))