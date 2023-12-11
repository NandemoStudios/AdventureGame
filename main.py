import window
import draw
import time
import threading

global shouldLoop
global Frames
global FPS


targetFramerate = 30
Frames = 0
FPS = 0


def UpdateFramerate():
    global Frames
    global FPS
    while True:
        time.sleep(1)
        FPS = Frames
        Frames = 0
        newWindow.FPSDisplay.config(text="FPS: "+str(FPS))


def RenderLoop():
    global Frames
    while True:
        newWindow.canvas.delete("all")
        newEngine.drawLoop()
        time.sleep(1/targetFramerate)
        Frames += 1


newWindow = window.Window("1280x720")

pawn_list = [20, 20, 20, 20, 5], [20, 200, 200, 20, 5], [50, 50, 100, 100, 5]
id_list = [1, 2, 3]
newEngine = draw.Engine(newWindow, pawn_list, id_list)

renderingThread = threading.Thread(target=RenderLoop, daemon=True)
renderingThread.start()

frameRateUpdate = threading.Thread(target=UpdateFramerate, daemon=True)
frameRateUpdate.start()

newWindow.Start()
