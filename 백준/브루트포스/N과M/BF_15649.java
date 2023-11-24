package 브루트포스.N과M;

import java.util.*;

/*

순열 https://www.acmicpc.net/problem/15649 https://st-lab.tistory.com/114

1. 숫자 조합을 입력 받는다.
2. 뽑아야 할 숫자를 계산한다.

 */
public class BF_15649 {
    private static int[] arr;
    private static boolean[] visited;
    private static int N, M;
    private static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        N = in.nextInt();
        M = in.nextInt();
        arr = new int[M];
        visited = new boolean[N+1];
        dfs(0);
        System.out.print(sb);
    }

    private static void dfs(int depth){
        if (depth == M){
            print(M);
            return;
        }

        for (int i = 1; i <= N; i++) {
            if (!visited[i]){
                visited[i] = true;
                arr[depth] = i;
                dfs(depth+1);
                visited[i] = false;
            }
        }
    }

    private static void print(int r){
        for (int i = 0; i < r; i++) {
            sb.append(arr[i]).append(" ");
        }
        sb.append("\n");
    }
}
