from turtle import *
from random import randint
import time

# Screen
screen = Screen()
screen.bgcolor("light blue")
screen.title("Catch The Turtle")
screen.setup(500, 500)

# Turtle
turtle_instance = Turtle()
turtle_instance.shape("turtle")
turtle_instance.penup()
turtle_instance.speed("fastest")

# Score
score = 0
style = ("courier", 20, "italic")

score_writer = Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(150, 200)

# Timer
timer = 10

timer_writer = Turtle()
timer_writer.hideturtle()
timer_writer.penup()
timer_writer.goto(-150, 200)

# Score functions
def update_score():
    score_writer.clear()
    score_writer.write(f"Score: {score}", font=style, align="center")

def increase_score(x, y):
    global score
    score += 1
    update_score()

# Timer functions
def update_timer():
    global timer
    timer_writer.clear()
    timer_writer.write(f"Time: {timer}", font=style, align="center")
    if timer > 0:
        timer -= 1
        screen.ontimer(update_timer, 1000)
    else:
        game_over()

# Turtle function to move it randomly
def move_turtle():
    if timer > 0:
        turtle_instance.hideturtle()
        turtle_instance.goto(randint(-200, 200), randint(-200, 200))
        turtle_instance.showturtle()
        screen.ontimer(move_turtle, 500)

# Game Over!
def game_over():
    turtle_instance.hideturtle()
    timer_writer.goto(0, 0)
    timer_writer.write("Game Over!", font=("courier", 30, "bold"), align="center")

# Function that triggers score increment
turtle_instance.onclick(increase_score)

# Calling functions
update_score()
update_timer()
move_turtle()

screen.mainloop()
