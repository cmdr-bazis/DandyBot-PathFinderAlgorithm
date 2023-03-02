import math
import array as arr


def waveCheck(string):
    for i in range(len(string)):
        if int(ord(string[i])) < 48 or int(ord(string[i]) > 57):
            return False
    return True


def listMapCreate(lenX, lenY, check):
    listMap = []
    for i in range(lenX):
        listMap.append([" "] * lenY)

    for i in range(lenX):
        for j in range(lenY):
            if check("wall", i, j) == 1 or check("player", i, j) == 1:
                listMap[i][j] = "#"
            elif check("gold", i, j) == 1:
                listMap[i][j] = "*"
            else:
                listMap[i][j] = " "
    return listMap


def waveCreation(listMap, x, y, lenX, lenY):
    xGoal = 0
    yGoal = 0
    lengthMin = 37624865
    for i in range(lenX):
        for j in range(lenY):
            if listMap[i][j] == "*":
                if math.sqrt((i - x) ** 2 + (j - y) ** 2) < lengthMin:
                    lengthMin = math.sqrt((i - x) ** 2 + (j - y) ** 2)
                    xGoal = i
                    yGoal = j
    waveLevel = 0
    listMap[xGoal][yGoal] = str(waveLevel)
    while True:
        for i in range(lenX):
            for j in range(lenY):
                if listMap[i][j] == str(waveLevel):
                    if i - 1 >= 0 and listMap[i - 1][j] != "#":
                        if i - 1 == x and j == y:
                            listMap[i - 1][j] = str(waveLevel + 1)
                            return listMap
                        else:
                            listMap[i - 1][j] = str(waveLevel + 1)
                    if i + 1 < lenX and listMap[i + 1][j] != "#":
                        if i + 1 == x and j == y:
                            listMap[i + 1][j] = str(waveLevel + 1)
                            return listMap
                        else:
                            listMap[i + 1][j] = str(waveLevel + 1)
                    if j - 1 >= 0 and listMap[i][j - 1] != "#":
                        if i == x and j - 1 == y:
                            listMap[i][j - 1] = str(waveLevel + 1)
                            return listMap
                        else:
                            listMap[i][j - 1] = str(waveLevel + 1)
                    if j + 1 < lenY and listMap[i][j + 1] != "#":
                        if i == x and j + 1 == y:
                            listMap[i][j + 1] = str(waveLevel + 1)
                            return listMap
                        else:
                            listMap[i][j + 1] = str(waveLevel + 1)

        waveLevel += 1


def script(check, x, y):
    if check("gold", x, y):
        return "take"
    direction = ""
    lenX = 0
    lenY = 0
    waveLevel = 0
    if check("level") == 1:
        lenX = 28
        lenY = 9
    elif check("level") == 2:
        lenX = 28
        lenY = 11
    elif check("level") == 3 or check("level") == 4:
        lenX = 28
        lenY = 25
    elif check("level") == 5:
        lenX = 17
        lenY = 17

    listMap = listMapCreate(lenX, lenY, check)
    listMap = waveCreation(listMap, x, y, lenX, lenY)

    waveMoveLevel = int(listMap[x][y])
    if x + 1 <= lenX:
        if waveCheck(listMap[x + 1][y]):
            if int(listMap[x + 1][y]) == waveMoveLevel - 1:
                return "right"
    if x - 1 >= 0:
        if waveCheck(listMap[x - 1][y]):
            if int(listMap[x - 1][y]) == waveMoveLevel - 1:
                return "left"
    if y + 1 < lenY:
        if waveCheck(listMap[x][y + 1]):
            if int(listMap[x][y + 1]) == waveMoveLevel - 1:
                return "down"
    if y - 1 >= 0:
        if waveCheck(listMap[x][y - 1]):
            if int(listMap[x][y - 1]) == waveMoveLevel - 1:
                return "up"
    return direction
