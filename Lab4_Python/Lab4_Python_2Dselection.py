TITLE = "MK Lab IV"
WIDTH = 960
HEIGHT = 500

start = Actor("startscreen")
start.screen = True
start.colorCounter = 0
start.fontcolor = "green"

select = Actor("selectscreen2d")

# add characters as actors
x = 260
y = 185
characterName = ["Scorpion", "Johnny Cage", "Raiden", "Lui Kang", "Tonya", "Kano", "Sub-Zero"]
characters = [""] * 7
for i in range(7):
    characters[i] = Actor("fighterbw"+str(i), (x,y))
    x += 146.5
    if x > 700:
        x = 260
        y = 362

# add p1Select box variables
p1Select = Actor("p1select")
p1Select.x = 260
p1Select.y = 185
p1Select.Visible = True
p1Select.Counter = 0
p1Select.index = 0

# Handle special case
characters[0].image = "fighter0"

arenaScreen = Actor("arenascreen")
arenaImages = ["arena0", "arena1", "arena2", "arena3"]
arenaSelect = Actor("arenaselect", (38, 252), (0,0))
arenaSelect.index = 0
arena = Actor(arenaImages[arenaSelect.index]+"f", (-WIDTH*0.95,-HEIGHT*0.1), (0,0))

screenNum = 1

maxHealth = 100
time = 99
animationCounter = 8

player1 = Actor("p1idle0", (0.10*WIDTH, 0.2*HEIGHT), (0,0))
player1.health = maxHealth
player1.name = "SCORPION"
player1.animationNum = 0
player1.dx = 0
player1.mode = "idle"

player2 = Actor("p2idle0", (0.75*WIDTH, 0.2*HEIGHT), (0,0))
player2.health = maxHealth
player2.name = "SUB-ZERO"
player2.animationNum = 0
player2.mode = "idle"

def draw():
    screen.clear()
    global screenNum
    if screenNum == 1:
        start.draw()
        screen.draw.text("PRESS ENTER", (int(0.37*WIDTH), int(0.87*HEIGHT)), fontsize = 45, color = start.fontcolor)
    elif screenNum == 2:
        select.draw()
        for i in range(7):
            characters[i].draw()

        if p1Select.Visible:
            p1Select.draw()
        screen.draw.text("P1: " + characterName[p1Select.index], (int(0.1*WIDTH), int(0.87*HEIGHT)), fontsize = 45, color = "green")

    elif screenNum ==  3:
        arenaScreen.draw()
        screen.blit(arenaImages[arenaSelect.index]+"m", (WIDTH*0.35, HEIGHT*0.73))
        x = 38
        y = 252
        for i in range(4):
            screen.blit(arenaImages[i], (x,y))
            x += 232
        arenaSelect.draw()

    elif screenNum == 4:
        arena.draw()
        #screen.blit(arenaImages[arenaSelect.index]+"f", (-WIDTH*0.95,-HEIGHT*0.1))

        # Health bar for player 1
        # Red bar
        screen.draw.filled_rect(Rect((40, 40), (maxHealth * 4, 30)), "red")
        # Green bar
        screen.draw.filled_rect(Rect((40, 40), (player1.health * 4, 30)), "green")
        # Yellow bar
        screen.draw.rect(Rect((40, 40), (maxHealth * 4, 30)), "yellow")

        # Health bar for player 2
        # Red bar
        screen.draw.filled_rect(Rect((510, 40), (maxHealth * 4, 30)), "red")
        # Green bar
        screen.draw.filled_rect(Rect((510, 40), (player2.health * 4, 30)), "green")
        # Yellow bar
        screen.draw.rect(Rect((510, 40), (maxHealth * 4, 30)), "yellow")

        # Draw players
        player1.draw()
        player2.draw()

        # Draw the text
        screen.draw.text(player1.name, (50, 43), fontsize = 40, color = "yellow")
        screen.draw.text(player2.name, (520, 43), fontsize = 40, color = "yellow")
        screen.draw.text(str(time), (460, 43), fontsize = 40, color = "yellow")

# make function for animating p1Select box
def animatePortrait(newIndex):
    characters[p1Select.index].image = "fighterbw" + str(p1Select.index)
    p1Select.index = newIndex
    characters[p1Select.index].image = "fighter" + str(p1Select.index)

def on_key_down(key):
    global screenNum
    if screenNum == 1:
        if key == keys.RETURN:
            screenNum = 2

    elif screenNum == 2:
        if key == keys.LEFT:
            if p1Select.x > 260:
                p1Select.x -= 146.5
                animatePortrait(p1Select.index - 1)
        elif key == keys.RIGHT:
            if p1Select.x < 699.5:
                if p1Select.y == 185:
                    p1Select.x += 146.5
                    animatePortrait(p1Select.index + 1)
                elif p1Select.y == 360 and p1Select.x < 553:
                    p1Select.x += 146.5
                    animatePortrait(p1Select.index + 1)
        elif key == keys.DOWN:
            if p1Select.y == 185 and p1Select.x <= 553:
                p1Select.y += 175
                animatePortrait(p1Select.index + 4)
        elif key == keys.UP:
            if p1Select.y == 360:
                p1Select.y -= 175
                animatePortrait(p1Select.index - 4)
        elif key == keys.RETURN:
            screenNum = 3

    elif screenNum == 3:
        if key == keys.LEFT:
            if arenaSelect.x > 38:
                arenaSelect.x -= 232
                arenaSelect.index -= 1
        elif key == keys.RIGHT:
            if arenaSelect.x < 730:
                arenaSelect.x += 232
                arenaSelect.index += 1
        elif key == keys.RETURN:
            screenNum = 4

    elif screenNum == 4:
        if key == keys.LEFT:
            player1.dx = -2
            player1.mode = "walk"
        elif key == keys.RIGHT:
            player1.dx = 2
            player1.mode = "walk"

def on_key_up(key):
    if screenNum == 4:
        if key == keys.LEFT or key == keys.RIGHT:
            player1.mode = "idle"
            player1.animationNum = 0
            player1.dx = 0

def update():
    if screenNum == 1:
        start.colorCounter += 1
        if start.colorCounter == 25:
            if start.fontcolor == "green":
                start.fontcolor = "black"
            else:
                start.fontcolor = "green"
            start.colorCounter = 0
    elif screenNum == 2:
        p1Select.Counter += 1
        if p1Select.Counter == 35:
            p1Select.Visible = not p1Select.Visible
            p1Select.Counter = 0
    elif screenNum == 4:
        global animationCounter

        # Player & Arena movement
        player1.x += player1.dx
        arena.x += -player1.dx
        player2.x += -player1.dx

        animationCounter -= 1
        if animationCounter == 0:
            animatePlayer1()
            animationCounter = 8

def animatePlayer1():
    if player1.mode == "walk":
        player1.image = "p1walk" + str(player1.animationNum)
        player1.animationNum = (player1.animationNum + 1) % 9
    elif player1.mode == "idle":
        player1.image = "p1idle" + str(player1.animationNum)
        player1.animationNum = (player1.animationNum + 1) % 7










