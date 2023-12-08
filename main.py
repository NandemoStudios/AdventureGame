import tkinter
import window
import draw

newWindow = window.Window("1280x720")

pawn_list = [1, 1]
id_list = [1, 2]

newEngine = draw.Engine(newWindow, pawn_list, id_list)
newEngine.drawLoop()

newWindow.Start()
