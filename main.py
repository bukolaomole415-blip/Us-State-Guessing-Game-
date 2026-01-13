import turtle
import pandas

writer = turtle.Turtle()
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()



guessed_states = []
#game_is_on = True


#Check the users guess is in the 50 states
while len(guessed_states) < len(all_states):
    answer_state = screen.textinput(title=f"{len(guessed_states)}/Guess the State",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = []
        for states in all_states:
            if states not in guessed_states:
                missing_states.append(states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")

        break

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        writer.hideturtle()
        writer.penup()
        state_data = data[data.state == answer_state]
        # Extract the single x and y coordinate values as integers
        x_cor = state_data.x.item()
        y_cor = state_data.y.item()
        # Pass these single integer/float values to the turtle function
        writer.goto(x_cor, y_cor)
        writer.write(answer_state)


#states_to_learn.csv




turtle.exitonclick()






















