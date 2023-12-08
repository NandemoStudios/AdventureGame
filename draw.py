import window


class Engine:
    def __init__(self, root_window, pawn_list, id_list):
        self.pawn_list = pawn_list
        self.id_list = id_list
        self.root_window = root_window

    def drawLoop(self):
        for entry in range(0, len(self.pawn_list)):
            # for each entry in the pawn-list, the game will find the correct ID, and draw it to the screen on set points
            if self.id_list[entry] == 1:
                self.root_window.draw_rectangle(self.pawn_list[entry][0],
                                                self.pawn_list[entry][1],
                                                self.pawn_list[entry][2],
                                                self.pawn_list[entry][3],
                                                self.pawn_list[entry][4])
            if self.id_list[entry] == 2:
                self.root_window.draw_ellipse(self.pawn_list[entry][0],
                                              self.pawn_list[entry][1],
                                              self.pawn_list[entry][2],
                                              self.pawn_list[entry][3],
                                              self.pawn_list[entry][4])
            if self.id_list[entry] == 3:
                self.root_window.draw_line(self.pawn_list[entry][0],
                                           self.pawn_list[entry][1],
                                           self.pawn_list[entry][2],
                                           self.pawn_list[entry][3],
                                           self.pawn_list[entry][4])

