import tkinter
import window
import draw
import threading


newWindow = window.Window("1280x720")

pawn_list = [20, 20, 20, 20, 5], [20, 200, 200, 20, 5], [50, 50, 100, 100, 5]
id_list = [1, 2, 3]
newEngine = draw.Engine(newWindow, pawn_list, id_list)
newEngine.drawLoop()

newWindow.Start()
