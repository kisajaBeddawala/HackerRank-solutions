import java.util.Scanner;

public class JavaStringReverse {
    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        /* Enter your code here. Print output to STDOUT. */
        StringBuilder stringBuilder = new StringBuilder(A);
        stringBuilder.reverse();
        
        if(A.equals(stringBuilder.toString())){
            System.out.println("Yes");
        }else{
            System.out.println("No");
        }
        sc.close();
    }
}
