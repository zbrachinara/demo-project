from tkinter import *
from box import Box

step_time = 10 # milliseconds

master = Tk()

display = Canvas(master, width=500, height=500)
display.pack()
display.focus_set()

player = Box(display, step_time / 1000)

display.bind("a", player.do_something_a)
display.bind("w", player.do_something_w)
# display.bind("s", player.step)
# display.bind("s", player.do_something_s)
display.bind("d", player.do_something_d)

def update_helper():
    player.step(0)
    display.after(step_time, update_helper)

display.after(step_time, update_helper)

master.mainloop()
