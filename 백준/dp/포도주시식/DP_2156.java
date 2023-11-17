package 포도주시식;

import java.util.Arrays;
import java.util.Scanner;

/*

https://www.acmicpc.net/problem/2156 https://mygumi.tistory.com/98

1. 각 항의 관계를 구한다.

dp[i] = max(dp[i-2] + nums[i], dp[i-3] + nums[i-1] + nums[i])

2.

 */
public class DP_2156 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] dp = new int[N + 1];
        int[] nums = new int[N + 1];

        for (int i = 1; i <= N; i++) {
            nums[i] = sc.nextInt();
        }

        dp[1] = nums[1];

        if (N == 1){
            System.out.println(dp[N]);
            return;
        }

        dp[2] = nums[1] + nums[2];

        if (N < 3){
            System.out.println(dp[N]);
            return;
        }

        for (int i = 3; i <= N; i++) {
            dp[i] = Math.max(dp[i-2] + nums[i], dp[i-3] + nums[i-1] + nums[i]);
            dp[i] = Math.max(dp[i - 1], dp[i]);
        }

        System.out.println(Arrays.stream(dp).max().getAsInt());
    }
}
