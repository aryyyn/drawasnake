print("Pick your color")
hello = input()

# adding input features
print("Enter your desired input key for forward movement : "); w = input()
print("Enter your desired input key for left movement : "); a = input()
print("Enter your desired input key for backward movement : "); s = input()
print("Enter your desired input key for right movement : "); d = input()

import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Game")

ball = turtle.Turtle()
ball.shape("circle")
ball.color(hello)
ball.shapesize(0.2)


def ball_up():
    positivex = ball.ycor()
    positivex = positivex + 5
    ball.sety(positivex)


def ball_left():
    negx = ball.xcor()
    negx = negx - 5
    ball.setx(negx)

def ball_right():
    posx = ball.xcor()
    posx = posx + 5
    ball.setx(posx)

def ball_down():
    negy = ball.ycor()
    negy = negy - 5
    ball.sety(negy)



screen.listen()
screen.onkeypress(ball_up, w)
screen.onkeypress(ball_left, a)
screen.onkeypress(ball_right, d)
screen.onkeypress(ball_down, s)

while True:
    screen.update()
