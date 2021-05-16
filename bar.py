import tkinter

class Bar:

    def __init__(self, canvas, posx=0, posy=0, width=100, height=10):
        self.canvas = canvas
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height

        # create_rectangle( upper_left(x, y), bottom_right(x, y) )
        canvas.create_rectangle(posx, posy, posx + width, posy + height, fill="black")

        self.pad = 2
        pad_coords = (posx + self.pad,
                      posy + self.pad,
                      (posx + width) - self.pad,
                      (posy + height) - self.pad)
        canvas.create_rectangle(*pad_coords, fill='#37383b') # 100% bar
        self.bar = canvas.create_rectangle(*pad_coords, fill='#de3c3c') # health relative to 100%


    def set_progress(self, amount):
        if not 0 <= amount <= 1:
            return

        new_coords = (self.posx + self.pad,
                      self.posy + self.pad,
                      self.posx + self.width * amount - self.pad,
                      self.posy + self.height - self.pad)
        self.canvas.coords(self.bar, *new_coords)