import java.util.Scanner;

public class StudentScore {
    public static void main(String... args) {
        Scanner input = new Scanner(System.in);

        System.out.println("How many students do you have?");
        int numberOfStudent = input.nextInt();

        System.out.println("How many subjects do they have?");
        int numberOfSubject = input.nextInt();

      int[][] studentGrade = new int[numberOfStudent][numberOfSubject];

	for (int count = 0; count < numberOfStudent; count++) {
            System.out.println("Entering scores for student " + (count+1));

            for (int counter = 0; counter < numberOfSubject; counter++) {
                while (true) {
                    System.out.println("Enter score for subject " + (counter+1));
                    int score = input.nextInt();

                    if (score >= 0 && score <= 100) {
			studentGrade[count][counter] = score;
                        break;
                    } else {
                        System.out.println("Please enter a score between 0 and 100.");
                    }
                }
            }

            System.out.println("Saving >>>>>>>>>>>>>>>>>>>>>>>>>>>>");
            System.out.println("Saved successfully");
	    System.out.println("              ");
	    System.out.println("              ");

        }

	    System.out.println(" ==============================================================");
            System.out.println( "STUDENT\t" + "\t" + "\t" + "\t");

            System.out.println(" ==============================================================");

    }

}

