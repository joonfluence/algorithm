import java.util.Scanner;

/**
 * 가장 긴 증가하는 부분 수열 (DP, 실버2) https://www.acmicpc.net/problem/11053
 *
 * 1. 점화식 세우기 : dp[i] = Math.max(dp[i], dp[j] + 1);
 * 2. 루프 순회하기
 * 3. 결과값 도출하기
 *
 * [입력값]
 *
 * 6
 * 10 20 10 30 20 50
 *
 * [출력값]
 *
 * 4
 */

class DP_11053_bottomUp {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();
        int[] dp = new int[N+1];
        int[] number = new int[N+1];
        int max = 1;

        for (int i = 1; i < N+1; i++) {
            dp[i] = 1;
            number[i] = in.nextInt();
            for (int j = 0; j < i; j++) {
                if (number[j] < number[i]){
                    // dp[i] = i번째 원소까지 가진 부분 수열의 증가 수열 최댓값
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
            max = Math.max(max, dp[i]);
        }
        System.out.println(max);
    }
}
