import tkinter

import window
import draw
import time
import threading
import caching

global shouldLoop
global Frames
global FPS

# TODO - Add some randomized movement to the engine
# TODO - Make the caching system based per pawn and not the entire screen

targetFramerate = 60
Frames = 0
Framerate = 0

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


def RenderLoop():
    global pawn_list
    caching.CreateCache(pawn_list)
    newEngine.drawLoop(pawn_list)
    while True:
        global Frames
        render_cache = caching.GetCache()
        if str(pawn_list) == str(render_cache):
            Frames += 1
            time.sleep(1/targetFramerate)
        else:
            caching.RenderChange(pawn_list, newWindow)
            newEngine.drawLoop(pawn_list)
            time.sleep(1 / targetFramerate)
            Frames += 1
            caching.CreateCache(pawn_list)
            print("Render was cached")


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
