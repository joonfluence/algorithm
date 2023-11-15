package 제곱수의합;

import java.util.Arrays;
import java.util.Scanner;

/**

 1. 각 항 간의 관계를 구한다.

 - 2^2 = 4
 ...
 ...
 - 316^2 = 99856
 ...
 ...
 - 100000

 3. 해당 수가 제곱수인지 확인한다.
 4. 만약 제곱수라면 해당 값을 1로 초기화한다.
 5. 제곱수가 아니라면 가장 근접한 제곱수를 찾고, 제곱수의 조합으로 해당 숫자를 구한다.
 6. dp[i]를 정의한다.
 7. 제곱수의 합으로 구성된 값으로 구할 수 있는지 확인한다.

 - dp[1] : 1 (제곱수)
 - dp[2] : 2
 - dp[3] : 3
 - dp[4] : 1 (제곱수)
 - dp[5] : 2
 - dp[6] : 3
 - dp[7] : 4
 - dp[8] : 5
 - dp[9] : 1 (제곱수)
 - dp[10] : 2
 - dp[11] : 3
 - dp[12] : 4
 - dp[13] : 2 (9 + 4) -> Math.min(dp[13], dp[9] + dp[4])
 - dp[14] : 3

 8. 점화식을 구한다.

 - dp[i] = Math.min(dp[i], dp[i-j] + dp[j]);

 */

public class DP_1699 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] dp = new int[N+1];
        Arrays.fill(dp, 1000001);

        for (int i = 1; i <= N; i++) {
            dp[i] = dp[i - 1] + 1;
            // 제곱수이면
            if (Math.sqrt(i) % 1 == 0.0){
                dp[i] = 1;
            }

            for (int j = 1; j < i; j++) {
                dp[i] = Math.min(dp[i], dp[i-j] + dp[j]);
            }
        }
        System.out.println(dp[N]);
    }
}
