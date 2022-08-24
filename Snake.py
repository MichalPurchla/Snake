from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_segments = self.create_snake()
        self.head = self.snake_segments[0]



    def create_snake(self):
        tmp_snake = [Turtle('square') for i in range(3)]
        for idx, element in enumerate(tmp_snake):
            element.color('white')
            element.penup()
            element.goto(x=idx * -20, y=0)
        return tmp_snake

    def move(self):
        for seg_number in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[seg_number-1].xcor()
            new_y = self.snake_segments[seg_number-1].ycor()
            self.snake_segments[seg_number].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def reset(self):
        for seg in self.snake_segments:
            seg.goto(1000, 1000)
        self.snake_segments.clear()
        self.snake_segments = self.create_snake()
        self.head = self.snake_segments[0]

    def new_segment(self):
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(self.snake_segments[-1].xcor(),self.snake_segments[-1].ycor())
        self.snake_segments.append(new_segment)
