import tkinter

import window


class Engine:
    def __init__(self, root_window, pawn_list, id_list):
        self.pawn_list = pawn_list
        self.id_list = id_list
        self.root_window = root_window

    def drawLoop(self, pawn_list):
        for entry in range(0, len(pawn_list)):
            ''' for each entry in the pawn-list, the game will find the correct ID, and draw it to the screen on set 
            points'''
            if self.id_list[entry] == 1:
                self.root_window.draw_rectangle(pawn_list[entry][0],
                                                pawn_list[entry][1],
                                                pawn_list[entry][2],
                                                pawn_list[entry][3],
                                                pawn_list[entry][4],
                                                entry)
            if self.id_list[entry] == 2:
                self.root_window.draw_ellipse(pawn_list[entry][0],
                                              pawn_list[entry][1],
                                              pawn_list[entry][2],
                                              pawn_list[entry][3],
                                              pawn_list[entry][4],
                                              entry)
            if self.id_list[entry] == 3:
                self.root_window.draw_line(pawn_list[entry][0],
                                           pawn_list[entry][1],
                                           pawn_list[entry][2],
                                           pawn_list[entry][3],
                                           pawn_list[entry][4],
                                           entry)
