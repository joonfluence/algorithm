package 브루트포스.순열;

import java.util.Scanner;

/*

4
0 10 15 20
5 0 9 10
6 13 0 12
8 8 9 0

2
1000000 1000000
1000000 1000000

어느 한 정점에서 출발해 N개의 정점을 모두 거쳐 다시 원래의 도시로 돌아오는 순회 경로.

문제링크 : https://www.acmicpc.net/problem/10971
참고링크 : https://velog.io/@yanghl98/%EB%B0%B1%EC%A4%80-10971-%EC%99%B8%ED%8C%90%EC%9B%90-%EC%88%9C%ED%9A%8C-2-JAVA

*/

public class BF_10971 {
    private static int N;
    private static int result;
    private static int[][] nums;
    private static int[] arr;
    private static boolean[] visited;
    private static Scanner sc = new Scanner(System.in);

    public static void main(String[] args){
        N = sc.nextInt();
        nums = new int[N][N];
        visited = new boolean[N];
        result = Integer.MAX_VALUE;

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                nums[i][j] = sc.nextInt();
            }
        }

        for(int i = 0; i < N; i++) {
            visited = new boolean[N];
            visited[i] = true;
            dfs(i, i, 0, 0);
        }

        System.out.println(result);
    }

    private static void dfs(int start, int now, int depth, int cost){
        if (depth == N-1 && cost != 0 && nums[now][start] != 0){
            result = Math.min(result, cost + nums[now][start]);
            return;
        }

        // 인접 노드
        for (int i = 0; i < N; i++) {
            if (!visited[i] && nums[now][i] != 0){
                visited[i] = true;
                dfs(start, i,depth+1, cost + nums[now][i]);
                visited[i] = false;
            }
        }
    }
}
