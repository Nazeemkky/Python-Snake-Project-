from turtle import Turtle

TOTAL_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_SNAKE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.statement = []
        self.create_snake()
        self.head = self.statement[0]

    def create_snake(self):
        for position in TOTAL_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        tim = Turtle("square")
        tim.color("white")
        tim.penup()
        tim.goto(position)
        self.statement.append(tim)

    def extend(self):
        self.add_segment(self.statement[-1].position())

    def move(self):
        for state in range(len(self.statement) - 1, 0, -1):
            new_x = self.statement[state - 1].xcor()
            new_y = self.statement[state - 1].ycor()
            self.statement[state].goto(new_x, new_y)
        self.head.forward(MOVE_SNAKE)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
