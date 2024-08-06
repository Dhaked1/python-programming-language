import turtle as t
t.circle(100)
t.undo()
t.right(90)
t.forward(100)
t.left(90)
t.circle(90)
t.reset()
#we can do this work by using goto in one line
t.goto(0,-100)
t.circle(100)
#up and down method
t.up()
t.goto(0,-100)
t.circle(100)
t.down()
t.circle(100)
t.reset()
t.up()
t.goto(100,100)
t.down()
t.circle(100)

