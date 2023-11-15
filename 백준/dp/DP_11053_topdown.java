import java.util.Arrays;
import java.util.Scanner;

/**
 * 가장 긴 증가하는 부분 수열 (DP, 실버2)
 */

class DP_11053_topdown {

    static int[] seq;
    static int[] dp;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();
        seq = new int[N];
        dp = new int[N];
        Arrays.fill(dp, 0);

        for (int i = 0; i < N; i++) {
            seq[i] = in.nextInt();
        }

        for (int i = 0; i < N; i++) {
            LIS(i);
        }

        // 최댓값 찾기
        System.out.println(Arrays.stream(dp).max().getAsInt());
    }

    static int LIS(int N){
        // 만약 탐색하지 않던 위치의 경우
        if (dp[N] == 0){
            dp[N] = 1; // 1로 초기화
            // N-1부터 0까지 중 N보다 작은 값들을 찾는다.
            for (int i = N-1; i >= 0; i--) {
                if (seq[i] < seq[N]){
                    dp[N] = Math.max(dp[N], LIS(i) + 1);
                }
            }
        }
        return dp[N];
    }
}
