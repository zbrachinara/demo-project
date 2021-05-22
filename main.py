from tkinter import *
from box import PlayerBox, NpcBox
from bar import Bar
import sys

step_time = 10  # milliseconds

master = Tk()

display = Canvas(master, width=500, height=500)
display.pack()
display.focus_set()

player = None
npc = None
update_helper = None
start_button = None

def setup():

    player = PlayerBox(display, step_time / 1000)

    npc = NpcBox(display, step_time / 1000)

    display.bind("a", player.do_something_a)
    display.bind("w", player.do_something_w)
    # display.bind("s", player.step)
    # display.bind("s", player.do_something_s)
    display.bind("d", player.do_something_d)
    # display.bind("<space>", update_manual)


    def update_helper():
        player.step()
        npc.step()
        display.after(step_time, update_helper)


    start_button = Button(master,
                          command=update_helper,
                          text="start",
                          height=1, width=5,
                          )

    player.quit_button = Button(master,
                         command=sys.exit,
                         text="quit",
                         height=1, width=5)


    start_button.place(anchor="se",
                       x=display["width"],
                       y=display["height"]
                       )

    health_bar = Bar(display, posx=10, posy=10, width=200, height=30)
    health_bar.set_progress(0.5)
    player.health_bar = health_bar

setup()

player.restart_button = Button(master,
                               command=setup,
                               text="restart",
                               height=1, width=5
                               )

player.restart_button.place(anchor="se",
                   x=int(display["width"])-200,
                   y=display["height"]
                   )

master.mainloop()
