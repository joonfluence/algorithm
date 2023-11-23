import java.util.Arrays;
import java.util.Scanner;

/**
 * 정수 삼각형 (DP, 실버2) https://www.acmicpc.net/problem/1932
 *

 1. 점화식 세우기

 - dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + dp[i][j]

 2. 예외 처리하기

 - 왼쪽 위 숫자가 없을 경우 -> 0
 - 오른쪽 위 숫자가 없을 경우 -> 0

 3. 변수 정하기

 - left_up = dp[i-1][j-1]
 - right_up =  dp[i-1][j]

 4. 결과값 도출하기

 - max(dp[i])


 [입력값]

 5
 7
 3 8
 8 1 0
 2 7 4 4
 4 5 2 6 5

 [출력값]

 30

 */
class DP_1932 {
    static int[][] dp;
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();
        dp = new int[N][];

        for (int i = 0; i < N; i++) {
            dp[i] = new int[i + 1];
            for (int j = 0; j <= i; j++) {
                dp[i][j] = in.nextInt();
            }
        }

        for (int i = 1; i < N; i++) {
            for (int j = 0; j < dp[i].length; j++) {
                int leftUp = 0;
                int up = 0;
                if (j > 0){
                    leftUp = dp[i - 1][j - 1];
                }
                if (j < i){
                    up = dp[i - 1][j];
                }
                dp[i][j] = dp[i][j] + Math.max(up, leftUp);
            }
        }

        System.out.println(Arrays.stream(dp[N - 1]).max().getAsInt());
    }
}
