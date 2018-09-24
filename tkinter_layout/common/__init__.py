import tkinter as tk

"""
Base 
"""


class BaseApplication(tk.Frame):
    winW = 640
    winH = 520

    def __init__(self, master=None):
        super().__init__(master)

        self.set_window_position()

    def set_window_position(self):
        posL = int((self.master.winfo_screenwidth() - self.winW) / 2)
        posT = int((self.master.winfo_screenheight() - self.winH) / 2)
        self.master.geometry('{}x{}+{}+{}'.format(self.winW, self.winH, posL, posT))
