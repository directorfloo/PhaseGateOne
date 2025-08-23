/*Formulas
Next Period Date
Next Period=LMP+CL
Ovulation Day
Ovulation usually occurs 14 days before the next period.
Ovulation= LMP + ( 𝐶𝐿 − 14)
Ovulation=LMP+(CL−14)
Fertile Window
Sperm can live up to 5 days, egg up to 1 day → fertile window = 5 days before ovulation + ovulation day + 1 day after.
Fertile Window =(Ovulation) to 
(Ovulation + 1)
Fertile Window=(Ovulation−5) to (Ovulation+1)
Safe Periods
Safe days are outside the fertile window:
Before Fertile Window:
Safe 1
= LMP to (Ovulation − 6)
Safe 1=LMP to (Ovulation−6)
After Fertile Window:
Safe 2 =(Ovulation +2) to Next Period
Safe 2=(Ovulation+2) to Next Period*/




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

