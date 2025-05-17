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
madrab2.goto(350 , 0)   # The Olace of the shabe


#  The ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0  , 0 )
# continue--------------------------------
# ---------------------Moving The objects-------------------





















# makeing The Game loop and update The Game every open


while True:
    wind.update() # again update window every open







