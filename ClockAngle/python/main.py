from time import sleep
from clock import Clock
from my_time import Time, TimeError
from sys import argv

def main():
    clock = Clock()
    while True:
        print("Current time: " + str(clock.time))
        print("Second: " + str(clock.second_angle))
        print("Minute: " + str(clock.minute_angle))
        print("Hour: " + str(clock.hour_angle))
        print("Second - Minute: " + str(clock.get_second_minute_angle()))
        print("Second - Hour: " + str(clock.get_second_hour_angle()))
        print("Minute - Hour: " + str(clock.get_minute_hour_angle()))
        clock.increase_second()
        sleep(1)
        for i in range(7):
            print("\033[1A", end = "")  # move cursor up by one line
            print("\033[2K", end = "")  # clear current line

# def main():
#     time = Time(int(argv[1]), int(argv[2]), int(argv[3]))
#     clock = Clock(time)
#     print("Current time: " + str(clock.time))
#     print("Second: " + str(clock.second_angle))
#     print("Minute: " + str(clock.minute_angle))
#     print("Hour: " + str(clock.hour_angle))
#     print("Second - Minute: " + str(clock.get_second_minute_angle()))
#     print("Second - Hour: " + str(clock.get_second_hour_angle()))
#     print("Minute - Hour: " + str(clock.get_minute_hour_angle()))

if __name__ == "__main__":
    main()
