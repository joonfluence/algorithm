package 동물원;

import java.util.Arrays;
import java.util.Scanner;

/*

https://www.acmicpc.net/problem/1309 https://mygumi.tistory.com/128

1. 각각의 경우의 수를 계산한다.

- 왼쪽에 배치하는 경우 : dp[i-1][0] + dp[i-1][2]
- 오른쪽에 배치하는 경우 : dp[i-1][1] + dp[i-1][2]
- 배치하지 않는 경우 : dp[i-1][0] + dp[i-1][1] + dp[i-1][2]

 */
public class DP_1309 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[][] dp = new int[N + 1][3];

        dp[1][0] = 1;
        dp[1][1] = 1;
        dp[1][2] = 1;

        for (int i = 2; i <= N; i++) {
            // 배차하지 않는 경우
            dp[i][0] += ((dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % 9901);
            // 왼쪽에 배치하는 경우
            dp[i][1] += ((dp[i-1][0] + dp[i-1][2]) % 9901);
            // 오른쪽에 배치하는 경우
            dp[i][2] += ((dp[i-1][0] + dp[i-1][1]) % 9901);
        }

        System.out.println((dp[N][0] + dp[N][1] + dp[N][2]) % 9901);
    }
}
