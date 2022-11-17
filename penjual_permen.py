import ast
from modul_lol import *

def penjual_permen(L):
    if isEmpty(L):
        return 0
    else:
        if is_atom(first_List(L)):
            if first_List(L) % 2 == 0:
                return penjual_permen(tail_List(L)) + (first_List(L) * 4000) 
            else:
                return penjual_permen(tail_List(L)) + (first_List(L) * 3000)
        else:
            if sum_int_list(first_List(L)) % 2 == 0:
                return (sum_int_list(first_List(L)) * 2000) + penjual_permen(tail_List(L))
            else:
                return (sum_int_list(first_List(L)) * 1000) + penjual_permen(tail_List(L))
                

list_of_list = ast.literal_eval(input())
print(penjual_permen(list_of_list))
