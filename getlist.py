from __future__ import print_function
# from datetime import date, timedelta
# import time
import xlwings as xw

def get_list():
    ws = xw.Book("X:/dir/list.xlsx").sheets['list']

    v1 = ws.range("H7:H64").value

    # Removes None values
    res = [i for i in v1 if i is not None]

    print(res)

if __name__ == '__main__':
    get_list()