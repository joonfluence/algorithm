import java.util.Arrays;
import java.util.Scanner;

/**
 *
 * [입력값]
 *
 * 10
 * 1 100 2 50 60 3 5 6 7 8
 *
 * 1. 점화식을 세운다.
 *
 * 1
 * 1 100
 * 1 100 2
 * 1 100 2 50
 * 1 100 2 50 60
 * 1 100 2 50 60 3
 * 1 100 2 50 60 3 5
 * 1 100 2 50 60 3 5 6
 * 1 100 2 50 60 3 5 6 7
 * 1 100 2 50 60 3 5 6 7 8
 *
 * dp[1] = 1
 * dp[2] = 101
 * dp[3] = 3
 * dp[4] = 53
 * dp[5] = 113
 * dp[6] = 5
 * dp[7] = 10
 * dp[8] = 16
 * dp[9] = 23
 * dp[10] = 31
 *
 * dp[i] = i번째 원소보다 크기가 작고 인덱스 값은 작은 부분 수열
 * dp[i] = max(dp[i], dp[j] + nums[i])
 *
 * 2. 순회한다.
 * 3. 조건을 작성한다.
 * 4. 출력한다.
 *
 */

public class DP_11055 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] dp = new int[N + 1];
        int[] nums = new int[N + 1];

        for (int i = 1; i < N+1; i++) {
            nums[i] = sc.nextInt();
            dp[i] = nums[i];
            for (int j = 1; j < i; j++) {
                if (nums[j] < nums[i]){
                    dp[i] = Math.max(dp[i], dp[j] + nums[i]);
                }
            }
        }

        System.out.println(Arrays.stream(dp).max().getAsInt());
    }
}
