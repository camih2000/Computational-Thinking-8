from utils import *

# Section 1 - setup
# You feed Mike to the Blair Witch to keep her health stable, and if you don't, you DIE. 

# TODO - create at least two variables and set their starting value. ex: cookies = 0
set_background("grigghouse.gif")
m1 = create_sprite("blair.gif", 0,0)
mikes = 0
m3 = create_sprite("alien", -300, 170)
m3.hideturtle()
health = 100
spritelist = []


# Section 2 - controls
# TODO - define an action. e
def make_mike():
    global mikes, health
    mikes += 1
    health += 2
    if health > 100:
        health = 100
    elif health < 0:
        health = 0
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    m2 = create_sprite("mike.gif", x,y)
    time.sleep(0.1)
    spritelist.append(m2)
    for i in range(1):
        m2 = spritelist.pop()
        m2.hideturtle()
    window.update()
# TODO - choose a key to do the action. ex: window.onkeypress(my_control, "space")
window.onkeypress(make_mike, "space")
# TODO - make a second control
def get_blair():
    m1.write(f"yummy...")
    for i in range(1):
        window.update()
        time.sleep(0.5)

        m1.clear()
window.onkeypress(get_blair, "c")



# Section 3 - game loop
window.listen()
for i in range(1000000000):
    if health < 0:
        m4 = create_sprite("blairwitch.gif", 0, -300)
        time.sleep(0.3)
        quit()
    health -= 1

    # OPTIONAL - use the message sprite to say a mes
    m3.clear()
    m3.write(f"health: {health}",font = ("Arial", 40, "normal"))
    time.sleep(0.2)
    window.update()