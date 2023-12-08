import window


class Engine:
    def __init__(self, root_window, pawn_list, id_list):
        self.pawn_list = pawn_list
        self.id_list = id_list
        self.root_window = root_window

    def drawLoop(self):
        for entry in range(0, len(self.pawn_list)):
            # for each entry in the pawnlist, the game will find the correct ID, and draw it to the screen on set points
            if self.id_list[entry] == 1:
                self.root_window.draw_ellipse(20, 200, 5)
            if self.id_list[entry] == 2:
                self.root_window.draw_rectangle(20, 20, 20, 20, 5)

