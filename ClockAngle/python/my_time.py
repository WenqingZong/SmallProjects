class TimeError(ValueError):

    def __init__(self, message):
        super().__init__(message)

class Time():

    def __init__(self, hour = 0, minute = 0, second = 0):
        self.second = second
        self.minute = minute
        self.hour = hour
        self.check_time_correctness()

    def __str__(self):
        return str(self.hour) + ":" + str(self.minute) + ":" + str(self.second)

    def check_time_correctness(self):
        if self.second < 0 or self.second >= 60:
            raise TimeError("Second cannot be " + str(self.second))

        if self.minute < 0 or self.minute >= 60:
            raise TimeError("Minute cannot be " + str(self.minute))

        if self.hour < 0 or self.hour >= 24:
            raise TimeError("Hour cannot be " + str(self.hour))

    def increase_second(self):
        try:
            self.second += 1
            self.check_time_correctness()
        except TimeError:
            try:
                self.second = 0
                self.minute += 1
                self.check_time_correctness()
            except TimeError:
                try:
                    self.minute = 0
                    self.hour += 1
                    self.check_time_correctness()
                except TimeError:
                    self.hour = 0

    def decrease_second(self):
        try:
            self.second -= 1
            self.check_time_correctness()
        except TimeError:
            try:
                self.second = 59
                self.minute -= 1
                self.check_time_correctness()
            except TimeError:
                try:
                    self.minute = 59
                    self.hour -= 1
                    self.check_time_correctness()
                except TimeError:
                    self.hour = 23

    def increase_minute(self):
        try:
            self.minute += 1
            self.check_time_correctness()
        except TimeError:
            try:
                self.minute = 0
                self.hour += 1
                self.check_time_correctness()
            except TimeError:
                    self.hour = 0

    def decrease_minute(self):
        try:
            self.minute -= 1
            self.check_time_correctness()
        except TimeError:
            try:
                self.minute = 59
                self.hout -= 1
                self.check_time_correctness()
            except TimeError:
                self.hour = 23

    def increase_hour(self):
        try:
            self.hour += 1
            self.check_time_correctness()
        except TimeError:
            self.hour = 0

    def decrease_hour(self):
        try:
            self.hour -= 1
            self.check_time_correctness()
        except TimeError:
            self.hour = 23
