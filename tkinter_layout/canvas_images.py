import tkinter as tk
from common import BaseApplication

"""
Sample: set image and text on canvas.
"""


class Application(BaseApplication):

    def __init__(self, master=None):
        super().__init__(master)

        c = tk.Canvas(root, bg='#aaa', width=self.winW, height=self.winH)
        c.pack()

        # keep instance
        self.image1 = tk.PhotoImage(file='images/image1.png')
        c.create_image(0, 0, image=self.image1, anchor=tk.NW)

        # not show by GC
        image2 = tk.PhotoImage(file='images/image2.png')
        c.create_image(300, 0, image=image2, anchor=tk.NW)

        # set text by canvas coordinate
        # default anchor is CENTER
        x = 0
        c.create_text(x, 10, text="Text:x=%s(NW)" % x, anchor=tk.NW)
        c.create_text(x, 30, text="Text:x=%s(CENTER)" % x, anchor=tk.CENTER)
        c.create_text(x, 50, text="Text:x=%s(NE)" % x, anchor=tk.NE)


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Canvas example')
    app = Application(master=root)

    app.mainloop()
