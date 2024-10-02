
import random

TITLE = "Arcade Ping Pong"
WIDTH = 480
HEIGHT = 320

background = Actor("background.png")
background.x = 240
background.y = 160

ball = Actor("ball.png")
ball.x = 242
ball.y = 160

ball.dx = 2
ball.dy = 2

ballMoving = random.randint(1,8)

bar = Actor("bar.png")
bar.x = 10
bar.y = 160

bar.dx = 0
bar.dy = 0

pcBar = Actor("pcbar.png")
pcBar.x = 470
pcBar.y = 160
pcBar.directory = 1
pcBar.counter = 0

myScore = 0
pcScore = 0

selectionBox = Actor("selectionbox.png")
selectionBox.x = 127
selectionBox.y = 190

gameStart = False
gameProcess = 0
gameMode = 0

def draw():
    screen.clear()
    background.draw()
    if gameProcess == 0:
        screen.draw.text("Press Enter to Start The Game", (100,150), fontsize = 30)
    elif gameProcess == 1:
        screen.draw.text("Choose The Game Mode", (100,100), fontsize = 35)
        screen.draw.text("EASY", (100,180), fontsize = 30)
        screen.draw.text("NORMAL", (200,180), fontsize = 30)
        screen.draw.text("HARD", (330,180), fontsize = 30)
        selectionBox.draw()
    elif gameProcess == 2:
        screen.draw.text(str(myScore) + " : " + str(pcScore), (212,0), fontsize = 40)
        ball.draw()
        bar.draw()
        pcBar.draw()
        if myScore == 5:
            screen.draw.text("You Win", (200, 160), fontsize = 30)
        elif pcScore == 5:
            screen.draw.text("You Lose", (200, 160), fontsize = 30)

def on_key_down(key):
    global gameProcess
    global gameMode
    if gameProcess == 1:
        if gameMode == 0:
            if key == keys.RIGHT:
                selectionBox.x += 117
                gameMode += 1
        elif gameMode == 1:
            if key == keys.RIGHT:
                selectionBox.x += 116
                gameMode += 1
            elif key == keys.LEFT:
                selectionBox.x -= 117
                gameMode -= 1
        elif gameMode == 2:
            if key == keys.LEFT:
                selectionBox.x -= 116
                gameMode -= 1
    elif gameProcess == 2:
        if key == keys.UP:
            bar.dy -= 1.5
        elif key == keys.DOWN:
            bar.dy += 1.5
        elif key == keys.RIGHT:
            bar.dx += 1.5
        elif key == keys.LEFT:
            bar.dx -= 1.5

    if key == keys.RETURN:
        if gameProcess == 0:
            gameProcess += 1
        elif gameProcess == 1:
            gameProcess += 1
            gameStart = True

def on_key_up(key):
    bar.dx = 0
    bar.dy = 0

def moveBar():
    if bar.x >= 0 and bar.x <= 240:
        bar.x = bar.x + bar.dx
    elif bar.x <0:
        bar.x = 0
    elif bar.x > 240:
        bar.x = 240

    if bar.y >= 0 and bar.y <= 320:
        bar.y = bar.y + bar.dy
    elif bar.y < 0:
        bar.y = 0
    elif bar.y > 320:
        bar.y = 320

def moveBall():
    if ballMoving == 1:
        ball.y = ball.y - ball.dy
    elif ballMoving == 2:
        ball.y = ball.y - ball.dy
        ball.x = ball.x + ball.dx
    elif ballMoving == 3:
        ball.x = ball.x + ball.dx
    elif ballMoving == 4:
        ball.y = ball.y + ball.dy
        ball.x = ball.x + ball.dx
    elif ballMoving == 5:
        ball.y = ball.y + ball.dy
    elif ballMoving == 6:
        ball.y = ball.y + ball.dy
        ball.x = ball.x - ball.dx
    elif ballMoving == 7:
        ball.x = ball.x - ball.dx
    elif ballMoving == 8:
        ball.y = ball.y - ball.dy
        ball.x = ball.x - ball.dx

def wallTouch():
    global ballMoving
    if ball.y == 0:
        if ballMoving == 1:
            ballMoving = random.choice([4,6])
        elif ballMoving == 2:
            ballMoving = 4
        elif ballMoving == 8:
            ballMoving = 6
    elif ball.y == 320:
        if ballMoving == 5:
            ballMoving = random.choice([2,8])
        elif ballMoving == 4:
            ballMoving = 2
        elif ballMoving == 6:
            ballMoving = 8
    return ballMoving

def mybarTouch():
    global ballMoving
    if ball.colliderect(bar):
        if ballMoving == 7:
            ballMoving = random.choice([2,4])
        elif ballMoving == 6:
            ballMoving = 4
        elif ballMoving == 8:
            ballMoving = 2
        return ballMoving

def pcbarTouch():
    global ballMoving
    if ball.colliderect(pcBar):
        if ballMoving == 3:
            ballMoving = random.choice([6,8])
        elif ballMoving == 4:
            ballMoving = 6
        elif ballMoving == 2:
            ballMoving = 8
        return ballMoving

def scoring():
    global pcScore
    global myScore
    if ball.x == 0:
        pcScore += 1
    elif ball.x == 480:
        myScore += 1
    return pcScore
    return myScore

def pcBarMovelv1():
    pcBar.y -= pcBar.directory
    pcBar.counter += 1
    if pcBar.counter > 160:
        pcBar.directory *= -1
        pcBar.counter *= -1

def pcBarMovelv2():
    if pcBar.y < ball.y:
        pcBar.y += 1.5
    elif pcBar.y > ball.y:
        pcBar.y -= 1.5

def pcBarMovelv3():
    if pcBar.y < ball.y:
        pcBar.y += 1.8
    elif pcBar.y > ball.y:
        pcBar.y -= 1.8
    if ball.x >= 240:
        if pcBar.x > ball.x:
            pcBar.x -= 1
    else:
        if pcBar.x <= 470:
            pcBar.x += 1.5

def reset():
    bar.x = 10
    bar.y = 160
    pcBar.x = 470
    pcBar.y = 160
    ball.x = 242
    ball.y = 160

def update():
    global gameStart
    if gameProcess == 2:
        if gameStart:
            print(ball.x,ball.y)
            if 0 < ball.x < 480:
                moveBar()
                moveBall()
                if gameMode == 0:
                    pcBarMovelv1()
                elif gameMode == 1:
                    pcBarMovelv2()
                elif gameMode == 2:
                    pcBarMovelv3()
                wallTouch()
                mybarTouch()
                pcbarTouch()
                scoring()
            else:
                gameStart = False
        else:
            if myScore < 5 and pcScore < 5:
                clock.schedule(reset, 1)
                gameStart = True # Q1. if it is in the reset fucntion then it's not working, why?

