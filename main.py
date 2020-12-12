from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "green", "blue", "yellow", "purple", "orange"]
all_turtles = []

user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? Enter a color: ")

y_pos = -120
for turtle_number in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_number])
    new_turtle.goto(x=-235, y=y_pos)
    y_pos += 50
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle is the winner.")
            else:
                print(f"You lost. The {winning_color} turtle is the winner.")
        step = random.randint(0, 10)
        turtle.forward(step)

screen.exitonclick()
