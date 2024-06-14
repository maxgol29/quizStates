import csv
import pandas as pd
import turtle

score = 0

screen = turtle.Screen()
screen.title(f'U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
screen.screensize(400, 400)
turtle.shape(image)

data_states = pd.read_csv('50_states.csv')

states = list(data_states["state"])

text_name = turtle.Turtle()
text_name.hideturtle()
text_name.penup()


def get_mouse_click_cor(x, y):
    print(x, y)


game_is_on = True

while game_is_on:
    answer_input = turtle.textinput(title="Guess the State",
                                    prompt=f"{score}/50 Correct\nWhat's another state's name?: ")
    if answer_input is None or answer_input == '':
        game_is_on = False
    if answer_input in states:
        score += 1
        text_name.goto(int(data_states[data_states["state"] == answer_input]["x"]),
                       int(data_states[data_states["state"] == answer_input]["y"]))
        text_name.write(f"{answer_input}")
    if score == 50:
        game_is_on = False

turtle.onscreenclick(get_mouse_click_cor)
turtle.mainloop()
