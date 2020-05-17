public class Clock {
    private Time time;
    private Angle secondAngle;
    private Angle minuteAngle;
    private Angle hourAngle;

    public Clock(Time requiredTime) {
        time = requiredTime;
        setSecondAngle();
        setMinuteAngle();
        setHourAngle();
    }

    public Clock() {
        time = new Time();
        secondAngle = new Angle(0);
        minuteAngle = new Angle(0);
        hourAngle = new Angle(0);
    }

    public Time getTime() {
        return time;
    }

    public Angle getSecondMinuteAngle() {
        setSecondAngle();
        setMinuteAngle();
        setHourAngle();
        Angle secondMinuteAngle = new Angle(secondAngle.getAngle()
                - minuteAngle.getAngle());
        secondMinuteAngle.convertToNormalAngle();
        return secondMinuteAngle;
    }

    public Angle getSecondHourAngle() {
        setSecondAngle();
        setMinuteAngle();
        setHourAngle();
        Angle secondHourAngle = new Angle(secondAngle.getAngle() - hourAngle.getAngle());
        secondHourAngle.convertToNormalAngle();
        return secondHourAngle;
    }

    public Angle getMinuteHourAngle() {
        setSecondAngle();
        setMinuteAngle();
        setHourAngle();
        Angle minuteHourAngle = new Angle(minuteAngle.getAngle() - hourAngle.getAngle());
        minuteHourAngle.convertToNormalAngle();
        return minuteHourAngle;
    }

    private void setSecondAngle() {
        secondAngle = new Angle(((double)time.getSecond() / 60) * 360);
    }
    private void setMinuteAngle() {
        minuteAngle = new Angle(((double)time.getMinute() / 60) * 360
                + (((double)time.getSecond() / (60 * 60)) * 360));
    }

    private void setHourAngle() {
        double hourIn12 = time.getHour() > 12 ? time.getHour() - 12 : time.getHour();
        hourAngle = new Angle(hourIn12 / 12 * 360
                + ((double)time.getMinute() / (60 * 12)) * 360
                + ((double)time.getSecond() / (60 * 60 * 12)) * 360);
    }

    public Angle getSecondAngle() {
        setSecondAngle();
        return secondAngle;
    }

    public Angle getMinuteAngle() {
        setMinuteAngle();
        return minuteAngle;
    }

    public Angle getHourAngle() {
        setHourAngle();
        return hourAngle;
    }

}
