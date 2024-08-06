import turtle as t
list1 = ["yellow","red","blue","green"]
t.up()
t.goto(200,0)
#pattern 1
for i in range(4):
    t.down()
    t.begin_fill()
    t.fillcolor(list1[i])
    t.circle(100)
    t.end_fill()
    t.up()
    t.bk(100)
t.reset()
    
#pattern 2
t.up()
t.goto(200,0)
for i in range(4):
    t.down()

    t.color(list1[i])
    t.pensize(20)
    t.circle(100)
    t.end_fill()
    t.up()
    t.bk(100)
t.reset()

#pattern 3    

