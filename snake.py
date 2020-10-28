from turtle import *
from random import randrange, choice
import random
from freegames import square, vector

colordot = random.randint(0,4)
colorsnake = random.randint(0,4)

while colorsnake == colordot:
    colorsnake = random.randint(0, 4)

color = ['blue', 'green', 'purple', 'orange', 'black']
color1 = ['blue', 'green', 'purple', 'orange', 'black']

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)
    

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, color[colordot])

    square(food.x, food.y, 9, color1[colorsnake])
    update()
    ontimer(move, 100)
def movefood():
    while food in range(420,420):
        food.x += randrange(-10,11,10) 
        food.y += randrange(-10,11,10)
        ontimer(movefood, 500)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
movefood()
done()
