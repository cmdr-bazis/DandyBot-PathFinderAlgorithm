import math
import array as arr

def script(check, x, y):
    if check("level") == 1 or check("level") == 2:
        direction = ""

        xGoal = 0
        yGoal = 0

        lengthMin = 1097415683745
        if check("gold", x, y):
            return "take"
        for xCheck in range(x - 30, x + 30):
            for yCheck in range(y - 30, y + 30):
                if check("gold", xCheck, yCheck):
                    if math.sqrt((xCheck - x)**2 + (yCheck - y)**2) < lengthMin:
                        lengthMin = math.sqrt((xCheck - x)**2 + (yCheck - y)**2)
                        xGoal = xCheck
                        yGoal = yCheck

        print(x, y)
        print(xGoal, yGoal)

        if abs(xGoal - x) > abs(yGoal - y):
            if xGoal > x:
                direction = "right"
            elif xGoal < x:
                direction = "left"
        else:
            if yGoal > y:
                direction = "down"
            elif yGoal < y:
                direction = "up"
        print(direction)
        return direction

    if check("level") == 3:
        findRange = 50
        listMap = []
        for i in range(2 * findRange):
            listMap.append([" "] * i)

        for i in range(x - findRange, x + findRange):
            for j in range(y - findRange, y + findRange):
                if check("wall", x, y):
                    listMap[i][j] = "#"
                elif check("gold", x, y):
                    listMap[i][j] = "1"

        for i in range(len(listMap)):
            for j in range(len(listMap)):
                print(listMap[i][j])

        return "pass"






