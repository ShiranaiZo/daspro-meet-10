import ast
from modul_lol import *

def hindari_monster(S, a):
    if isEmpty(S):
        return S
    else:
        if isinstance(first_List(S), int):
            if  a == '' or first_List(S) % int(a) == 0:
                return hindari_monster(tail_List(S), a)
            else:
                return konso_LoL(first_List(S), hindari_monster(tail_List(S), a))
        else:
            return konso_LoL(hindari_monster(first_List(S), a), hindari_monster(tail_List(S), a))
            
        
list_of_list = ast.literal_eval(input())
a = input()
print(hindari_monster(list_of_list, a))