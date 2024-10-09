TITLE = "Assignment 6 - Test your might"
WIDTH = 800
HEIGHT = 500

game = Actor("bgd.png")
game.timer = 5*60       # 5 seconds
game.playerMight = 0.0
game.hardness = 50.0
game.started = False
game.dropValue = 0.2
game.increaseValue = 7.5
# Assignment 6 - add the 2 properties and 2 lists to the given actor
game.moveNextLevel = False
game.level = 0
game.items = ['wood','stone', 'steel', 'ruby', 'diamond']
game.brokenItems = ['woodb','stoneb', 'steelb', 'rubyb', 'diamondb']

# Assignment 6 - create new actor to represent the item to break
item = Actor(game.items[game.level])

player = Actor("ready.png")


def on_key_down(key):
    game.started = True
    if key == keys.SPACE and game.timer > 0:
        game.playerMight  += game.increaseValue

def update():
    # Assignment 6 -  modify the code from Assignment 5 so the player advances through different levels
    # each time they advance to a new level, they get a new item, and the stage becomes more challenging
    if game.timer > 0:
        if game.started:
            game.timer -= 1
        if game.playerMight > 0:
            game.playerMight -= game.dropValue
    else:
        player.image = "hit.png"
        if game.playerMight >= game.hardness:
            item.image = game.brokenItems[game.level]
            game.image = "bgds.png"
            if game.level < 4 and not game.moveNextLevel:  # Assignment 6 - moves to the next level
                game.moveNextLevel = True
                clock.schedule(nextLevel, 1.5)
        else:
            game.image = "bgdf.png"

# Assignment 6 - Need to write this function
def nextLevel():
    # Update Variables
    game.level += 1
    game.timer = 5*60       # 5 seconds
    game.playerMight = 0.0
    game.started = False
    game.moveNextLevel = False
    game.dropValue += 0.05
    game.increaseValue -= 0.5
    # Reset Images
    game.image = "bgd.png"
    player.image = "ready.png"
    item.image = game.items[game.level]


def draw():
    screen.clear()
    game.draw()
    player.draw()
    item.draw()
    screen.draw.text("Level "+str(game.level + 1), center=(WIDTH*0.5, HEIGHT*0.1), fontsize=50, color= "white")
    screen.draw.text(str(game.timer//60), center=(WIDTH*0.25, HEIGHT*0.5), fontsize=50, color="yellow")
    mightBar = Rect((WIDTH*0.75, max(HEIGHT*0.25, HEIGHT*0.75-game.playerMight*2.5)), (WIDTH*0.06, min(game.playerMight*2.5, HEIGHT*0.5)))
    screen.draw.filled_rect(mightBar, (255, 211, 0))
    mightRuler = Rect((WIDTH*0.75, HEIGHT*0.25), (WIDTH*0.06, HEIGHT*0.5))
    screen.draw.rect(mightRuler, (91, 168, 255))
    screen.draw.line((WIDTH*0.75, HEIGHT/2), (WIDTH*0.81, HEIGHT/2), (255, 32, 32))
    if not game.started :
        screen.draw.text("PRESS ANY KEY TO START", center=(WIDTH*0.5, HEIGHT*0.5), fontsize=30, color="yellow", background="black")




