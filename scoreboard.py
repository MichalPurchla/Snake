from turtle import Turtle
ALIGMENT = 'center'
FONT = ('Arial', 12)
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(x=0, y = 280)
        self.highest_result = 0
        self.read_highest_score()
        self.display_score()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.check_highest_result()
        self.display_score()

    def check_highest_result(self):
        if self.score >= self.highest_result:
            self.highest_result = self.score

    def display_score(self):
        self.clear()
        self.write(f'Score: {self.score}      Highest score: {self.highest_result}', move=False, align=ALIGMENT, font=FONT)

    def game_over(self):
        # self.goto(0,0)
        # self.write(f'GAME OVER', move=False, align=ALIGMENT, font=FONT)
        self.save_highest_score()
        self.reset()

    def read_highest_score(self):
        with open('highest_score.txt', 'r') as reader:
            try:
                self.highest_result = int(reader.read())
            except ValueError:
                self.highest_result = 0

    def reset(self):
        self.score = 0
        self.display_score()

    def save_highest_score(self):
        with open('highest_score.txt', 'w') as writer:
            writer.write(str(self.score))

