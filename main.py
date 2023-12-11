import window
import draw
import time
import threading

global shouldLoop

targetFramerate = 30


def RenderLoop():
    while True:
        newWindow.canvas.delete("all")
        newEngine.drawLoop()
        time.sleep(1/targetFramerate)


newWindow = window.Window("1280x720")

pawn_list = [20, 20, 20, 20, 5], [20, 200, 200, 20, 5], [50, 50, 100, 100, 5]
id_list = [1, 2, 3]
newEngine = draw.Engine(newWindow, pawn_list, id_list)

renderingThread = threading.Thread(target=RenderLoop, daemon=True)
renderingThread.start()

newWindow.Start()
