from asyncore import write
import random
import turtle
from pynput import keyboard

turtle.setup(width=1920, height=1080)
turtle.hideturtle()
turtle.penup()
turtle.bgcolor("yellow")
turtle.goto(0,-40)
turtle.pensize(60)
turtle.speed(0)

pos_pin = [(0,-300), (-200,-100), (200,-100), (-400,100),(0,100),(400,100),(-600,300),(-200,300),(200,300),(600,300)]
score = 0

def writescore(n):
    global score
    if pos[n-1]=='black':
        score += 4
    elif pos[n-1]=='red':
        score += 3
    elif pos[n-1]=='blue':
        score += 2
    elif pos[n-1]=='white':
        score += 1
    else:
        pass
    turtle.penup()
    turtle.goto(800,450)
    turtle.pendown()
    turtle.pencolor("yellow")
    turtle.pensize(100)
    turtle.circle(100)
    turtle.pencolor("black")
    turtle.write(score, move=False, align="center", font=("Arial", 40, "bold"))
    turtle.penup()

def ran():
    global pos
    global score
    score = 0

    turtle.clear()
    turtle.pensize(60)
    black_pos = random.randrange(0,2)

    pos = ['red','red','red','blue','blue','blue','white','white','white']
    random.shuffle(pos)

    if black_pos==1:
        pos.insert(6,'black')
    else:
        pos.insert(9,'black')

    print(pos,black_pos)

    i=0
    for color in pos:
        if color=='black':
            turtle.pencolor("black")
        elif color=='blue':
            turtle.pencolor("blue")
        elif color=='red':
            turtle.pencolor("red")
        elif color=='white':
            turtle.pencolor("white")
        
        turtle.goto(pos_pin[i])
        turtle.pendown()
        turtle.circle(30)
        turtle.pencolor("yellow")
        turtle.write(i+1,move=False, align="center", font=("Arial", 40, "normal"))
        turtle.penup()

        i=i+1
    
    turtle.pencolor("black")
    turtle.pensize(30)
    turtle.penup()
    turtle.goto(0,-500)
    turtle.pendown()
    turtle.write("스페이스바를 눌러 새로고침", move=False, align="center", font=("Arial", 20, "normal"))
    turtle.penup()

    turtle.penup()
    turtle.goto(800,450)
    turtle.pendown()
    turtle.pencolor("yellow")
    turtle.pensize(100)
    turtle.circle(100)
    turtle.pencolor("black")
    turtle.write(score, move=False, align="center", font=("Arial", 40, "bold"))
    turtle.penup()

ran()

def erase1():
    turtle.penup()
    turtle.pensize(40)
    turtle.goto(pos_pin[0])
    turtle.pencolor("yellow")
    turtle.pendown()
    turtle.circle(30)
    turtle.penup()
    writescore(1)

def erase2():
    turtle.penup()
    turtle.pensize(40)
    turtle.goto(pos_pin[1])
    turtle.pencolor("yellow")
    turtle.pendown()
    turtle.circle(30)
    turtle.penup()
    writescore(2)

def erase3():
    turtle.penup()
    turtle.pensize(40)
    turtle.goto(pos_pin[2])
    turtle.pencolor("yellow")
    turtle.pendown()
    turtle.circle(30)
    turtle.penup()
    writescore(3)

def erase4():
    turtle.penup()
    turtle.pensize(40)
    turtle.goto(pos_pin[3])
    turtle.pencolor("yellow")
    turtle.pendown()
    turtle.circle(30)
    turtle.penup()
    writescore(4)

def erase5():
    turtle.penup()
    turtle.pensize(40)
    turtle.goto(pos_pin[4])
    turtle.pencolor("yellow")
    turtle.pendown()
    turtle.circle(30)
    turtle.penup()
    writescore(5)

def erase6():
    turtle.penup()
    turtle.pensize(40)
    turtle.goto(pos_pin[5])
    turtle.pencolor("yellow")
    turtle.pendown()
    turtle.circle(30)
    turtle.penup()
    writescore(6)

def erase7():
    turtle.penup()
    turtle.pensize(40)
    turtle.goto(pos_pin[6])
    turtle.pencolor("yellow")
    turtle.pendown()
    turtle.circle(30)
    turtle.penup()
    writescore(7)

def erase8():
    turtle.penup()
    turtle.pensize(40)
    turtle.goto(pos_pin[7])
    turtle.pencolor("yellow")
    turtle.pendown()
    turtle.circle(30)
    turtle.penup()
    writescore(8)

def erase9():
    turtle.penup()
    turtle.pensize(40)
    turtle.goto(pos_pin[8])
    turtle.pencolor("yellow")
    turtle.pendown()
    turtle.circle(30)
    turtle.penup()
    writescore(9)

def erase10():
    turtle.penup()
    turtle.pensize(40)
    turtle.goto(pos_pin[9])
    turtle.pencolor("yellow")
    turtle.pendown()
    turtle.circle(30)
    turtle.penup()
    writescore(10)


turtle.onkeypress(erase1,"1")
turtle.onkeypress(erase2,"2")
turtle.onkeypress(erase3,"3")
turtle.onkeypress(erase4,"4")
turtle.onkeypress(erase5,"5")
turtle.onkeypress(erase6,"6")
turtle.onkeypress(erase7,"7")
turtle.onkeypress(erase8,"8")
turtle.onkeypress(erase9,"9")
turtle.onkeypress(erase10,"0")
turtle.onkeypress(ran, "space")


turtle.listen()
turtle.mainloop()