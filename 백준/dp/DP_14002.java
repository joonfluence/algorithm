import java.util.ArrayList;
import java.util.Scanner;
import java.util.Stack;

/**
 * 가장 긴 증가하는 부분 수열4 (DP, 골드4) https://www.acmicpc.net/problem/14002
 *
 * 1. 점화식 세우기
 * 2. 조건문 작성하기
 * 3. 값 추가하기
 * 4. 역순회하기
 * 5. 출력하기
 *
 */

class DP_14002 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] dp = new int[N + 1];
        int[] numbers = new int[N + 1];
        ArrayList<Integer> results = new ArrayList<>();
        int max = 1;
        int lis = 1;

        for (int i = 1; i < N+1; i++) {
            dp[i] = 1;
            numbers[i] = sc.nextInt();

            ArrayList<Integer> temp = new ArrayList<>();

            for (int j = 1; j < i; j++) {
                if(numbers[j] < numbers[i]){
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                    lis = Math.max(lis, dp[i]);
                }
            }
            max = Math.max(max, dp[i]);
        }

        StringBuilder sb = new StringBuilder();
        sb.append(lis+"\n");

        Stack<Integer> s = new Stack<>();
        for(int i=N; i>=1; i--) {
            // dp: [0, 1, 2, 1, 3, 2, 4]
            // lis : 4 -> 3 -> 2 -> 1
            if(dp[i] == lis) {
                s.push(numbers[i]); // numbers: [0, 10, 20, 10, 30, 20, 50]
                lis--;
            }
        }

        // 10 -> 20 -> 30 -> 50
        while(!s.isEmpty()) {
            sb.append(s.pop()+" ");
        }
        // 4+'\n'
        System.out.println(sb.toString());
    }
}