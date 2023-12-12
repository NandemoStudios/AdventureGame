import tkinter

import window
import draw
import time
import threading
import time

global shouldLoop
global Frames
global FPS

# TODO - Add some randomized movement to the engine
# TODO - Make the caching system based per pawn and not the entire screen
# TODO - Fix the framerate cap, lower end devices cause the capped framerate system to break

targetFramerate = 60
Frames = 0
FPS = 0

def CacheCurrentRendering():
    renderCache = open("RenderCache.txt", 'w+')
    renderCache.write(str(pawn_list))
    renderCache.close()


def UpdateFramerate():
    global Frames
    global FPS
    while True:
        FPS = Frames
        Frames = 0
        newWindow.FPSDisplay.config(text="FPS: "+str(FPS))
        time.sleep(1)

def IncreaseSize():
    pawn_list[1][2] = pawn_list[1][2] + 10
    print(pawn_list[1][2])


def RenderLoop():
    CacheCurrentRendering()
    global pawn_list
    newEngine.drawLoop(pawn_list)
    while True:
        global Frames
        render_cache = open("renderCache.txt", 'r').read()
        if str(pawn_list) == str(render_cache):
            start_time = time.time()
            Frames += 1
            end_time = time.time()
            remaining_wait = end_time - start_time
            remaining_wait = ((1 / targetFramerate) - remaining_wait) / 2
            time.sleep(remaining_wait)
        else:
            start_time = time.time()
            newWindow.canvas.delete("all")
            newEngine.drawLoop(pawn_list)
            end_time = time.time()
            remaining_wait = end_time-start_time
            remaining_wait = ((1/targetFramerate)-remaining_wait) / 2
            time.sleep(remaining_wait)
            Frames += 1
            CacheCurrentRendering()
            print(remaining_wait)


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

newWindow.root.bind("WM_DELETE_WINDOW", newWindow.on_closing)

newWindow.Start()
