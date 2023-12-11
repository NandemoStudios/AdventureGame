import tkinter

import window
import draw
import time
import threading

global shouldLoop
global Frames
global FPS
global renderCache

renderCache = []

targetFramerate = 60
Frames = 0
FPS = 0

def CacheRendering():
    renderCache = pawn_list


def UpdateFramerate():
    global Frames
    global FPS
    while True:
        time.sleep(1)
        FPS = Frames
        Frames = 0
        newWindow.FPSDisplay.config(text="FPS: "+str(FPS))

def IncreaseSize():
    pawn_list[1][2] = pawn_list[1][2] + 10
    print(pawn_list[1][2])
    renderCache = pawn_list


def RenderLoop():
    global Frames
    global renderCache
    CacheRendering()
    while True:
        if renderCache == pawn_list:
            print(pawn_list)
            print(renderCache)
            time.sleep(1 / targetFramerate)
            Frames += 1
        else:
            newWindow.canvas.delete("all")
            newEngine.drawLoop(pawn_list)
            time.sleep(1 / targetFramerate)
            Frames += 1
            renderCache = pawn_list
            print("Cached Render")


newWindow = window.Window("1280x720")
addButton = tkinter.Button(newWindow.root, text="+", command=IncreaseSize)
addButton.pack()

pawn_list = [20, 20, 20, 20, 5], [20, 200, 200, 20, 5], [50, 50, 100, 100, 5]
id_list = [1, 2, 3]
newEngine = draw.Engine(newWindow, pawn_list, id_list)

renderingThread = threading.Thread(target=RenderLoop, daemon=True)
renderingThread.start()

frameRateUpdate = threading.Thread(target=UpdateFramerate, daemon=True)
frameRateUpdate.start()

newWindow.Start()
