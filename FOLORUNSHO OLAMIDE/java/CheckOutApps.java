import java.util.Scanner;
import java.time.LocalDate;
import java.util.ArrayList;

public class CheckOutApp {
    public static void main(String[] args) {
        ArrayList<String> itemList = new ArrayList<>();
        ArrayList<Double> unitList = new ArrayList<>();
        ArrayList<Double> piecesList = new ArrayList<>();

        Scanner scanner = new Scanner(System.in);
        LocalDate localDate = LocalDate.now();

        System.out.print("What is your full name:\n ");
        String name = scanner.nextLine();

        String addItem = "YES";
        double pieces = 0;
        double unit = 0;
        while (!addItem.equals("NO")) {
            System.out.print("What did the user buy?:\n ");
            String product = scanner.next();

            System.out.print("How many pieces?:\n ");
            pieces = scanner.nextDouble();

            System.out.print("How much per unit?:\n ");
            unit = scanner.nextDouble();

            itemList.add(product);
            unitList.add(unit);
            piecesList.add(pieces);

            System.out.print("Add more items? (Yes/No):\n ");
            addItem = scanner.next().toUpperCase();
        }
	double subTotal = 1;
        System.out.print("Enter discount (%): ");
	
        double discount = scanner.nextDouble();
	double discountAmount = (discount / 100) * subTotal;
	
        double finalTotal = subTotal - discountAmount;


        System.out.println("\n\n SEMICOLON STORES");
        System.out.println(" MAIN BRANCH");
        System.out.println(" LOCATION: 312, HERBERT MACAULAY WAY,  SABO YABA, LAGOS.");
        System.out.println(" TEL: 08123425776 ");
        System.out.println(" Date: " + localDate);
        System.out.println(" Cashier: Adam ");
        System.out.println(" Customer Name: " + name);
        System.out.println("================================================================");
        System.out.println(" ITEM\t\tQTY\tPRICE\tTOTAL(NGN)");
        System.out.println("----------------------------------------------------------------");

        for (int counter = 0; counter < unitList.size(); counter++) {
            double itemTotal = unitList.get(counter) * piecesList.get(counter);
            subTotal += unitList.get(counter) * piecesList.get(counter);
        
            System.out.println(" " + itemList.get(counter) + "\t\t" + piecesList.get(counter) + "\t" + unitList.get(counter) + "\t" + itemTotal);
        }

        System.out.println("================================================================");
        System.out.println(" Sub Total: " + subTotal);
        System.out.println(" Discount: " + discountAmount);
        System.out.println(" Final Total: " + finalTotal);
    }
}