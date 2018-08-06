
import turtle
turtle.goto(0,0)

UP = 0
direction = None
DOWN= 1
LEFT=2
RIGHT=3

def up():
    global direction
    print("You pressed the up key.")
    direction= UP
    print(direction)
    on_move()
    
turtle.onkey(up, "Up") 
turtle.listen()

def down():
    global direction
    direction= DOWN
    print ("you pressed the down key.")
    print(direction)
    on_move()
    
turtle.onkey(down, "Down")
turtle.listen()
 
def left():
    global direction
    direction= LEFT
    print ("you pressed the left key.")
    print(direction)
    on_move()
    
turtle.onkey(left, "Left")
turtle.listen()

def right():
    global direction
    direction= RIGHT
    print ("you pressed the right key.")
    print(direction)
    on_move()
turtle.onkey(right, "Right")
turtle.listen()

def on_move():
    #to do
    global direction
    x, y = turtle.pos()
    if direction==0:
        turtle.goto(x, y+100)
    elif direction==1:
        turtle.goto(x, y-100)
    elif direction==2:
        turtle.goto(x-100, y)
    elif direction==3:
        turtle.goto(x+100, y)

        
    


turtle.mainloop()
