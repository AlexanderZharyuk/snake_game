from turtle import Screen, Turtle
from scoreboard import FONT_SETTINGS
import time

# DIFFICULTY'S
EASY = 0.1
MEDIUM = 0.05
HARD = 0.03


def choose_difficulty():
    screen = Screen()
    user_choice = screen.textinput('CHOOSE DIFFICULT', 'TYPE EASY/MEDIUM/HARD').lower()
    if user_choice == 'medium':
        DIFFICULT = MEDIUM
        return DIFFICULT
    elif user_choice == 'hard':
        DIFFICULT = HARD
        return DIFFICULT
    else:
        DIFFICULT = EASY
        return DIFFICULT


def ready_count():
    ready = Turtle()
    ready.penup()
    ready.color('white')
    ready.hideturtle()
    ready.goto(0, 0)
    count = 3
    for _ in range(3):
        ready.clear()
        ready.write(count, align='center', font=FONT_SETTINGS)
        time.sleep(1)
        count -= 1
    ready.clear()
