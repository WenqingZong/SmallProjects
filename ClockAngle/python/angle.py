class Angle():
    def __init__(self, angle = 0.0):
        self.angle = angle

    def convert_to_normal_angle(self):
        self.angle = abs(self.angle)
        while self.angle >= 360:
            self.angle -= 360

        if self.angle > 180:
            self.angle = 360 - self.angle

    def __str__(self):
        return str(self.angle) + " degree"
