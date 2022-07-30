"""
Use boolean variables to control program logic between two different code
paths.
"""
import turtle

if __name__ == '__main__':
    # TODO)
    #  1. Use a boolean variable to indicate if it is the weekend.
    #     Display a different message to the user depending on whether it is
    #     the weekend or not.
    day='saturday'
    is_weekday = day == 'saturday'  #true
    is_weekday = day == 'sunday'  #true
    if is_weekday:
        print('its the weekend!')
    else:
        print('its a week day!')
    #  2. Use a boolean variable to indicate if a student passed an exam.
    #     Display a different message to the user depending on whether they
    #     passed or not.
    score='71'
    is_score = score > '69' #true
    if is_score:
        print('you passed the test!')
    else:
        print('you failed!')
    #  3. Use a boolean variable to indicate if a game is over. When the game
    #     is over, tell the user.
    game='ongoing'
    is_game = game == 'ongoing' #true
    if is_game:
        print('the game is ongoing')
    else:
        print('game is over')

    #  4. Use two boolean variables, one to indicate if a shape should be red,
    #     the other to indicate if the shape is to be square. When both
    #     variables are true, use a turtle to draw a red square.
    red='false'
    square='true'
    is_red = red == 'true' #true
    is_square = square == 'true' #true
    bob=turtle.Turtle()
    if is_red:
        print("is_red is true so rob will be red")
        bob.pencolor('red')
    else:
        print('you now have nothing')
    if is_square:

        for i in range (4):
            bob.forward(100)
            bob.right(90)
    else:
        print('you now have red someth')
    pass
