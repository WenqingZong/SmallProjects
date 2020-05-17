from my_time import Time
from angle import Angle
class Clock():
    def __init__(self, time = Time(0, 0, 0)):
        self.time = time
        self.set_second_angle()
        self.set_minute_angle()
        self.set_hour_angle()

    def set_second_angle(self):
        self.second_angle = Angle(self.time.second / 60 * 360)

    def set_minute_angle(self):
        self.minute_angle = Angle(self.time.minute / 60 * 360 + self.time.second / (60 * 60) * 360)

    def set_hour_angle(self):
        if self.time.hour > 12:
            hour = self.time.hour - 12
        else:
            hour = self.time.hour
        self.hour_angle = Angle(hour / 12 * 360 + self.time.minute / (60 * 12) * 360
+ self.time.second / (60 * 60 * 12) * 360)

    def increase_second(self):
        self.time.increase_second()
        self.set_second_angle()
        self.set_minute_angle()
        self.set_hour_angle()

    def decrease_second(self):
        self.time.decrease_second()
        self.set_second_angle()
        self.set_minute_angle()
        self.set_hour_angle()

    def increase_minute(self):
        self.time.increase_minute()
        self.set_second_angle()
        self.set_minute_angle()
        self.set_hour_angle()

    def decrease_minute(self):
        self.time.decrease_minute()
        self.set_second_angle()
        self.set_minute_angle()
        self.set_hour_angle()

    def increase_hour(self):
        self.time.increase_hour()
        self.set_second_angle()
        self.set_minute_angle()
        self.set_hour_angle()

    def decrease_hour(self):
        self.time.decrease_hour()
        self.set_second_angle()
        self.set_minute_angle()
        self.set_hour_angle()

    def get_second_minute_angle(self):
        self.set_second_angle()
        self.set_minute_angle()
        self.set_hour_angle()
        second_minute_angle = Angle(self.second_angle.angle - self.minute_angle.angle)
        second_minute_angle.convert_to_normal_angle()
        return second_minute_angle

    def get_second_hour_angle(self):
        self.set_second_angle()
        self.set_minute_angle()
        self.set_hour_angle()
        second_hour_angle = Angle(self.second_angle.angle - self.hour_angle.angle)
        second_hour_angle.convert_to_normal_angle()
        return second_hour_angle

    def get_minute_hour_angle(self):
        self.set_second_angle()
        self.set_minute_angle()
        self.set_hour_angle()
        minute_hour_angle = Angle(self.minute_angle.angle - self.hour_angle.angle)
        minute_hour_angle.convert_to_normal_angle()
        return minute_hour_angle
