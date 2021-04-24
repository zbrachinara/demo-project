
class Platform:

    def __init__(self, display, pos_x, pos_y, box, length=100):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.length = length

        self.box = box

        display.create_line(pos_x, pos_y, pos_x + length, pos_y)

    def is_collision(self):

        if self.pos_x < self.box.box_x < self.pos_x + self.length:
            if self.box.box_y_prev < self.pos_y < self.box.box_y:
                return True
        else:
            self.box.on_platform = False;

        return False

    def do_collision(self):

        self.box.vel_y = 0
        self.box.box_y = self.pos_y - 1
        self.box.on_platform = True
