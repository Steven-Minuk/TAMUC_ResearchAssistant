TITLE = "Maze Game"
blockSize = 50
WIDTH = blockSize*16
HEIGHT = blockSize*12

background = [
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[3,2,2,2,2,2,2,2,4,4,4,4,4,4,4,1],
[1,4,4,4,4,4,4,2,4,4,4,4,4,4,4,1],
[1,4,4,4,4,4,4,2,4,4,4,4,4,4,4,1],
[1,4,4,4,4,4,4,2,4,4,4,4,4,4,4,1],
[1,4,4,4,4,4,4,2,4,4,4,4,4,4,4,1],
[1,4,4,4,4,4,4,2,4,4,4,4,4,4,4,1],
[1,4,4,4,4,4,4,2,2,2,2,2,2,2,2,3],
[1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1],
[1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1],
[1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

blackblock = Actor("blackblock", (0,0), (0,0))
whiteblock = Actor("whiteblock", (0,0), (0,0))
greenblock = Actor("greenblock", (0,0), (0,0))
yellowblock = Actor("yellowblock", (0,0), (0,0))
redblock = Actor("redblock", (0,blockSize), (0,0))

gameover = False


for row in background:
    print(row)

def draw():
    screen.clear()
    for row in range(len(background)):
        for column in range(len(background[row])):
            if background[row][column] == 1:
                blackblock.x = blockSize*column
                blackblock.y = blockSize*row
                blackblock.draw()
            elif background[row][column] == 2:
                whiteblock.x = blockSize*column
                whiteblock.y = blockSize*row
                whiteblock.draw()
            elif background[row][column] == 3:
                yellowblock.x = blockSize*column
                yellowblock.y = blockSize*row
                yellowblock.draw()
            elif background[row][column] == 4:
                greenblock.x = blockSize*column
                greenblock.y = blockSize*row
                greenblock.draw()
            elif background[row][column] == 5:
                redblock.x = blockSize*column
                redblock.y = blockSize*row
                redblock.draw()
    redblock.draw()

def update():
    "Make the RedBlock reach to the goal!"
    if redblock.x <= blockSize*7:
        goRight()
    else:
        stop()
        if redblock.y <= blockSize*7:
            goDown()
        else:
            stop()
            if redblock.x <= blockSize*15:
                goRight()
            else:
                stop()


def goRight():
    redblock.x += 1

def goLeft():
    redblock.x -= 1

def goDown():
    redblock.y += 1

def goUp():
    redblock.y -= 1

def stop():
    redblock.x += 0
    redblock.y += 0

