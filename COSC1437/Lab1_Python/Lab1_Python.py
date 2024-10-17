TITLE = "MK Lab I"
WIDTH = 960
HEIGHT = 500

start = Actor("startscreen")
start.screen = True
start.colorCounter = 0
start.fontcolor = "green"

select = Actor("selectscreen")

def draw():
    screen.clear()
    if start.screen:
        start.draw()
        screen.draw.text("PRESS ENTER", (int(0.37*WIDTH), int(0.87*HEIGHT)), fontsize = 45, color = start.fontcolor)
    else:
        select.draw()


def on_key_down(key):
    if key == keys.RETURN:
        start.screen = False

def update():
    start.colorCounter += 1
    if start.colorCounter == 25:
        if start.fontcolor == "green":
            start.fontcolor = "black"
        else:
            start.fontcolor = "green"
        start.colorCounter = 0
