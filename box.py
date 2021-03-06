from PIL import Image, ImageTk
from surface import Platform, FloorPlatform


class Box:

    def __init__(self, display, step_size):
        # coordinates
        self.box_x = 250
        self.box_y = 25

        self.vel_y = 0
        self.box_y_prev = 0
        self.on_platform = False

        self.step_size = step_size

        self.pilImage = Image.open("blockTexture.png")
        self.tkImage = ImageTk.PhotoImage(self.pilImage)
        self.id = display.create_image(100, 100, image=self.tkImage)
        print(id)

        self.display = display

        self.platforms = []
        self.platforms.append(Platform(display, 50, 75, self, length=300))
        self.platforms.append(Platform(display, 100, 100, self))
        self.platforms.append(Platform(display, 100, 200, self))
        self.platforms.append(FloorPlatform(display, 0, 500, self, length=500))

    def sense_key(self, type):
        global box_x
        global box_y

        if type == 0:
            self.box_x -= 10
        elif type == 1:
            self.box_y -= 10
        elif type == 2:
            self.box_y += 10
        elif type == 3:
            self.box_x += 10

        self.display.coords(self.id, self.box_x, self.box_y)

    def do_something_a(self, e):
        print("a pressed")
        self.sense_key(0)

    def do_something_w(self, e):
        print("w pressed")
        self.on_platform = False
        self.sense_key(1)

    def do_something_s(self, e):
        print("s pressed")
        self.sense_key(2)

    def do_something_d(self, e):
        print("d pressed")
        self.sense_key(3)

    # new functions
    def step(self):
        self.display.coords(self.id, self.box_x, self.box_y)


class PlayerBox(Box):

    def __init__(self, display, step_size):
        super().__init__(display, step_size)

        self.health = 100
        self.max_health = 100
        self.health_bar = None

    def step(self):
        if not self.on_platform:
            self.vel_y += 100 * self.step_size
            # print(self.vel_y)
            self.box_y_prev = self.box_y
            self.box_y += self.vel_y * self.step_size
        # print(self.box_y)

        for platform in self.platforms:
            if platform.is_collision():
                platform.do_collision()

        self.health_bar.set_progress( self.health / self.max_health )

        if self.health == 0:
            self.quit_button.place(anchor="se",
                                  x=int(self.display["width"]) - 100,
                                  y=self.display["height"]
                                  )

        super().step()


class NpcBox(Box):

    def __init__(self, display, step_size):
        super().__init__(display, step_size)

        self.box_y = 100
        self.box_x = 100

        self.direction = 1
        self.range = 100
        self.start = self.box_x
        self.end = self.box_x + self.range

    def step(self):

        period = 50

        if self.box_x > self.end:
            self.direction = -1
            # print("reverse to the left")
        if self.box_x < self.start:
            self.direction = 1
            # print("reverse to the right")

        self.box_x += (self.range / period) * self.direction

        super().step()
