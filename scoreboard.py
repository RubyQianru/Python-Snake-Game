from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.read_high_score()
        self.scoreboard_update()

    def scoreboard_update(self):
        self.clear()
        self.color("pink")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align="center",
                   font=("Arial", 12, "normal"))


    def mark_score(self):
        self.score += 1
        self.scoreboard_update()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        # self.mark_score()
        self.scoreboard_update()
        self.store_high_score()

    def store_high_score(self):
        with open("high_score.txt", mode="w") as file:
            file.write(str(self.high_score))

    def read_high_score(self):
        with open("high_score.txt") as file:
            contents = file.read()
            self.high_score = int(contents)


    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", move=False, align="center", font=("Arial", 12, "normal"))

