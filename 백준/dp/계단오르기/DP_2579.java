package 계단오르기;
import java.util.Scanner;

/*

1. 점화식을 구한다

dp[i] = max(dp[i-2] + nums[i], dp[i-3] + nums[i-1] + nums[i])



 */
public class DP_2579 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int N = in.nextInt();

        int[] DP = new int[N + 1];
        int[] arr = new int[N + 1];


        for (int i = 1; i <= N; i++) {
            arr[i] =in.nextInt();
        }

        // index = 0 은 시작점이므로 0이다.
        DP[1] = arr[1];

        // N 이 1이 입력될 수도 있기 때문에 예외처리를 해줄 필요가 있다.
        if (N >= 2) {
            DP[2] = arr[1] + arr[2];
        }

        for (int i = 3; i <= N; i++) {
            DP[i] = Math.max(DP[i - 2] , DP[i - 3] + arr[i - 1]) + arr[i];
        }

        System.out.println(DP[N]);
    }
}
