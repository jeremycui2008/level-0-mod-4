"""
Use a while loop to recite the digits of pi
"""
from tkinter import messagebox, simpledialog, Tk
import math


if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    # TODO) Place the first 20 digits of pi into a variable as a string
    #  3.1415926535897932384
    pi_str='3.1415926535897932384'
    # TODO) Print out the first 3 digits of pi. For example,
    is_pi = pi_str == '3.1415926535897932384'
    while pi_str<'3.14159265358979323845':
        print(pi_str)
        pi_str='3.141592653589799323845'
    pi_str='3.1415926535897932384'
    # TODO) Use a while loop to keep asking for the next digit of pi
    while pi_str == '3.1415926535897932384':
        number=simpledialog.askstring(None, prompt='whats the 21st number in pi?')
        if number=='6':
            pi_str='3.14159265358979323846'
        else:
            messagebox.showinfo(None, message='you failed to recite any number of pi')
            pi_str='grufgrirgfri'

    while pi_str == '3.14159265358979323846':
        number=simpledialog.askstring(None, prompt='whats the 22nd number in pi?')
        if number=='2':
            pi_str='3.141592653589793238462'
            messagebox.showinfo(None, message='you recited two numbers!')
    pass

        # TODO) If they are correct, print "correct".
        #  If they are not, print "incorrect" and break out of the while loop


    # TODO) Print out how many digits of pi the user was able to recite
    #  in a row




'3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'
