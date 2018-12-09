import tkinter as tk
from common import BaseApplication

"""
Sample: scroll canvas width image.
"""


class Application(BaseApplication):

    def __init__(self, master=None):
        super().__init__(master)

        self.items = []

        row_height = 50
        row_color = '#999'
        header = tk.Frame(master, bg=row_color, height=row_height)
        tk.Label(header, text="header", bg=row_color).pack()
        footer = tk.Frame(master, bg=row_color, height=row_height)
        tk.Label(footer, text="Footer", bg=row_color).pack()
        # don't adjust to fit the contents
        header.pack_propagate(0)
        footer.pack_propagate(0)

        # buttons
        btn_area = tk.Frame(header, bg=row_color, width=200, height=row_height / 2)
        btn_area.pack_propagate(0)
        btn_add = tk.Button(btn_area, text='add')
        btn_add['command'] = self.add_item
        btn_del = tk.Button(btn_area, text='del')
        btn_del['command'] = self.delete_item

        # body setting
        body_height = self.winH - row_height - row_height
        body = tk.Frame(master, bg='#000', height=body_height)

        self.canvas = tk.Canvas(body, bg="#fff", width=self.winW)
        self.body = tk.Frame(self.canvas)
        # bind user changed widget
        self.body.bind("<Configure>", self.on_configure)

        self.scrollbar = tk.Scrollbar(body, orient=tk.VERTICAL, command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # canvas background image
        self.master.todo_area = tk.PhotoImage(file='images/image3.png')
        self.drawn_bg_height = 0

        # put widget on canvas
        self.canvas.create_window((0, 0), window=self.body, anchor=tk.NW)

        # pack widgets
        header.pack(fill=tk.BOTH)
        btn_area.pack()
        btn_add.pack(side=tk.LEFT)
        btn_del.pack(side=tk.RIGHT)

        body.pack(fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        footer.pack(fill=tk.BOTH)

        self.set_items()

    def set_items(self):
        for row in range(50):
            item = tk.Label(self.body, text="row %s" % row)
            item.pack(fill=tk.BOTH)
            self.items.append(item)

    def draw_scroll_bg(self, target_height):
        image_height = self.master.todo_area.height()

        if self.drawn_bg_height - image_height > target_height and len(self.canvas.find_withtag('bg')) > 0:
            self.canvas.delete(self.canvas.find_withtag('bg')[-1])
            self.drawn_bg_height -= image_height
            print('del canvas_bg_ids: ', self.canvas.find_withtag('bg'))

        while self.drawn_bg_height < target_height:
            self.canvas.create_image(0, self.drawn_bg_height, image=self.master.todo_area, anchor=tk.NW, tags='bg')
            self.drawn_bg_height += image_height
            print('add canvas_bg_ids: ', self.canvas.find_withtag('bg'))

        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_configure(self, event):
        print(event)
        # set body area size
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

        self.draw_scroll_bg(event.height)

    def add_item(self):
        item = tk.Label(self.body, text="row add")
        item.pack(fill=tk.BOTH)
        self.items.append(item)

    def delete_item(self):

        for item in self.items:
            print(item, type(item))
            item.destroy()
            self.items.pop(0)
            break


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Canvas scroll example')
    root.resizable(width=False, height=False)
    app = Application(master=root)

    app.mainloop()
