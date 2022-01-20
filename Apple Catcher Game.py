# Name: Hallie Jenkins

# Apple Catcher Game

# Purpose: Game design with functions, conditionals, and loop structures

# Certificate of Authenticity: I certify that this code is entirely
# my own work.

# Input: Mouse clicks
# Output: Gameplay

from math import *
from graphics import *
from random import *


def distance(p1,p2):
    """
    Uses the distance formula to calculate the distance between 2 points
    """
    x1 = p1.getX()
    y1 = p1.getY()
    x2 = p2.getX()
    y2 = p2.getY()
    return sqrt((x2-x1)**2 + (y2-y1)**2)


def collides(cart, apple):
    """Takes the cart and apple Circle objects and compares them to
    see if they overlap.
    Returns True if they do.
    Returns False otherwise."""
    center1 = cart.getCenter()
    center2 = apple.getCenter()

    radius1 = cart.getRadius()
    radius2 = apple.getRadius()

    d = distance(center1,center2)

    if (radius1-radius2 <= d <= radius1+radius2) \
            or (d == 0):
        return True
    else:
        return False


def hit_floor(cir,win):
    """
    :param cir: Accepts a Circle Object
    :param win: Accepts a GraphWin Object
    :return: True if the Circle Object passes the bottom limit of the
    GraphWin Object
    """
    d = win.getHeight()-(cir.getCenter().getY()+cir.getRadius())
    if d <= 0:
        return True
    else:
        return False


def hit_wall(cir,win):
    """
    :param cir: Accepts a circle Object
    :param win: Accepts a GraphWin Object
    :return: True if the Circle Object passes the side limits of
    either side of the GraphWin Object
    """
    w = win.getWidth()
    d1 = cir.getCenter().getX()-cir.getRadius()
    d2 = cir.getCenter().getX()+cir.getRadius()

    if d1 <= 0 or d2 >= w:
        return True
    else:
        return False


def create_win():
    """
    Creates Graphics window for Apple Catcher Game
    """
    win = GraphWin("Apple Catcher",900,700, autoflush=False)
    win.setBackground(color_rgb(135,206,250))
    return win


def create_cart(win,radius, height):
    """
    Creates a cart to catch apples for Apple Catcher Game

    :param win: Graphics Window
    :param radius: Radius of Circle object
    :param height: y coordinate for center Point of Circle Object
    :return: Circle object drawn on window
    """
    x = win.getWidth()/2
    cart = Circle(Point(x,height),radius)
    cart.setFill("brown")
    return cart.draw(win)


def create_tree(win):
    width = win.getWidth()
    trunk = Rectangle(Point((width / 2)-50, 45), Point((width /
                                                        2)+50,
                                                       win.getHeight()))
    trunk.setFill("brown")
    trunk.draw(win)
    for i in range(0,width+45,45):
        section = Circle(Point(i, 45), 50)
        section.setFill("green")
        section.setOutline("green")
        section.draw(win)


def create_apple(win,radius,min_height):
    """
    Creates  apples for Apple Catcher Game

    :param win: Graphics Window
    :param radius: Radius of Circle object
    :param min_height: Lowest y coordinate allowed for center Point of
    Circle Object
    :return: Circle object drawn on window
    """
    x = randrange(1,win.getWidth())
    y = randrange(1,min_height)
    apple = Circle(Point(x,y),radius)
    apple.setFill("red")
    return apple.draw(win)


def main():
    """
    Runs Apple Catcher Game
    """
    window = create_win()
    create_tree(window)
    w_height = window.getHeight()
    w_width = window.getWidth()
    ground = Rectangle(Point(0, w_height - 100), Point(
        w_width, w_height))
    ground.setFill("green")
    ground.draw(window)
    velocity = 5
    gravity = 15
    cart = create_cart(window, 50, w_height - 100)
    points = 0

    instruction_box = Rectangle(Point((w_width/2)-200,
                                (w_height/2)-150),
                                Point((w_width/2)+200,(w_height/2)+150))

    instruction_box.setFill("white")
    instruction_box.draw(window)

    instruction_text = Text(Point(w_width / 2, w_height / 2),
                            "Welcome to Apple Catcher!"
                            "\nThere are 20 apples on the apple "
                            "tree.\nThe cart will move back and "
                            "forth under the apple tree."
                            "\nClick when the the cart is under the "
                            "apple to catch it.\nClick anywhere to "
                            "start playing!")
    instruction_text.setSize(13)
    instruction_text.draw(window)

    window.getMouse()
    instruction_box.undraw()
    instruction_text.undraw()

    point_text = Text(Point(w_width/2,w_height/2), f"Score: {points}")
    point_text.setTextColor("blue")
    point_text.setStyle("bold")
    point_text.setSize(14)
    point_text.draw(window)
    while True:
        for i in range(20):
            apple = create_apple(window, 10, 50)
            while not window.checkMouse():
                if hit_wall(cart, window):
                    velocity = -velocity
                cart.move(velocity, 0)
                update()

            while (not collides(cart,apple)) and \
                    (not hit_floor(apple,window)):

                if hit_wall(cart, window):
                    velocity = -velocity
                cart.move(velocity, 0)
                apple.move(0, gravity)
                update()

                if collides(cart,apple):
                    apple.undraw()
                    points += 1
                    point_text.setText(f"Score: {points}")
                if hit_floor(apple,window):
                    apple.undraw()

        break

    game_over = Text(Point((w_width/2),(w_height/2)-30),"GAME OVER")
    game_over.setTextColor("white")
    game_over.setStyle("bold")
    game_over.setSize(24)
    point_text.setSize(24)
    game_over.draw(window)

    window.getMouse()
    window.close()


main()
