import turtle

if __name__ == "__main__":
    turtle.shape("turtle")
    for _ in range(5):
        for _ in range(2):
            turtle.forward(40)
            turtle.right(60)
            turtle.forward(40)
            turtle.right(120)
        turtle.right(90)
    turtle.exitonclick()
    