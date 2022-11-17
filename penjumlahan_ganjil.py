import ast
from modul_lol import *

def penjumlahan_ganjil(S):
    if isEmpty(S):
        return 0
    else:
        if isinstance(first_List(S), int):
            if  first_List(S) % 2 != 0:
                return penjumlahan_ganjil(tail_List(S)) + first_List(S)
            else:
                return penjumlahan_ganjil(tail_List(S))
        else:
            return penjumlahan_ganjil(first_List(S)) + penjumlahan_ganjil(tail_List(S))

list_of_list = ast.literal_eval(input())
print(penjumlahan_ganjil(list_of_list))
