def CreateCache(pawn_list):
    renderCache = open("RenderCache.txt", 'w+')
    CacheText = ''
    for x in range(0, len(pawn_list)):
        for y in range(0, len(pawn_list[x])):
            CacheText = CacheText + str(pawn_list[x][y]) + ','
        CacheText = CacheText+'\n'
    # CacheText = CacheText.replace("([", '')
    # CacheText = CacheText.replace("])", '')
    renderCache.write(CacheText)
    renderCache.close()

def GetCache():
    renderCache = open("RenderCache.txt", 'r')
    currentCache = []
    loop = 0
    for line in renderCache:
        currentLineArray = line.split(',')
        lineLoop = 0
        for x in currentLineArray:
            print(currentLineArray)
            currentCache[loop][x] = currentLineArray[int(x)]
            loop += 1

def RenderChange(pawn_list, currentWindow):
    print(GetCache())
    currentRender = pawn_list
    currentCache = GetCache()
    for pawn in currentCache:
        if currentCache[int(pawn)] == currentRender[int(pawn)]:
            pass
        else:
            currentWindow.canvas.delete(str(pawn))
