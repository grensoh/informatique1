import turtle
import time
tortue = turtle.Turtle()
tortue.speed("fastest")
color = ["black", "yellow", "red"] #couleurs pour le drapeau belge

def square(size, color): #fonction tracant un carré
    tortue.color(color)
    tortue.pendown()
    tortue.begin_fill()
    for i in range(4):
        tortue.forward(size)
        tortue.right(90)
    tortue.end_fill()
    tortue.penup()

def rectangle(width, height, colorr): #fonction tracant un rectangle
    tortue.color(colorr)
    if width < height: #on trace un rectangle vertical
        tortue.forward(width)
        tortue.pendown()
        tortue.begin_fill()
        for i in range(2):
            tortue.right(90)
            tortue.forward(height)
            tortue.right(90)
            tortue.forward(width)
        tortue.end_fill()
        tortue.penup()
    else: #on trace un rectangle horizontal
        tortue.pendown()
        tortue.begin_fill()
        for i in range(2):
            tortue.forward(width)
            tortue.right(90)
            tortue.forward(height)
            tortue.right(90)
        tortue.end_fill()
        tortue.penup()
        tortue.right(90) #on se replace pour les prochains appels de fonction
        tortue.forward(height)
        tortue.left(90)


def belgian_flag(width): #fonction tracant le drapeau belge
    width = width//3
    height = (3*width)/2 #le ratio est de 3:2
    for i in range(3):
        rectangle(width, height, color[i])

def three_color_flag(width, color1, color2, color3, is_horiz): #fonction tracant un drapeau horizontal ou vertical
    if is_horiz: #drapeau horizontal
        height = (width/3)*3/5
    else: #drapeau vertical
        height = width*3/5
        width = width/3
    rectangle(width, height, color1)
    rectangle(width, height, color2)
    rectangle(width, height, color3)

def yellow_star(angle): #fonction tracant une étoile
    tortue.color("#FFCC00")
    tortue.pendown()
    tortue.begin_fill()
    tortue.right(36)
    for i in range(5):
        tortue.right(72)
        tortue.forward(10)
        tortue.left(144)
        tortue.forward(10)
    tortue.end_fill()
    tortue.penup()
    tortue.left(36) #on se place pour les prochains appels de fonction
    tortue.right(angle)
    tortue.forward(40)
    tortue.penup()


def european_flag(width): #fonction tracant le drapeau européen
    height = width*2/3 #le ratio est 2:3
    rectangle(width, height, "#003399") #on trace un grand rectangle horizontal
    tortue.goto((width/2)+15, (-height/6)-15) #on se replace pour tracer les étoiles
    for i in range(12): #on appelle 12 fois la fonction tracant l'étoile
        yellow_star(360/12)

def all_flags(): #fonction tracant tous les drapeaux
    european_flag(400)
    tortue.goto(-300,150)
    three_color_flag(200, "#008C45", "#F4F5F0", "#CD212A", False)
    tortue.goto(-50, 150)
    three_color_flag(200, "#AE1C28", "white", "#21468B", True)
    tortue.goto(200, 150)
    three_color_flag(200, "#000000", "#DD0000", "#FFCE00", True)
    tortue.goto(450, 150)
    three_color_flag(200, "#0055A4", "white", "#EF4135", False)
    tortue.goto(-300, -300)
    tortue.right(45)
    for i in range(5): #on trace 5 drapeaux belges en arc de cercle
        three_color_flag(200, "black", "#FFD700", "#FF0000", False)
        tortue.left(25)
        tortue.forward(50)
    time.sleep(3) #on attend 3 secondes pour pouvoir admirer le travail

all_flags() #on trace tous les drapeaux
