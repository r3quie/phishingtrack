from __future__ import print_function
# from datetime import date, timedelta
# import time
import xlwings as xw

def get_list(path, sheet):
    ws = xw.Book(path).sheets[sheet]

    v1 = ws.range("H1:H65").value

    # Removes None values
    res = [i for i in v1 if i is not None]

    print(res)

if __name__ == '__main__':
    get_list(input("Enter file name or path:\n"), input("Enter sheet name:\n"))
