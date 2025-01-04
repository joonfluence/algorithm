package RGB거리;

import java.io.*;
import java.util.StringTokenizer;

/*

https://www.acmicpc.net/problem/1149 https://m.blog.naver.com/occidere/220785383050

N : 3

1
2
3

1번과 2번
N번과 N-1번
i번과 i-1번, i+1번

cost[0][0] = 26
cost[0][1] = 40
cost[0][2] = 83

cost[1][0] = min(cost[0][1], cost[0][2]) + 49
cost[1][1] = min(cost[0][0], cost[0][2]) + 60
cost[1][2] = min(cost[0][0], cost[0][1]) + 57

cost[2][0] = min(cost[1][1], cost[0][2]) + 13
cost[2][1] = min(cost[1][0], cost[0][2]) + 89
cost[2][2] = min(cost[1][0], cost[0][1]) + 99

dp[3] = cost[0][0] + cost[1][1] + cost[2][0]

 */

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class DP_1149 {

    final static int Red = 0;
    final static int Green = 1;
    final static int Blue = 2;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        int[][] dp = new int[N+1][3];

        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            dp[i][Red] = Integer.parseInt(st.nextToken());
            dp[i][Green] = Integer.parseInt(st.nextToken());
            dp[i][Blue] = Integer.parseInt(st.nextToken());
        }

        for (int i = 1; i <= N; i++) {
            dp[i][Red] += Math.min(dp[i-1][Green], dp[i-1][Blue]);
            dp[i][Green] += Math.min(dp[i-1][Red], dp[i-1][Blue]);
            dp[i][Blue] += Math.min(dp[i-1][Red], dp[i-1][Green]);
        }

        System.out.println(Math.min(Math.min(dp[N][Red], dp[N][Green]), dp[N][Blue]));
    }
}
