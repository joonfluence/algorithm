package 오르막수;

import java.util.Arrays;
import java.util.Scanner;

/*

오르막 수 실버1 https://www.acmicpc.net/problem/11057

1. 각 항의 관계를 찾는다.

N: 1 (0, 1, 2, 3, 4, 5, 6, 7, 8, 9) 1 * 10 = 10
N: 2 (00 .. 09, 11 ... 19, 22 ... 29, 33 .. 39, ... ) 10 + 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1 = 55
M: 3 (000 ... 009, 011 ... 019 ... , 022 ... 029, 111 .. 119, 222 ... 229, ) 55 + 45 + 36 + 28 + 21 + 15 + 10 + 6 + 3 + 1 = 220
M: 4 (0000 ... 0009, 1111 ... 1119, 1222 ... 1229 ) 220 + 165 + 120 + 84 + 56 + 35 + 20 + 10 + 4 + 1 = 715

dp[1][0] = 1, dp[1][1] = 1, dp[1][2] = 1, ... dp[1][9] = 1 => sum(dp[1])
dp[2][0] = 10, dp[2][1] = 9 .. => sum(dp[2])

2. 점화식을 구한다.

dp[i][j] = dp[i][j] = dp[i-1][j] + ... dp[i-1][N]

3. 결과값을 도출한다.

sum(dp[n])

 */
public class DP_11057 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[][] dp = new int[N+1][10];
        for (int i = 0; i < 10; i++) {
            dp[1][i] = 1;
        }

        for (int i = 2; i <= N; i++) {
            for (int j = 0; j < 10; j++) {
                for (int k = j; k < 10; k++) {
                    dp[i][j] += dp[i-1][k];
                }
                dp[i][j] %= 10007;
            }
        }

        System.out.println(Arrays.stream(dp[N]).sum() % 10007);
    }
}
