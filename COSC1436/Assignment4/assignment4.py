TITLE = "Assignment 4"
WIDTH = 960
HEIGHT = 500

# Declare the fight game Actor (Sprite)
fight = Actor("shang stage full", (500, 200))
#fight = Actor("shang stage")
fight.time = 99
fight.maxHealth = 100

# Declare the Player 1 Actor (Sprite)
player1 = Actor("p1idle0", (0.2*WIDTH, 0.58*HEIGHT))
player1.name = "SCORPION"
player1.health = 100
player1.score = 0
# Assignment 4 - new added properties
player1.imgNum = 0
player1.animCounter = 8
player1.dx = 0
player1.move = "idle"

# Declare the Player 2 Actor (Sprite)
player2 = Actor("p2idle0", (0.8*WIDTH, 0.58*HEIGHT))
player2.name = "SUB-ZERO"
player2.health = 100
player2.score = 0

def draw():
    screen.clear()
    # Draw the Background (Assignment 2)
    fight.draw()

    # Draw the 2 players (Assignment 2)
    player2.draw()
    player1.draw()

    # Assignment 4: animate the first player
    nextImage()

    # Draw health bar for Player 1 (Assignment 2)
    screen.draw.filled_rect(Rect((45, 55), (fight.maxHealth * 4+10, 40)), "yellow")
    screen.draw.filled_rect(Rect((50, 60), (fight.maxHealth * 4, 30)), "red")
    screen.draw.filled_rect(Rect((50, 60), (player1.health * 4, 30)), "green")
    screen.draw.text(player1.name, (50, 70), fontsize = 30, color= "black")

    # Draw health bar for Player 2 (Assignment 2)
    screen.draw.filled_rect(Rect((535, 55), (fight.maxHealth * 4+10, 40)), "yellow")
    screen.draw.filled_rect(Rect((540, 60), (fight.maxHealth * 4, 30)), "red")
    screen.draw.filled_rect(Rect((540+(fight.maxHealth - player2.health)*4, 60), ((player2.health)* 4, 30)), "green")
    screen.draw.text(player2.name, (800, 70), fontsize = 30, color= "black")

    # Draw the time and Scores, for now only print constant values (Assignment 2)
    screen.draw.text("99", (475, 20), fontsize = 60, color= "red")
    screen.draw.text("0000", (50, 30), fontsize = 40, color= "yellow")
    screen.draw.text("0000", (850, 30), fontsize = 40, color= "yellow")

def on_key_down(key):
    "Add your code here"    # - Assignment 4: key movements: forwards, backwards, punch, and kick

    player1.imgNum = 0
    if key == keys.LEFT:
        player1.dx  = -2
        player1.move = "walk"
    elif key == keys.RIGHT:
        player1.dx  = 2
        player1.move = "walk"
    elif key == keys.UP:
        player1.move = "hp" # Revised by Minuk
        #player1.imgNum = 0
    elif key == keys.DOWN:
        player1.move = "lk" # Revised by Minuk

def on_key_up(key):
    "Add your code here"    # - Assignment 4:
    if key == keys.LEFT or key == keys.RIGHT:
        player1.dx = 0
        player1.move = "idle"

def update():
    "Add your code here"    # - Assignment 4: add  continuous character movement
    player1.x += player1.dx


def nextImage():
    "Add your code here"    # - Assignment 4: function to animate player 1 movement or idle standing
    # to animate,student can either use modulus or if statements
    player1.animCounter -= 1
    if player1.animCounter == 0:
        player1.animCounter = 8
        if player1.move == "idle":
            player1.imgNum = (player1.imgNum+1) % 7
            player1.image = "p1"+ player1.move +str(player1.imgNum) # Revised by Minuk
        elif player1.move == "walk":
            player1.imgNum = (player1.imgNum+1) % 9
            player1.image = "p1" + player1.move +str(player1.imgNum) # Revised by Minuk
        elif player1.move == "hp":
            player1.imgNum = (player1.imgNum+1) % 5
            player1.image = "p1" + player1.move +str(player1.imgNum) # Revised by Minuk
            if player1.imgNum ==0:
                player1.move = "idle"
        elif player1.move == "lk":
            player1.imgNum = (player1.imgNum+1) % 5
            player1.image = "p1" + player1.move +str(player1.imgNum) # Revised by Minuk
            if player1.imgNum ==0:
                player1.move = "idle"
