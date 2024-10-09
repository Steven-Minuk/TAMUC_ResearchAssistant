TITLE = "Assingment 1"
WIDTH = 1000
HEIGHT = 500

# Questions 1 & 2 & 4 should be here
maxHealth = 100
player1Health = maxHealth
player2Health = maxHealth-50

def draw():
    screen.clear()

    # Draw health bar for Player 1 - Question 3
    screen.draw.filled_rect(Rect((45, 25), (100 * 4+10, 40)), "yellow")
    screen.draw.filled_rect(Rect((50, 30), (100 * 4, 30)), "red")
    screen.draw.filled_rect(Rect((50, 30), (player1Health * 4, 30)), "green")

    # Draw health bar for Player 2  - Question 5
    screen.draw.filled_rect(Rect((545, 25), (100 * 4+10, 40)), "yellow")
    screen.draw.filled_rect(Rect((550, 30), (100 * 4, 30)), "green")
    screen.draw.filled_rect(Rect((550, 30), (player2Health * 4, 30)), "red")


def update():
    "please do not delete"
