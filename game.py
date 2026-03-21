# Import Brython browser tools
from browser import document

# Get canvas element from HTML
canvas = document["game"]

# Get drawing context (used to draw shapes)
ctx = canvas.getContext("2d")

# -------------------------------
# DRAW FUNCTION
# -------------------------------
def draw():
    """
    This function draws basic elements on the screen.

    It will be expanded later to include units, combat,
    and animations.
    """

    # Clear the screen
    ctx.clearRect(0, 0, 800, 300)

    # Draw ground
    ctx.fillStyle = "lightgreen"
    ctx.fillRect(0, 200, 800, 100)

    # Draw player base (left side)
    ctx.fillStyle = "blue"
    ctx.fillRect(20, 150, 50, 50)

    # Draw enemy base (right side)
    ctx.fillStyle = "red"
    ctx.fillRect(730, 150, 50, 50)


# Call draw once (for now)
draw()

# Import Brython browser tools
from browser import document, timer

# Get canvas element from HTML
canvas = document["game"]

# Get drawing context (used to draw shapes)
ctx = canvas.getContext("2d")

# -------------------------------
# GAME STATE
# -------------------------------

# This variable controls whether the game is running
game_running = True


# -------------------------------
# DRAW FUNCTION
# -------------------------------
def draw():
    """
    Draws all game elements on the screen.

    This function is called repeatedly in the game loop,
    allowing animations and updates.
    """

    # Clear the screen (important for animation)
    ctx.clearRect(0, 0, 800, 300)

    # Draw ground
    ctx.fillStyle = "lightgreen"
    ctx.fillRect(0, 200, 800, 100)

    # Draw player base
    ctx.fillStyle = "blue"
    ctx.fillRect(20, 150, 50, 50)

    # Draw enemy base
    ctx.fillStyle = "red"
    ctx.fillRect(730, 150, 50, 50)


# -------------------------------
# GAME LOOP
# -------------------------------
def game_loop():
    """
    Main game loop.

    This function runs repeatedly (about 60 times per second).
    It updates the game and redraws everything.
    """

    if game_running:
        draw()


# Run the game loop every 16 ms (~60 FPS)
timer.set_interval(game_loop, 16)