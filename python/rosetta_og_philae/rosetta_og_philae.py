import math
import turtle

gravitasjon = -0.01
romskip = {
    'fart_x': 0.1,
    'fart_y': 0.5
}

def tegn_bakgrunn():
    turtle.bgcolor('black')
    turtle.speed(11)
    turtle.pensize(10)
    turtle.penup()
    turtle.setposition(-400, -300)
    turtle.pendown()
    turtle.color('grey')
    turtle.forward(200)
    turtle.color('red')
    turtle.forward(200)
    turtle.color('grey')
    turtle.forward(400)


def tegn_romskip():
    turtle.penup()
    turtle.shapesize(4)
    turtle.setpos(200, 400)
    turtle.setheading(90)
    turtle.color('blue')

    turtle.onkey(snu_hoyre, 'Right')
    turtle.onkey(snu_venstre, 'Left')
    turtle.onkey(bruk_motor, 'Up')
    turtle.listen()


def snu_hoyre():
    turtle.right(5)


def snu_venstre():
    turtle.left(5)


def bruk_motor():
    vinkel = turtle.heading() * math.pi / 180.0
    romskip['fart_x'] += math.cos(vinkel)
    romskip['fart_y'] += math.sin(vinkel)


def fly_romskip():
    while True:
        x, y = turtle.position()
        if y < -270:
            return

        romskip['fart_y'] += gravitasjon
        turtle.setposition(x + romskip['fart_x'],
                           y + romskip['fart_y'])


def sjekk_landing():
    x = turtle.xcor()
    vinkel = turtle.heading()

    if x < -200 or x > 0:
        print('Du landet utenfor basen!')
    elif abs(vinkel - 90) > 10:
        print('Du landet skjevt!')
    elif romskip['fart_y'] < -1:
        print('Du landet for hardt!')
    else:
        print('Perfekt landing!')


tegn_bakgrunn()
tegn_romskip()
fly_romskip()
sjekk_landing()
input('Trykk Enter')
