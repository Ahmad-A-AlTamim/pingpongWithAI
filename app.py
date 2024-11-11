import turtle
import time

# Initialize screen
wind = turtle.Screen()
wind.cv._rootwindow.resizable(False, False)
wind.title("Ping Pong")
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0)

# Player 1 (Manual)
player1 = turtle.Turtle()
player1.speed(0)
player1.shape("square")
player1.color("red")
player1.penup()
player1.goto(-350, 0)
player1.shapesize(stretch_wid=6, stretch_len=1)

# Player 2 (Automated, easier)
player2 = turtle.Turtle()
player2.speed(6)
player2.shape("square")
player2.color("blue")
player2.penup()
player2.goto(350, 0)
player2.shapesize(stretch_wid=6, stretch_len=1)

# Ball
ball = turtle.Turtle()
ball.speed(1)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 7
ball.dy = 7

# Score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player1 : 0 || Player2 : 0", align="center", font=("Courier", 24, "normal"))

# Player movement variables
player1_moving_up = False
player1_moving_down = False

# Functions for Player 1
def player1_up():
    global player1_moving_up
    player1_moving_up = True

def player1_down():
    global player1_moving_down
    player1_moving_down = True

def player1_up_release():
    global player1_moving_up
    player1_moving_up = False

def player1_down_release():
    global player1_moving_down
    player1_moving_down = False

# Keyboard bindings for Player 1
wind.listen()
wind.onkeypress(player1_up, "w")
wind.onkeyrelease(player1_up_release, "w")
wind.onkeypress(player1_down, "s")
wind.onkeyrelease(player1_down_release, "s")

# Function to display winner and exit game
def display_winner(winner):
    score.clear()
    score.goto(0, 0)
    score.write(f"{winner} Wins!", align="center", font=("Courier", 36, "bold"))
    wind.update()
    time.sleep(5)
    wind.bye()

# Game loop
try:
    while True:
        wind.update()

        # Move Player 1 if keys are held down
        if player1_moving_up:
            y = player1.ycor()
            if y < 250:
                y += 5.5  # Slower paddle speed
            player1.sety(y)

        if player1_moving_down:
            y = player1.ycor()
            if y > -250:
                y -= 5.5  # Slower paddle speed
            player1.sety(y)

        # Move ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border collision
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        # Score update
        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
            score1 += 1
            score.clear()
            score.write(f"Player1 : {score1} || Player2 : {score2}", align="center", font=("Courier", 24, "normal"))
        
        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            score2 += 1
            score.clear()
            score.write(f"Player1 : {score1} || Player2 : {score2}", align="center", font=("Courier", 24, "normal"))

        # Check for winning score
        if score1 == 10:
            display_winner("Player 1")
            break
        elif score2 == 10:
            display_winner("Player 2")
            break

        # Player 2 (AI) movement, slower and easier
        if player2.ycor() < ball.ycor() and abs(player2.ycor() - ball.ycor()) > 15:
            player2.sety(player2.ycor() + 6)  # Slower AI paddle movement
        elif player2.ycor() > ball.ycor() and abs(player2.ycor() - ball.ycor()) > 15:
            player2.sety(player2.ycor() - 6)  # Slower AI paddle movement

        # Paddle collision with extended collision area to capture corner hits
        if (340 < ball.xcor() < 360) and (player2.ycor() - 70 < ball.ycor() < player2.ycor() + 70):
            ball.setx(340)
            ball.dx *= -1
        
        if (-360 < ball.xcor() < -340) and (player1.ycor() - 70 < ball.ycor() < player1.ycor() + 70):
            ball.setx(-340)
            ball.dx *= -1

        # Slight delay to control overall game speed
        time.sleep(0.02)

except turtle.Terminator:
    print("Game exited.")
