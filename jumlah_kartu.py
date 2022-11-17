import ast
from modul_lol import *

def jumlah_kartu(L):
    if isEmpty(L):
        return 0
    else:
        if is_atom(first_List(L)):
            return jumlah_kartu(tail_List(L)) + 1
        else:
            return jumlah_kartu(first_List(L)) + jumlah_kartu(tail_List(L))

list_of_list = ast.literal_eval(input())
print(jumlah_kartu(list_of_list))
[[10, 9, [8, [7, 3], 2, [1, 2]], 4], 5]
