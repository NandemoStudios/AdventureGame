import tkinter


class Window:

    def __init__(self, geometry):
        self.root = None
        self.canvas = None
        self.geometry = geometry
        self.root = tkinter.Tk()
        self.root.geometry(self.geometry)
        self.create_canvas()
        self.FPSDisplay = tkinter.Label(self.root, text="FPS: 0")
        self.FPSDisplay.pack()

    def create_canvas(self):
        self.canvas = tkinter.Canvas(self.root, height=600, width=1280)
        self.canvas.pack()

    def draw_ellipse(self, x, y, x2, y2, line_width, tags):
        circle = self.canvas.create_oval(x, y, x2, y2, width=line_width, tags=tags)
        return circle

    def draw_rectangle(self, x, y, width, height, line_width, tags):
        rectangle = self.canvas.create_rectangle(x, y, x+width, y+height, width=line_width, tags=tags)
        return rectangle

    def draw_line(self, x, y, x2, y2, line_width, tags):
        line = self.canvas.create_line(x, y, x2, y2, width=line_width, tags=tags)
        return line

    def Start(self):
        self.root.mainloop()
