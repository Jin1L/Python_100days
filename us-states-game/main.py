import turtle
import pandas

data = pandas.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
guessed_states = []
states_list = data.state.to_list()
#correct_num = 0

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=str(len(guessed_states)) + "/50 States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        # missing_states = []
        missing_states = [state for state in states_list if state not in guessed_states]
        # for state in states_list:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break



    if answer_state in states_list:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        #correct_num += 1



