package 구현;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class IM_1330 {
    private final static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        Integer[] nums = Arrays.stream(br.readLine().split(" ")).map(Integer::parseInt).toArray(Integer[]::new);

        int A = nums[0];
        int B = nums[1];

        if(A == B){
            System.out.println("==");
        } else if(A < B){
            System.out.println("<");
        } else if(A > B){
            System.out.println(">");
        }
    }
}
