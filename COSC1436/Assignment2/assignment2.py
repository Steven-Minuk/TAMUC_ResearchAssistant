TITLE = "Assignment 2"
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

# Declare the Player 2 Actor (Sprite)
player2 = Actor("p2idle0", (0.8*WIDTH, 0.58*HEIGHT))
player2.name = "SUB-ZERO"
player2.health = 100
player2.score = 0

def draw():
    screen.clear()
    # Draw the Background
    fight.draw()

    # Draw the 2 players
    player1.draw()
    player2.draw()

    # Draw health bar for Player 1
    screen.draw.filled_rect(Rect((45, 55), (fight.maxHealth * 4+10, 40)), "yellow")
    screen.draw.filled_rect(Rect((50, 60), (fight.maxHealth * 4, 30)), "red")
    screen.draw.filled_rect(Rect((50, 60), (player1.health * 4, 30)), "green")
    screen.draw.text(player1.name, (50, 70), fontsize = 30, color= "black")

    # Draw health bar for Player 2
    screen.draw.filled_rect(Rect((535, 55), (fight.maxHealth * 4+10, 40)), "yellow")
    screen.draw.filled_rect(Rect((540, 60), (fight.maxHealth * 4, 30)), "red")
    screen.draw.filled_rect(Rect((540+(fight.maxHealth - player2.health)*4, 60), ((player2.health)* 4, 30)), "green")
    screen.draw.text(player2.name, (800, 70), fontsize = 30, color= "black")

    # Draw the time and Scores, for now only print constant values
    screen.draw.text("99", (475, 20), fontsize = 60, color= "red")
    screen.draw.text("0000", (50, 30), fontsize = 40, color= "yellow")
    screen.draw.text("0000", (850, 30), fontsize = 40, color= "yellow")

# In later assignments we will modify the code below
def update():
    "please do not delete"
