TITLE = "Assignment 5 - Test your might"
WIDTH = 800
HEIGHT = 500

game = Actor("bgd.png")
# Assignment 5 - add properties to the given actor
game.timer = 5*60       # 5 seconds
game.playerMight = 0.0
game.steelHardness = 50.0
game.started = False
game.dropValue = 0.5
game.increaseValue = 7.0

player = Actor("ready.png")


def on_key_down(key):
    "Add your code here"    # - Assignment 5: game starts when player presses any key
    game.started = True
    if key == keys.SPACE and game.timer > 0:
        game.playerMight  += game.increaseValue

def update():
    "Add your code here"    # - Assignment 5: the students need to implement if logic: healthbar increases when spacebar is pressed
                            # after 5 seconds pass, either the player wins or fails
    if game.timer > 0:
        if game.started:
            game.timer -= 1
        if game.playerMight > 0:
            game.playerMight -= game.dropValue
    else:
        if game.playerMight >= game.steelHardness:
            player.image = "successful.png"
        else:
            player.image = "failed.png"

def draw():
    screen.clear()
    game.draw()
    player.draw()
    screen.draw.text(str(game.timer//60), center=(WIDTH*0.25, HEIGHT*0.5), fontsize=50, color=(255, 211, 0))
    mightBar = Rect((WIDTH*0.75, max(HEIGHT*0.25, HEIGHT*0.75-game.playerMight*2.5)), (WIDTH*0.06, min(game.playerMight*2.5, HEIGHT*0.5)))
    screen.draw.filled_rect(mightBar, (255, 211, 0))
    mightRuler = Rect((WIDTH*0.75, HEIGHT*0.25), (WIDTH*0.06, HEIGHT*0.5))
    screen.draw.rect(mightRuler, (91, 168, 255))
    screen.draw.line((WIDTH*0.75, HEIGHT/2), (WIDTH*0.81, HEIGHT/2), (255, 32, 32))
    # - Assignment 5: need to add
    if not game.started :
        screen.draw.text("PRESS ANY KEY TO START", center=(WIDTH*0.5, HEIGHT*0.5), fontsize=30, color=(255, 211, 0), background="black")




