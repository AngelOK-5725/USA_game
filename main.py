'''30.06'''
import os
os.system('cls')

import pandas

data = pandas.read_csv('./USA_game/Archive/50_states.csv')

st_name = data.state
st_list = data.state.to_list()
image = './USA_game/Archive/blank_states_img.gif'


# --------------------------------------------------------------------------------
from turtle import Turtle, Screen 
import turtle
screen = Screen()

screen.title('USA_game')
screen.setup(725,491)
screen.bgpic('./USA_game/Archive/blank_states_img.gif')  # можно так (устанавливаем каринку как фон)
# screen.addshape(image) # а можно так  (добавляем картинку как фигуру)
# turtle.shape(image)
# -------------------------------------------------

user = ''
score = 0 
while user != "Stop":
    user = screen.textinput(title= f"{score}/50 State" , prompt= "Enter State name: ").title()


    if user in st_list:
        score += 1
        current_state = data[data.state == user]
        new_x = int(current_state.x)
        new_y = int(current_state.y)
        tom = Turtle()
        tom.penup()
        tom.hideturtle()
        tom.goto(new_x, new_y)
        tom.write(user)    


    if score == 50:
        user = "Stop"



print(st_name)
# -------------------------------------------------
screen.exitonclick()