from tkinter import *
from box import PlayerBox, NpcBox

step_time = 10 # milliseconds

master = Tk()

display = Canvas(master, width=500, height=500)
display.pack()
display.focus_set()

player = PlayerBox(display, step_time / 1000)

npc = NpcBox(display, step_time / 1000)

def update_manual(e):
    npc.step()

display.bind("a", player.do_something_a)
display.bind("w", player.do_something_w)
# display.bind("s", player.step)
# display.bind("s", player.do_something_s)
display.bind("d", player.do_something_d)
display.bind("<space>", update_manual)

def update_helper():
    player.step()
    # npc.step()
    display.after(step_time, update_helper)

display.after(step_time, update_helper)

master.mainloop()
