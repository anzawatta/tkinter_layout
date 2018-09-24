import tkinter as tk
from common import BaseApplication

"""
Sample: scroll canvas.
"""


class Application(BaseApplication):

    def __init__(self, master=None):
        super().__init__(master)

        row_height = 50
        row_color = '#999'
        header = tk.Frame(master, bg=row_color, height=row_height)
        tk.Label(header, text="header", bg=row_color).pack()
        footer = tk.Frame(master, bg=row_color, height=row_height)
        tk.Label(footer, text="Footer", bg=row_color).pack()
        # don't adjust to fit the contents
        header.pack_propagate(0)
        footer.pack_propagate(0)

        # body setting
        body_height = self.winH - row_height - row_height
        body = tk.Frame(master, bg='#000', height=body_height)

        self.canvas = tk.Canvas(body, bg="#fff", width=self.winW)
        self.body = tk.Frame(self.canvas)
        # bind user changed widget
        self.body.bind("<Configure>", self.on_configure)

        self.scrollbar = tk.Scrollbar(body, orient=tk.VERTICAL, command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # put widget on canvas
        self.canvas.create_window((0, 0), window=self.body, anchor=tk.NW)

        # pack widgets
        header.pack(fill=tk.BOTH)

        body.pack(fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        footer.pack(fill=tk.BOTH)

        self.set_items()

    def set_items(self):
        for row in range(100):
            tk.Label(self.body, text="row %s" % row).pack(fill=tk.BOTH)

    def on_configure(self, event):
        print(event)
        # set body area size
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Canvas scroll example')
    app = Application(master=root)

    app.mainloop()
