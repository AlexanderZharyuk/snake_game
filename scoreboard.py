from turtle import Turtle

FONT_SETTINGS = ('Comic Sans MS', 16, 'bold')


def check_high_score_from_file():
    with open('high_score.txt', 'r') as file:
       number = file.read()
    return int(number)


def rewrite_high_score(number):
    with open('high_score.txt', 'w') as file:
        file.write(f'{number}')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.user_score = 0
        self.high_score = check_high_score_from_file()
        self.start_score_position()

    def start_score_position(self):
        self.goto(0, 270)
        self.pendown()
        self.color('white')
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'SCORE: {self.user_score} | HIGH SCORE: {self.high_score}', align='center', font=FONT_SETTINGS)

    def increase_score(self):
        self.clear()
        self.user_score += 1
        self.update_scoreboard()

    def reset(self):
        if self.user_score > self.high_score:
            self.high_score = self.user_score
            rewrite_high_score(self.high_score)
        self.user_score = 0
        self.update_scoreboard()

