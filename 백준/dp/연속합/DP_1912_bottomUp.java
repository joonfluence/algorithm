import java.io.IOException;
import java.util.Scanner;

/**

 [입력값]

 1. 점화식 세우기

 dp[i] = Math.max(dp[i-1] + nums[i], dp[i]);

 [10, -4, 3, 1, 5, 6, -35, 12, 21, -1]

 i -> 부분 수열에서 길이 
 
 dp[1] = 10
 dp[2] = 6
 dp[3] = 9
 dp[4] = 10
 dp[5] = 16
 dp[6] = -19
 dp[7] = 12
 dp[8] = 33
 dp[9] = 32

 2. 루프 순회하기
 3. 결과값 도출하기

 [출력값]

 4

 */

class DP_1912_bottomUp {

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] dp = new int[N+1];
        int[] nums = new int[N+1];
        int max = -1001;

        for (int i = 1; i <= N; i++) {
            nums[i] = sc.nextInt();
            dp[i] = nums[i];
            dp[i] = Math.max(dp[i-1] + nums[i], dp[i]);
            max = Math.max(max, dp[i]);
        }
        System.out.println(max);
    }
}
