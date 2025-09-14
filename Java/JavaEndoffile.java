import java.util.Scanner;

public class JavaEndoffile {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int count = 0;
        while(scanner.hasNext()){
            String txt = scanner.nextLine();
            count++;
            System.out.println(count +" "+txt);
        }
        scanner.close();
    }
}
