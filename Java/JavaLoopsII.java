import java.util.Scanner;

public class JavaLoopsII {
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        for(int i=0;i<t;i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            
            int total = a;
            int[] array = new int[n];
            for(int j = 0; j < n; j++){
                total += Math.pow(2, j) * b;
                array[j] = total;
            }
            
            for(int k : array){
                System.out.print(k + " ");
            }
            System.out.println();
        }
        in.close();
    }
}
