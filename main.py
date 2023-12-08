import tkinter


class Window:

    def __init__(self, geometry):
        self.root = None
        self.canvas = None
        self.geometry = geometry
        self.root = tkinter.Tk()
        self.root.geometry(self.geometry)
        self.create_canvas()
        self.draw_ellipse(20, 100, 5)
        self.draw_ellipse(120, 200, 5)
        self.root.mainloop()

    def create_canvas(self):
        self.canvas = tkinter.Canvas(self.root, height=720, width=1280)
        self.canvas.pack()

    def draw_ellipse(self, x, y, line_width):
        circle = self.canvas.create_oval(x, y, y, x, width=line_width)
        return circle


newWindow = Window("1280x720")
