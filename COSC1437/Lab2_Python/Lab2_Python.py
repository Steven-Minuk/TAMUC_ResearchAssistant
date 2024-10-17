TITLE = "MK Lab II"
WIDTH = 960
HEIGHT = 500

start = Actor("startscreen")
start.screen = True
start.colorCounter = 0
start.fontcolor = "green"

select = Actor("selectscreen")

# add characters as actors
x = 77
y = 326
characterName = ["Scorpion", "Johnny Cage", "Raiden", "Lui Kang", "Tonya", "Kano", "Sub-Zero"]
characters = [""] * 7
for i in range(7):
    characters[i] = Actor("fighterbw"+str(i), (x,y))
    x += 134

# add p1Select box variables
p1Select = Actor("p1select")
p1Select.x = 77
p1Select.y = 326
p1Select.Visible = True
p1Select.Counter = 0
p1Select.index = 0

# Handle special case
characters[0].image = "fighter0"

def draw():
    screen.clear()
    if start.screen:
        start.draw()
        screen.draw.text("PRESS ENTER", (int(0.37*WIDTH), int(0.87*HEIGHT)), fontsize = 45, color = start.fontcolor)
    else:
        select.draw()
        for i in range(7):
            characters[i].draw()

        if p1Select.Visible:
            p1Select.draw()
        screen.draw.text("P1: " + characterName[p1Select.index], (int(0.1*WIDTH), int(0.87*HEIGHT)), fontsize = 45, color = "green")

# make function for animating p1Select box
def animatePortrait(newIndex):
    characters[p1Select.index].image = "fighterbw" + str(p1Select.index)
    p1Select.index = newIndex
    characters[p1Select.index].image = "fighter" + str(p1Select.index)

def on_key_down(key):
    if key == keys.RETURN:
        start.screen = False

    else:
        if key == keys.LEFT:
            if p1Select.x > 77:
                p1Select.x -= 134
                animatePortrait(p1Select.index - 1)


        elif key == keys.RIGHT:
            if p1Select.x < 881:
                p1Select.x += 134
                animatePortrait(p1Select.index + 1)

def update():
    start.colorCounter += 1
    if start.colorCounter == 25:
        if start.fontcolor == "green":
            start.fontcolor = "black"
        else:
            start.fontcolor = "green"
        start.colorCounter = 0
    else:
        p1Select.Counter += 1
        if p1Select.Counter == 35:
            p1Select.Visible = not p1Select.Visible
            p1Select.Counter = 0











