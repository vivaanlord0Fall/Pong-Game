import turtle
import winsound 
wnd = turtle.Screen()
wnd.title("Pong by vivaanlord0Fall")
wnd.bgpic("background.gif")
wnd.setup(width=700, height=500)
wnd.tracer(0)
score_a = 0
score_b = 0

padleft = turtle.Turtle()
padleft.speed(0)
padleft.shape("square")
padleft.color("white")
padleft.shapesize(stretch_wid=5, stretch_len=1)
padleft.penup()
padleft.goto(-300, 25)

padright = turtle.Turtle()
padright.speed(0)
padright.shape("square")
padright.color("white")
padright.shapesize(stretch_wid=5, stretch_len=1)
padright.penup()
padright.goto(300, 25)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 25)
ball.dx = 0.25
ball.dy = 0.25

score_statement = turtle.Turtle()
score_statement.speed(0)
score_statement.color("white")
score_statement.penup()
score_statement.hideturtle()
score_statement.goto(0, 175)
score_statement.write("{}         {}".format(score_a, score_b), align= "center", font= ("Wide Latin", 25, "normal"))

def padleft_up():
    y=padleft.ycor()
    y+=20
    padleft.sety(y)

wnd.listen()
wnd.onkeypress(padleft_up, "w")

def padleft_down():
    y=padleft.ycor()
    y-=20
    padleft.sety(y)

wnd.listen()
wnd.onkeypress(padleft_down, "s")

def padright_up():
    y=padright.ycor()
    y+=20
    padright.sety(y)

wnd.listen()
wnd.onkeypress(padright_up, "Up")

def padright_down():
    y=padright.ycor()
    y-=20
    padright.sety(y)

wnd.listen()
wnd.onkeypress(padright_down, "Down")
  
while True:
    wnd.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
        
    if ball.ycor() > 225:
        ball.sety(225)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -215:
        ball.sety(-215)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 335:
        ball.dx = -0.2
        padleft.goto(-300, 25)
        padright.goto(300, 25)
        ball.goto(0, 25)
        score_a += 1
        score_statement.clear()
        score_statement.write("{}         {}".format(score_a, score_b), align= "center", font= ("Wide Latin", 25, "normal"))

    if ball.xcor() < -335:
        ball.dx = 0.2
        padleft.goto(-300, 25)
        padright.goto(300, 25)
        ball.goto(0, 25)
        score_b += 1
        score_statement.clear()
        score_statement.write("{}         {}".format(score_a, score_b), align= "center", font= ("Wide Latin", 25, "normal"))
                
    ball_x_int= int(ball.xcor())
    ball_y_int= int(ball.ycor())
    if (ball_x_int>290 and ball_x_int<300) and (ball_y_int < padright.ycor() + 50 and ball_y_int > padright.ycor() - 50):
        ball.dx *= -1
        ball.setx(290)
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (ball_x_int<-290 and ball_x_int>-300) and (ball_y_int < padleft.ycor() + 50 and ball_y_int > padleft.ycor() - 50):
        ball.dx *= -1
        ball.setx(-290)
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
            
    if score_a == 11:
        score_statement.clear()
        score_statement.goto(0, 25)
        wnd.bgpic("black.gif")
        ball.color("black")
        padleft.color("black")
        padright.color("black")
        score_statement.write("Player 1 wins!", align= "center", font= ("Wide Latin", 25, "normal"))
        ball.dx = 0
        ball.dy = 0
            
    if score_b == 11:
        score_statement.clear()
        score_statement.goto(0, 25)
        wnd.bgpic("black.gif")
        ball.color("black")
        padleft.color("black")
        padright.color("black")
        score_statement.write("Player 2 wins!", align= "center", font= ("Wide Latin", 25, "normal"))
        ball.dx = 0
        ball.dy = 0
            
    if padright.ycor() > 205:
        padright.sety(205)
            
    if padright.ycor() < -195:
        padright.sety(-195)

    if padleft.ycor() > 205:
        padleft.sety(205)
            
    if padleft.ycor() < -195:
        padleft.sety(-195)