import java.text.NumberFormat;
import java.util.Locale;
import java.util.Scanner;

public class JavaCurrencyFormatter {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double payment = scanner.nextDouble();
        scanner.close();
        
        // Write your code here.
        Locale us = Locale.US;
        Locale india = new Locale("en", "IN");
        Locale china = Locale.CHINA;
        Locale france = Locale.FRANCE;
        
        System.out.println("US: " + NumberFormat.getCurrencyInstance(us).format(payment));
        System.out.println("India: " + NumberFormat.getCurrencyInstance(india).format(payment));
        System.out.println("China: " + NumberFormat.getCurrencyInstance(china).format(payment));
        System.out.println("France: " + NumberFormat.getCurrencyInstance(france).format(payment));
    }
}
