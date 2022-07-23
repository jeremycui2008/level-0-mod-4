"""
Write a program to return the correct letter grade
"""
from tkinter import messagebox, simpledialog, Tk

# The teacher wants you to write a program that converts the score on 2
# 100 point tests to a letter grade. The teacher wants you to average the
# score from the 2 tests and print out the letter grade back to the user.
# The letter grades are assigned as follows:
#   A = 89.5 to 100
#   B = 79.5 to less than 89.5
#   C = 69.5 to less than 79.5
#   D = 59.5 to less than 69.5
#   F = less than 59.5
if __name__ == '__main__':
    window=Tk()

    # TODO) Ask the user for their score on the FIRST test and store their
    #  score in a variable
    test_1=simpledialog.askinteger(title='first_test', prompt='what was the score for your first test?')
    # TODO) Ask the user for their score on the SECOND test and store their
    #  score in a variable
    test_2 = simpledialog.askinteger(title='test_2',prompt='what was the score for your second test?')
    # TODO) Take the average score of both tests (total score / 2)
    average=(test_1+test_2)/2
    if average>89.5 and average<100:
        messagebox.showinfo(title='wow!', message='Wow! You must have studied really hard for those tests!')
    elif average<89.5 and average>79.5:
        messagebox.showinfo(title='ok',message='ok, I guess.')
    elif average>100:
        messagebox.showinfo(title='you lied',message='you have lied, now is the time for bloodshed')
    elif average<79.5 and average>69.5:
        messagebox.showinfo(title='ok?',message='you are starting to disappoint...')
    elif average<69.5 and average>59.5:
        messagebox.showinfo(title='maybe get better',message='please study more')
    elif average<59.5 and average>0:
        messagebox.showinfo(title='you should study, now!',message='go get studying')
    elif average<0:
        messagebox.showinfo(title='tou are failure supreme',message='a negative score? Wow just wow.')

    # TODO) Use if statements to check the average score and print the
    #  corresponding letter grade back to the user. Also, give a different
    #  message according to their grade. Example, for an 'A' grade:
    #  "Wow! You must have studied really hard for those tests!"
    pass
