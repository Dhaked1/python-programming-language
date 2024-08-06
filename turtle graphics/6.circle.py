import turtle as t
t.begin_fill()
wn = t.Screen()
wn.bgcolor("green")
t.begin_fill()
t.fillcolor("yellow")
t.circle(20)#radius is +ve so draw circle counter clockwise direction
t.circle(-50)
t.end_fill()
t.reset()#it will set the turtle to its home position
t.circle(100,180)#for semicircle
t.reset()
t.circle(100,steps = 3)
t.reset()
t.circle(70,steps = 5)
t.reset()
t.circle(90,steps=10)

