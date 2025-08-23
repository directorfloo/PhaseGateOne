




/* 1.The menstrual cycle is the recurring process in the female reproductive system that prepares the body for a possible pregnancy. It is controlled by hormones and typically lasts 21–35 days (average 28 days). The cycle involves changes in the ovaries and the uterus.*/


//2.



public class MonthlyCycle {

    public static int nextperiodCycle(int lastMenstrualPeriodStartDate, int cycleLength, int periodLength) {
        int nextperiod = lastMenstrualPeriodStartDate + cycleLength;
        return nextperiod;
    }

    public static int ovulationCycle(int lastMenstrualPeriodStartDate, int cycleLength, int periodLength) {
        int ovulation = lastMenstrualPeriodStartDate + (cycleLength - 14);
        return ovulation;
    }

    public static int[] fertileWindowCycle(int ovulation) {
        int fertileStart = ovulation - 5;
        int fertileEnd = ovulation + 1;
        return new int[]{fertileStart, fertileEnd};
    }

    public static int[] safePeriod(int ovulation, int lastMenstrualPeriodStartDate, int nextperiod) {
        int safeBeforeFertileWindow = lastMenstrualPeriodStartDate;
        int safeBeforeEnd = ovulation - 6;

        int safeAfterStart = ovulation + 2;
        int safeAfterEnd = nextperiod;

        return new int[]{safeBeforeFertileWindow, safeBeforeEnd, safeAfterStart, safeAfterEnd};
    }

    public static void main(String... args) {
        int lastMenstrualPeriodStartDate = 1; 
        int cycleLength = 28;
        int periodLength = 5;

        int nextperiod = nextperiodCycle(lastMenstrualPeriodStartDate, cycleLength, periodLength);
        int ovulation = ovulationCycle(lastMenstrualPeriodStartDate, cycleLength, periodLength);
        int[] fertile = fertileWindowCycle(ovulation);
        int[] safe = safePeriod(ovulation, lastMenstrualPeriodStartDate, nextperiod);

        System.out.println("Next Period starts on day: " + nextperiod);
        System.out.println("Ovulation on day: " + ovulation);
        System.out.println("Fertile Window: day " + fertile[0] + " to day " + fertile[1]);
        System.out.println("Safe Periods:");
        System.out.println("   Safe before fertile: day " + safe[0] + " to day " + safe[1]);
        System.out.println("   Safe after fertile: day " + safe[2] + " to day " + safe[3]);
    }
}

