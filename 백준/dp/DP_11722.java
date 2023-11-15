import java.util.Scanner;

/**
 * 가장 긴 감소하는 부분 수열 (DP, 실버2) https://www.acmicpc.net/problem/11722
 *
 * 1. 점화식 세우기 : dp[i] = Math.max(dp[i], dp[j] + 1);
 * 2. 루프 순회하기
 * 3. 조건문 작성하기 : numbers[i] < numbers[j]
 * 4. 결과값 도출하기
 *
 * [입력값]
 *
 * 6
 * 10 20 10 30 20 50
 *
 * [출력값]
 *
 * 3
 */

public class DP_11722 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] dp = new int[N + 1];
        int[] numbers = new int[N + 1];
        int max = 1;

        for (int i = 1; i < N+1; i++) {
            dp[i] = 1;
            numbers[i] = sc.nextInt();

            for (int j = 0; j < i; j++) {
                if(numbers[i] < numbers[j]){
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
            max = Math.max(max, dp[i]);
        }
        System.out.println(max);
    }
}
