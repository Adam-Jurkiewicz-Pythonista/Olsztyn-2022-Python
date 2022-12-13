import pgzrun
from random import randint

WIDTH = 640
HEIGHT = 425
TITLE = "Moja gra"
kroki = 3


class Bohater:
    def __init__(self, hero, keyb, krok):
        self.my_actor = hero
        self.u, self.d, self.l, self.r = tuple(keyb)
        self.step = kroki
        self.my_actor.pos = ( randint(kroki, 600) , randint(kroki, 400) )

    def draw(self):
        self.my_actor.draw()

    def move(self, key_keyboard):
        if key_keyboard == self.u:
            self.my_actor.y -= self.step
        if key_keyboard == self.d:
            self.my_actor.y += self.step
        if key_keyboard == self.l:
            self.my_actor.x -= self.step
        if key_keyboard == self.r:
            self.my_actor.x += self.step
        # teraz trzeba od razu zdefiniować odbicie
        # if self.my_actor.x ...

santa = Bohater( Actor("santa-claus.png"), "wsad", 10)
beetle = Bohater( Actor("beetle.png"), "ikjl", 2)

def on_key_down(key):
    key_str = str(key)[-1:].lower()
    if key_str in "wsad":
        santa.move(key_str)
    if key_str in "ijkl":
        beetle.move(key_str)



def update():
   pass

def draw():
    screen.blit("beach.jpg", (0,0) )
    santa.draw()
    beetle.draw()

pgzrun.go()