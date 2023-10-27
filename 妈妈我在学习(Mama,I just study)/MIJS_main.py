import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mgb
import os
import keyboard
import win32api
import sys
from PIL import ImageTk

screensize_X = win32api.GetSystemMetrics(0)
screensize_Y = win32api.GetSystemMetrics(1)
mode = 0
debug = True


class Starter:
    def __int__(self):
        pass

    def main(self):
        pass


# StudyThingsDisPlayModel
class STDM:
    def __init__(self):
        self.root = tk.Tk()
        self.image = None
        self.video = None
        self.audio = None
        self.asset_import()
        self.root.overrideredirect(True)
        self.root.geometry()
        keyboard.add_hotkey('ctrl+shift+a',self.cloak)
        self.cloak_status = True
        self.M_frm = None
        self.asset_prepare()

    def asset_import(self):
        if mode == 0:
            self.image = ImageTk.PhotoImage(file=r"C:\Users\ds2006\Pictures\WallpaperLib\do3_-hkmwytq1316890.jpg")

    def asset_prepare(self):
        if mode == 0:
            self.M_frm = tk.Canvas(self.root, width=screensize_X, height=screensize_Y)
            self.M_frm.create_image((int(screensize_X // 2)), (int(screensize_Y // 2)), image=self.image,
                                    anchor='center')
            self.M_frm.pack()

    def cloak(self):
        if self.cloak_status is False:
            self.root.withdraw()
            self.cloak_status = True
        elif self.cloak_status is True:
            self.root.wm_deiconify()
            self.cloak_status = False

    def main(self):
        self.root.mainloop()


def pic_choose():
    pass


def load():
    try:
        config = open('config.json', 'r')
        pass
    except FileNotFoundError:
        config = open('config.json', 'w')
        editor = Starter()
        editor.main()

def fvck():
    quit('sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss')

def main():
    a = STDM()
    a.main()



if __name__ == '__main__':
    main()
