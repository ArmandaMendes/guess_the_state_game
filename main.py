import turtle
import pandas

data = pandas.read_csv("50_states.csv")
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.bgcolor("pink")
screen.setup(width=800, height=600)


image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
#create new turtle so it does not interfere with current image turtle

list_of_states = data.state.tolist()
guessed_states = []

while len(guessed_states) < len(list_of_states):

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50",
                                    prompt="What is another state?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in list_of_states:
            if state not in guessed_states:
                missing_states.append(state)
                learning_data = pandas.DataFrame(missing_states)
                learning_data.to_csv("states_to_learn.csv")

        break
    if answer_state in list_of_states:
        guessed_states.append(answer_state)
            #create the turtle:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
            #turtle needs to go the x and y coordinates
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)











