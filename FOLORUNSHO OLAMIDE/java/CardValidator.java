import java.util.Scanner;

public class CreditCalculator {

   
    public static int LeftRight(int[] array) {
        int sum = 0;
        for (int index = array.length - 2; index >= 0; index -= 2) {
            int digit = array[index] * 2;
            if (digit > 9) {
                digit = (digit / 10) + (digit % 10); 
            }
            sum += digit;
        }
        return sum;
    }

    public static int oddPlaces(int[] array) {
        int sum = 0;
        for (int index = array.length - 1; index >= 0; index -= 2) {
            sum += array[index];
        }
        return sum;
    }

    
    public static int totalSum(int leftRightSum, int oddPlaceSum) {
       int add = leftRightSum + oddPlaceSum;
	return  add;
    }

    
    public static boolean valid(int total) {
         if(total % 10 == 0){
	return true;
	} else{
	return false;
	
    }
     }
public static void int getCardType(long number){
for(int count = 0; count < number.length(); count++) {



    
    
}
}