import json
import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mgb

with open('cricket_list.json', 'r') as cfp:
    cricket_list = json.load(cfp)


class cricket_importer:
    def __init__(self):
        self.error_type = 0
        self.name = None
        self.hp = None
        self.atk = None
        self.dfn = None
        self.root = tk.Tk()
        self.title = tk.Label()
        self.frm1 = tk.Frame(self.root)
        self.label1 = tk.Label(self.frm1)
        self.entry1 = tk.Entry(self.frm1)
        self.label2 = tk.Label(self.frm1)
        self.entry2 = tk.Entry(self.frm1)
        self.label3 = tk.Label(self.frm1)
        self.entry3 = tk.Entry(self.frm1)
        self.label4 = tk.Label(self.frm1)
        self.entry4 = tk.Entry(self.frm1)
        self.button = ttk.Button(self.root, command=lambda: self.information_input())
        self.title.pack()
        self.label1.grid(row=0, column=0)
        self.entry1.grid(row=0, column=1)
        self.label2.grid(row=1, column=0)
        self.entry2.grid(row=1, column=1)
        self.label3.grid(row=2, column=0)
        self.entry3.grid(row=2, column=1)
        self.label4.grid(row=3, column=0)
        self.entry4.grid(row=3, column=1)
        self.frm1.pack()
        self.button.pack()

    def is_int(self):
        try:
            pass
        except ValueError:
            self.error_type = 2

    def information_input(self):
        pass

    def main(self):
        pass


def cricket_list_write_in(name, hp, atk, dfn):
    global cricket_list
    t_list = [name, hp, atk, dfn]
    cricket_list[(len(cricket_list) + 1)] = t_list


def int_input(text):
    try:
        temp = int(input(text))
    except ValueError:
        int_input(text)
    else:
        return temp


def main():
    print('''
        模式选择
        1:新增蛐蛐
        2:查询蛐蛐列表
    ''')
    mode = input('请输入:')
    if mode == '1':
        cfp = open('cricket_list.json', 'w+')
        cricket_name = input()
        cricket_hp = int_input('a')
        cricket_atk = int_input('b')
        cricket_dfn = int_input('c')
        cricket_list_write_in(cricket_name, cricket_hp, cricket_atk, cricket_dfn)
        json.dump(cricket_list, cfp)
        cfp.close()
    elif mode == '2':
        for i in range(len(cricket_list)):
            i += 1
            print(i, end='   ')
            print(cricket_list[str(i)])
        os.system('pause')

    else:
        main()


if __name__ == '__main__':
    main()

else:
    print(cricket_list)
