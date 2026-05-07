from utils import *

# Section 1 - Variables
x1 = -100
y1 = 150
x2 = -100
y2 = 50
x3 = -100
y3 = -30
x4 =-100
y4 =-120
# # shows where the sprites are located on the graph

# Section 2 - Setup
set_background("pier")
t1 = create_sprite("alien.gif",x1,y1)
t2 = create_sprite("lizzo.gif",x2,y2)
t3 = create_sprite("grandma.gif",x3,y3)
t4 = create_sprite("quenlin.gif",x4,y4)
# # Section 3 - Racing
for i in range(30):
    x1 += random.randint(7,30)
    # # x1 goes either 7 or 30! second fastest or fastest sprite.
    x2 += random.randint(10,29)
    # # x2 goes either 10 or 29! the fastest or second fastest sprite!
    x3 += random.randint(8,17)
    # # x3 goes either 8 or 17! the second fastest or fourth fastest sprite!
    x4 += random.randint(3,20)
    # # x4 goes either 3 or 20! slowest or third fastest sprite!
    t1.goto(x1, y1)
    t2.goto(x2, y2)
    t3.goto(x3, y3)
    t4.goto(x4, y4)
    window.update()
    time.sleep(0.1)
# # Section 4 - Winner
s5 = create_sprite("alien",-200,-200)

if x1 >= x2 and x1 >= x3 and x1 >= x4:
    s5.write("alien wins!")
elif x2 >= x1 and x2 >= x3 and x2 >= x4:
    t2.write("lizzo wins!")
elif x3 >= x1 and x3 >= x2 and x3 >= x4:
    t3.write("grandma wins!")
elif x4 >= x1 and x4 >= x2 and x4 >= x3:
    t4.write("quen wins!")
turtle.exitonclick()