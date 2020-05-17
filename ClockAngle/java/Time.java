public class Time {
    private int hour;
    private int minute;
    private int second;

    public Time(String StringRepresentation) throws TimeException {
        hour = Integer.parseInt(StringRepresentation.split(":")[0]);
        minute = Integer.parseInt(StringRepresentation.split(":")[1]);
        second = Integer.parseInt(StringRepresentation.split(":")[2]);
        checkTimeCorrectness(this);
    }

    public Time() {
        hour = 0;
        minute = 0;
        second = 0;
    }

    public void checkTimeCorrectness(Time time) throws TimeException {
        if (time.hour < 0 || time.hour >= 24)
            throw new TimeException("Hour cannot be " + time.hour);

        if (time.minute < 0 || time.minute >= 60)
            throw new TimeException("Minute cannot be " + time.minute);

        if (time.second < 0 || time.second >= 60)
            throw new TimeException("Second cannot be " + time.second);
    }

    public void checkTimeCorrectness(int hour, int minute, int second) throws TimeException {
        if (hour < 0 || hour >= 24)
            throw new TimeException("Hour cannot be " + hour);

        if (minute < 0 || minute >= 60)
            throw new TimeException("Minute cannot be " + minute);

        if (second < 0 || second >= 60)
            throw new TimeException("Second cannot be " + second);
    }

    @Override
    public String toString() {
        return "" + hour + ":" + minute + ":" + second;
    }

    public void increaseSecond() {
        try {
            second++;
            checkTimeCorrectness(this);
        }
        catch(TimeException eSecond) {
            try {
                second = 0;
                minute++;
                checkTimeCorrectness(this);
            }
            catch(TimeException eMinute) {
                try {
                    minute = 0;
                    hour++;
                    checkTimeCorrectness(this);
                }
                catch(TimeException eHour) {
                    hour = 0;
                }
            }
        }
    }

    public void decreaseSecond() {
        try {
            second--;
            checkTimeCorrectness(this);
        }
        catch(TimeException eSecond) {
            try {
                second = 59;
                minute--;
                checkTimeCorrectness(this);
            }
            catch(TimeException eMinute) {
                try {
                    minute = 59;
                    hour--;
                    checkTimeCorrectness(this);
                }
                catch(TimeException eHour) {
                    hour = 23;
                }
            }
        }
    }

    public void increaseMinute() {
        try {
            minute++;
            checkTimeCorrectness(this);
        }
        catch(TimeException eMinute) {
            try {
                minute = 0;
                hour++;
                checkTimeCorrectness(this);
            }
            catch(TimeException eHour) {
                hour = 0;
            }
        }
    }

    public void decreaseMinute() {
        try {
            minute--;
            checkTimeCorrectness(this);
        }
        catch(TimeException eMinute) {
            try {
                minute = 59;
                hour--;
                checkTimeCorrectness(this);
            }
            catch(TimeException eHour) {
                hour = 23;
            }
        }
    }

    public void increaseHour() {
        try {
            hour++;
            checkTimeCorrectness(this);
        }
        catch(TimeException eHour) {
            hour = 0;
        }
    }

    public void decreaseHour() {
        try {
            hour--;
            checkTimeCorrectness(this);
        }
        catch(TimeException eHour) {
            hour = 23;
        }
    }

    public int getSecond() {
        return second;
    }

    public int getMinute() {
        return minute;
    }

    public int getHour() {
        return hour;
    }

    public static class TimeException extends IllegalArgumentException {
        public TimeException() {
            super();
        }

        public TimeException(String message) {
            super(message);
        }

        public TimeException(String message, Throwable cause) {
            super(message, cause);
        }

        public TimeException(Throwable cause) {
            super(cause);
        }

    }

}
