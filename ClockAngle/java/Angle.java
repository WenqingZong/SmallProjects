public class Angle {
    private double angle;

    public Angle(double requiredAngle) {
        angle = requiredAngle;
    }

    public Angle() {
        angle = 0;
    }

    public void convertToNormalAngle() {
        angle = Math.abs(angle);
        while (angle >= 360)
            angle -= 360;

        if (angle > 180)
            angle = 360 - angle;
    }

    public double getAngle() {
        return angle;
    }

    @Override
    public String toString() {
        return "" + angle + " degree";
    }
}
