import pgzrun
from random import randint

WIDTH = 640
HEIGHT = 425
TITLE = "Moja gra"
kroki = 3


class Bohater:
    def __init__(self, hero, keyb, krok):
        self.my_actor = hero
        self.my_actor.pos = ( randint(kroki, 600) , randint(kroki, 400) )

    def draw(self):
        self.my_actor.draw()

santa = Bohater( Actor("santa-claus.png"), "wasd", 10)
beetle = Bohater( Actor("beetle.png"), "tfgh", 2)

def update():
   pass

def draw():
    screen.blit("beach.jpg", (0,0) )
    santa.draw()
    beetle.draw()

pgzrun.go()