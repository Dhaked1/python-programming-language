import turtle as t

list1 = ['orange', 'purple', 'red', 'blue', 'black']
t.speed(0)  # Set the turtle speed to the maximum
for i in range(300):
    t.color(list1[i % 5])
    s = i // 10 + 1
    t.pensize(s)  
    t.forward(i)
    t.left(59)

t.done()  
