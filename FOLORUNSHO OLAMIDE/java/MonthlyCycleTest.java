import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertArrayEquals;

public class MonthlyCycleTest {

    @Test
    public void testToMonthlyCycleCalculator() {
        // Arrange
        int lastMenstrualPeriodStartDate = 1; 
        int cycleLength = 28;
        int periodLength = 5;

        // Act
        int nextperiod = MonthlyCycle.nextperiodCycle(lastMenstrualPeriodStartDate, cycleLength, periodLength);
        int ovulation = MonthlyCycle.ovulationCycle(lastMenstrualPeriodStartDate, cycleLength, periodLength);
        int[] fertile = MonthlyCycle.fertileWindowCycle(ovulation);
        int[] safe = MonthlyCycle.safePeriod(ovulation, lastMenstrualPeriodStartDate, nextperiod);

        // Assert
        assertEquals(29, nextperiod, "Next period should be day 29");
        assertEquals(15, ovulation, "Ovulation should be day 15");
        assertArrayEquals(new int[]{10, 16}, fertile, "Fertile window should be days 10–16");
        assertArrayEquals(new int[]{1, 9, 17, 29}, safe, "Safe periods should be days 1–9 and 17–29");
    }
}
