import turtle

# Creating car's body
turtle.color(1, 0, 0)
turtle.begin_fill()
turtle.forward(120)
turtle.left(90)
turtle.forward(40)
turtle.left(90)
turtle.forward(40)
turtle.right(90)
turtle.forward(40)
turtle.left(90)
turtle.forward(80)
turtle.left(90)
turtle.forward(40)
turtle.right(90)
turtle.forward(40)
turtle.left(90)
turtle.forward(40)
turtle.end_fill()

# Creating a front wheel
turtle.color(0, 0, 0)
turtle.up()
turtle.forward(30)
turtle.down()
turtle.begin_fill()
turtle.circle(30)
turtle.end_fill()

# Creating a back wheel
turtle.setheading(0)
turtle.up()
turtle.forward(120)
turtle.right(90)
turtle.forward(30)
turtle.setheading(0)
turtle.begin_fill()
turtle.down()
turtle.circle(30)
turtle.end_fill()

turtle.done()
