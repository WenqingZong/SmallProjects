/*
In Main.java, currently the program is running an infinite while
loop, which will increase current time by 1 second and re-calculate every angle,
a bit like a show-off mode.

To use it as a clock angle calculator, please comment out current main method
and uncomment the other, which will get a time in string representation
(format: hh:mm:ss) from command line argument.
*/
public class Main {
    public static void main(String[] argv) {
        Time testTime = new Time();
        Clock testClock = new Clock(testTime);
        while (true) {
            System.out.println("Current time: " + testTime);
            System.out.println("Second: " + testClock.getSecondAngle());
            System.out.println("Minute: " + testClock.getMinuteAngle());
            System.out.println("Hour: " + testClock.getHourAngle());
            System.out.println("Second - Minute angle: " + testClock.getSecondMinuteAngle());
            System.out.println("Second - Hour angle: " + testClock.getSecondHourAngle());
            System.out.println("Minute - Hour angle: " + testClock.getMinuteHourAngle());
            testTime.increaseSecond();
            try {
                Thread.sleep(1000);
            }
            catch(Exception e) {
                System.err.println(e);
                e.printStackTrace();
            }
            for (int i = 0; i < 7; i++) {
                System.out.print(String.format("\033[%dA", 1)); // Move up
                System.out.print("\033[2K"); // Erase line content
                // System.out.print(String.format("\033[2J")); // equals to 'clear' command
            }
        }
    }

/*
    public static void main(String[] argv) {
        Time testTime = new Time(argv[0]);
        Clock testClock = new Clock(testTime);
        System.out.println("Current time: " + testTime);
        System.out.println("Second: " + testClock.getSecondAngle());
        System.out.println("Minute: " + testClock.getMinuteAngle());
        System.out.println("Hour: " + testClock.getHourAngle());
        System.out.println("Second - Minute angle: " + testClock.getSecondMinuteAngle());
        System.out.println("Second - Hour angle: " + testClock.getSecondHourAngle());
        System.out.println("Minute - Hour angle: " + testClock.getMinuteHourAngle());
    }
*/

}
