import turtle  # module for making the game

wind =  turtle.Screen()  # declere vrible and store it in class screem
wind.title("This Ping Pong Game Created By bo7hmeeed:)") #game titile
wind.bgcolor("black") # game color
wind.setup(width=800, height=600) # make cusomatztion about window
wind.tracer(0) # prevent The Window from update itself every open game


#  create The objects  in Screen
# madrab1
# madrab2
# ball

madrab1 =  turtle.Turtle() # making opjects in this class
madrab1.speed(0)  # speed for opject
madrab1.color("blue") # color for opjects
madrab1.shape("square")  # shape desgin
madrab1.shapesize(stretch_wid=6 , stretch_len=1)
#  making the default shabe multibletion 6 * 20 default
madrab1.penup()
# prevent the shape from kaing shadow
madrab1.goto(-350 , 0)   # The Olace of the shabe

madrab2 =  turtle.Turtle() # making opjects in this class
madrab2.speed(0)  # speed for opject
madrab2.color("red") # color for opjects
madrab2.shape("square")  # shape desgin
madrab2.shapesize(stretch_wid=6 , stretch_len=1)
#  making the default shabe multibletion 6 * 20 default
madrab2.penup()
# prevent the shape from kaing shadow
madrab2.goto(350 , 0)   # The place of the shabe


#  The ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0  , 0 )
ball.dx =0.1  # fast of the shape when game start
ball.dy =0.1 #--------------------------------



def madrab1_up():  # making the basic funcation for move the nadrib
    y = madrab1.ycor() # get the location of y cordent in thes moment
    # and move the mdribe in the same cordente
    y +=20   # from the same location add 20 to madrib 1 at current locarion
    madrab1.sety(y)  #  set the new location in madrib1
def madrab1_down():
    y = madrab1.ycor()
    y -= 20   # decreess the location in same codinete at same value
    madrab1.sety(y)
def madrab2_up():
    y = madrab2.ycor()
    y +=20
    madrab2.sety(y)

def madrab2_down():
    y = madrab2.ycor()
    y -=20
    madrab2.sety(y)


wind.listen()   # when user input any thing in output screen

wind.onkeypress(madrab1_up, "w")  # when the windown lissten w start the funcation
wind.onkeypress(madrab1_down, "s") # when the windown l
wind.onkeypress(madrab2_up, "Up")
wind.onkeypress(madrab2_down, "Down")















# continue--------------------------------
# ---------------------Moving The objects-------------------





















# makeing The Game loop and update The Game every open


while True:
    wind.update() # again update window every open
    ball.setx(ball.xcor() + ball.dx)  # calc the location of ball and get change every start the game lopp
    ball.sety(ball.ycor() + ball.dy)  #calc the location of ball and get change every start the game lopp

    # check the ball go to broders of x , y any test value clalced by widthe and height
    if ball.ycor() > 290:
        ball.sety(290) # get the new cordinests when ball move
        ball.dy *=-1 # change the new speed of ball
    if ball.ycor() < -290: # same thing but when in negitive codients of y
        ball.sety(-290)
        ball.dy *=-1
    # ==================================================
    if ball.xcor() > 400: # check in x codinets
        ball.goto(0 ,0 ) # when go to x axcies retun to defalt location
        ball.dx *=-1

    if ball.xcor() < -400: # same but in negitave
        ball.goto(0 ,0) # retun to 0  ,  9
        ball.dx *=-1























