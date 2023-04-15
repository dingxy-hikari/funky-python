import json
import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mgb

with open('cricket_list.json', 'r') as cfp:
    cricket_list = json.load(cfp)


class cricket_importer:
    def __init__(self):
        self.help_text = '''
        蛐蛐名字：新创建蛐蛐的名字（接受字符串）
        蛐蛐生命值：新创建蛐蛐的生命值（仅接受整数输入）
        蛐蛐攻击力；新创建蛐蛐的攻击力（仅接受整数输入）
        蛐蛐防御力：新创建蛐蛐的防御力（仅接受整数输入）
        '''
        self.error_type = None
        self.name = None
        self.hp = None
        self.atk = None
        self.dfn = None
        self.root = tk.Tk()
        self.title = tk.Label(self.root, text='自定义蛐蛐生成')
        self.frm1 = tk.Frame(self.root)
        self.label1 = tk.Label(self.frm1, text='蛐蛐名字:', width=15)
        self.entry1 = tk.Entry(self.frm1, width=15)
        self.label2 = tk.Label(self.frm1, text='蛐蛐生命值(整数):', width=15)
        self.entry2 = tk.Entry(self.frm1, width=15)
        self.label3 = tk.Label(self.frm1, text='蛐蛐攻击力(整数):', width=15)
        self.entry3 = tk.Entry(self.frm1, width=15)
        self.label4 = tk.Label(self.frm1, text='蛐蛐防御力(整数:)', width=15)
        self.entry4 = tk.Entry(self.frm1, width=15)
        self.frm2 = tk.Frame(self.root)
        self.btn1 = ttk.Button(self.frm2, text='帮助!', command=lambda: mgb.showinfo('提示', self.help_text), width=15)
        self.btn2 = ttk.Button(self.frm2, text='生成!', command=lambda: self.information_input(), width=15)
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
        self.btn1.grid(row=0, column=0)
        self.btn2.grid(row=0, column=1)
        self.frm2.pack()

    def is_int(self, var):
        try:
            output = int(var)
        except ValueError:
            self.error_type = 2
            return None
        else:
            return output

    def information_input(self):
        self.name = self.entry1.get()
        if self.name == '':
            self.error_type = 1
        self.hp = self.is_int(self.entry2.get())
        self.atk = self.is_int(self.entry3.get())
        self.dfn = self.is_int(self.entry4.get())

        if self.error_type is not None:
            if self.error_type == 1:
                mgb.showwarning()
            elif self.error_type == 2:
                mgb.showwarning()
            else:
                mgb.showwarning()

        if self.error_type is None:
            cricket_list_write_in(self.name, self.hp, self.atk, self.dfn)
            lfp = open('cricket_list.json', 'w+')
            json.dump(cricket_list, lfp)
            lfp.close()

    def main(self):
        self.root.mainloop()


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


def create_basic_json():
    basic_dict = {'1': ['青绿士兵', 10, 10, 10, ],
                  '2': ['沙色刀客', 9, 13, 8],
                  '3': ['大胖子  ', 13, 4, 13],
                  '4': ['铁翅将军', 8, 11, 11, ],
                  '5': ['钢角司令', 7, 14, 19],
                  '6': ['金银贵人', 20, 5, 5],
                  '7': ['黑色肃杀', 10, 12, 8],
                  '8': ['疾驱之火', 7, 13, 10, ], }

    with open('cricket_list.json', 'w') as bfp:
        json.dump(basic_dict, bfp)


def main():
    print('''
        模式选择
        1:新增蛐蛐
        2:查询蛐蛐列表
    ''')
    mode = input('请输入:')
    if mode == '1':
        a = cricket_importer()
        a.main()
    elif mode == '2':
        print('1  2  3  4  5')
        for i in range(len(cricket_list)):
            i += 1
            print(i, end=' ')
            print(cricket_list[str(i)][0], end=' ')
            print(cricket_list[str(i)][1], end=' ')
            print(cricket_list[str(i)][2], end=' ')
            print(cricket_list[str(i)][3])

        os.system('pause')
    else:
        main()


if __name__ == '__main__':
    main()

else:
    for i in range(len(cricket_list)):
        i += 1
        print(i, end=' ')
        print(cricket_list[str(i)][0], end=' ')
        print(cricket_list[str(i)][1], end=' ')
        print(cricket_list[str(i)][2], end=' ')
        print(cricket_list[str(i)][3])
