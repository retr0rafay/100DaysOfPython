from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.scores = []
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def reset(self):
        self.clear()
        with open('highscores.txt') as file:
            contents = file.read()
            self.high_score = int(contents)
        if self.score > self.high_score:
            self.high_score = self.score
            with open('highscores.txt', mode='w') as file:
                file.write(f'{self.high_score}')
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        with open('highscores.txt') as file:
            self.write(f"Score: {self.score} High Score: {file.read()}", align='center',
                       font=('Arial', 24, 'normal'))
        return

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
