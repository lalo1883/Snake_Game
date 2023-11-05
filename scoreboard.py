from turtle import *

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as score:
            self.highscore = int(score.read())
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.updateScoreBoard()
        self.hideturtle()


    def updateScoreBoard(self):
        self.clear()
        self.write(f'Your score is: {self.score} Highscore: {self.highscore}', align='center', font=('Arial', 20, 'normal'))


    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('data.txt', mode='w') as score:
                score.write(f'{self.highscore}')
        self.score = 0
        self.updateScoreBoard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f'GAME OVER :(', align='center', font=('Arial', 20, 'normal'))


    def addPoints(self):
        self.score += 1
        self.updateScoreBoard()