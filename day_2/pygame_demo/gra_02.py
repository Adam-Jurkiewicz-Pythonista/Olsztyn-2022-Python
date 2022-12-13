from random import randint
# Wczytujemy moduł pgzrun
import pgzrun
import sys

# Definiujemy klasy i funkcje dodatkowe

# Start programu
WIDTH = 1280
HEIGHT = 853
TITLE = "PONG - najlepsza gra na świecie ;-)"

hero = Actor("santa-claus.png")
hero.x = randint(10, WIDTH - 100)
hero.y = randint(10, HEIGHT - 100)

hero2 = Actor("beetle.png")
hero2.x = randint(10, WIDTH - 100)
hero2.y = randint(10, HEIGHT - 100)

def check_keyboard():
    if keyboard.right:
        hero.x += 20
    if keyboard.left:
        hero.x -= 20
    if keyboard.up:
        hero.y -= 20
    if keyboard.down:
        hero.y += 20

    if keyboard.d:
        hero2.x += 20
    if keyboard.a:
        hero2.x -= 20
    if keyboard.w:
        hero2.y -= 20
    if keyboard.s:
        hero2.y += 20

def check_win():
    odleglosc = hero.distance_to(hero2)
    if odleglosc < 30:
        print("Winner!")
        sys.exit(0)
    else:
        print(f"Odległość: {odleglosc} pixeli.")
        
# Najważniejsze funkcje sterujące
def update():
    check_keyboard()
    check_win()


def draw():
    screen.blit("nature-2384_1280.jpg", (0, 0))
    hero2.draw()
    hero.draw()
    


# Uruchomienie modułu Pygame Zero
pgzrun.go()
